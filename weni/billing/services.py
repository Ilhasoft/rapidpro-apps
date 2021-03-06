from django_grpc_framework import generics
from weni.billing.grpc_gen.billing_pb2 import BillingResponse
from weni.billing.queries import ActiveContactsQuery as Query
from weni.billing.serializers import BillingRequestSerializer, ActiveContactDetailSerializer


class BillingService(generics.GenericService):
    def Total(self, request, context):
        serializer = BillingRequestSerializer(message=request)
        if serializer.is_valid():
            org_uuid = serializer.validated_data["org_uuid"]
            before = serializer.validated_data["before"]
            after = serializer.validated_data["after"]
            total_count = Query.total(org_uuid, before, after)
            return BillingResponse(active_contacts=total_count)

    def Detailed(self, request, context):
        serializer = BillingRequestSerializer(message=request)
        if serializer.is_valid():
            org_uuid = serializer.validated_data["org_uuid"]
            before = serializer.validated_data["before"]
            after = serializer.validated_data["after"]
            results = Query.detailed(org_uuid, before, after)
            return ActiveContactDetailSerializer(results, many=True).message
