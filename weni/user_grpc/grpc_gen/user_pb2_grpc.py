# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.user_grpc.grpc_gen import user_pb2 as weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2


class UserPermissionControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Retrieve = channel.unary_unary(
                '/user.UserPermissionController/Retrieve',
                request_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionRetrieveRequest.SerializeToString,
                response_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
                )
        self.Update = channel.unary_unary(
                '/user.UserPermissionController/Update',
                request_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.SerializeToString,
                response_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
                )
        self.Remove = channel.unary_unary(
                '/user.UserPermissionController/Remove',
                request_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.SerializeToString,
                response_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
                )


class UserPermissionControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserPermissionControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionRetrieveRequest.FromString,
                    response_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.FromString,
                    response_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.FromString,
                    response_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.UserPermissionController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserPermissionController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserPermissionController/Retrieve',
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionRetrieveRequest.SerializeToString,
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserPermissionController/Update',
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.SerializeToString,
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserPermissionController/Remove',
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserPermissionUpdateRequest.SerializeToString,
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.Permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class UserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Retrieve = channel.unary_unary(
                '/user.UserController/Retrieve',
                request_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.User.FromString,
                )


class UserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserRetrieveRequest.FromString,
                    response_serializer=weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserController/Retrieve',
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.UserRetrieveRequest.SerializeToString,
            weni_dot_user__grpc_dot_grpc__gen_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
