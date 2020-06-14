# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb import api_pb2 as pb_dot_api__pb2


class APIStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserById = channel.unary_unary(
                '/api.API/GetUserById',
                request_serializer=pb_dot_api__pb2.GetUserByIdReq.SerializeToString,
                response_deserializer=pb_dot_api__pb2.User.FromString,
                )


class APIServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=pb_dot_api__pb2.GetUserByIdReq.FromString,
                    response_serializer=pb_dot_api__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.API/GetUserById',
            pb_dot_api__pb2.GetUserByIdReq.SerializeToString,
            pb_dot_api__pb2.User.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
