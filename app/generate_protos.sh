find pb -name '*.proto' | protoc -I. \
  --python_out=backend/src \
  --grpc_python_out=backend/src \
  --plugin=protoc-gen-grpc_python=$(which grpc_python_plugin) \
  \
  --js_out="import_style=commonjs,binary:frontend/src" \
  --grpc-web_out="import_style=typescript,mode=grpcweb:frontend/src" \
  \
  $(xargs)