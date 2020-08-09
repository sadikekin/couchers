from jinja2 import Environment, FileSystemLoader, Template
from markdown2 import markdown
from couchers.email.smtp import send_smtp_email
from couchers.email.dev import print_dev_email
from couchers.config import config

env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
)

plain_base_template = env.get_template("email_base_plain.md")
html_base_template = env.get_template("email_base_html.html")

def _render_email(subject, template_file, template_args={}):
    # we render both a plain-text and a HTML version, and embed both in the email

    template = env.get_template(f"{template_file}.md")

    # TODO(aapeli): convert to macro
    def button(text, link):
        return f"""<a style="background-color: #643073; border-radius: 3px; margin: 20px; padding: 10px 20px; color: white; text-decoration: none;" href="{link}">{text}</a>""".strip()

    plain_content = template.render(**template_args, plain=True, html=False)
    html_content = markdown(template.render(**template_args, plain=False, html=True, button=button))

    plain = plain_base_template.render(subject=subject, content=plain_content)
    html = html_base_template.render(subject=subject, content=html_content)

    return plain, html

def send_email(sender_name, sender_email, recipient, subject, plain, html):
    if config["ENABLE_EMAIL"]:
        return send_smtp_email(sender_name, sender_email, recipient, subject, plain, html)
    else:
        return print_dev_email(sender_name, sender_email, recipient, subject, plain, html)

def send_email_template(recipient, subject, template_file, template_args={}):
    plain, html = _render_email(subject, template_file, template_args)
    return send_email("Couchers.org", "signup@dev.couchers.org", recipient, subject, plain, html)
