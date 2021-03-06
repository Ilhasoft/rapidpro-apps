from django_grpc_framework import generics

from temba.flows.models import Flow
from weni.flow_grpc.serializers import FlowProtoSerializer
from weni.grpc_central.services import AbstractService


class FlowService(generics.GenericService, AbstractService):
    def List(self, request, context):
        org = self.get_org_object(request.org_uuid, "uuid")
        queryset = Flow.objects.filter(name__icontains=request.flow_name, org=org.id)

        serializer = FlowProtoSerializer(queryset, many=True)
        for message in serializer.message:
            yield message
