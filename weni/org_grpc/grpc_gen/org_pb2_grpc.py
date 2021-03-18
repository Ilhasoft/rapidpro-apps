# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from weni.org_grpc.grpc_gen import org_pb2 as weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2


class OrgControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
            "/org.OrgController/List",
            request_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgListRequest.SerializeToString,
            response_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
        )
        self.Create = channel.unary_unary(
            "/org.OrgController/Create",
            request_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgCreateRequest.SerializeToString,
            response_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
        )
        self.Retrieve = channel.unary_unary(
            "/org.OrgController/Retrieve",
            request_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgRetrieveRequest.SerializeToString,
            response_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
        )
        self.Update = channel.unary_unary(
            "/org.OrgController/Update",
            request_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.SerializeToString,
            response_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.FromString,
        )
        self.Destroy = channel.unary_unary(
            "/org.OrgController/Destroy",
            request_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgDestroyRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class OrgControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OrgControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_stream_rpc_method_handler(
            servicer.List,
            request_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgListRequest.FromString,
            response_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgCreateRequest.FromString,
            response_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.SerializeToString,
        ),
        "Retrieve": grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgRetrieveRequest.FromString,
            response_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.FromString,
            response_serializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.SerializeToString,
        ),
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgDestroyRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("org.OrgController", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OrgController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/org.OrgController/List",
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgListRequest.SerializeToString,
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/org.OrgController/Create",
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgCreateRequest.SerializeToString,
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Retrieve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/org.OrgController/Retrieve",
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgRetrieveRequest.SerializeToString,
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.Org.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/org.OrgController/Update",
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.SerializeToString,
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgUpdateRequest.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Destroy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/org.OrgController/Destroy",
            weni_dot_org__grpc_dot_grpc__gen_dot_org__pb2.OrgDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
