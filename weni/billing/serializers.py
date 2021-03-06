from django.utils import timezone as tz
from django_grpc_framework.proto_serializers import ProtoSerializer
from rest_framework import serializers
from temba.api.v2.fields import TranslatableField
from weni.billing.grpc_gen import billing_pb2


class BillingRequestSerializer(ProtoSerializer):
    org_uuid = serializers.UUIDField()
    before = serializers.DateTimeField()
    after = serializers.DateTimeField()

    def validate(self, data):
        if data["after"] > data["before"]:
            raise serializers.ValidationError('"after" should be earlier then "before"')
        return data

    def validate_after(self, value):
        if value > tz.now():
            raise serializers.ValidationError("Cannot search after this date.")
        return value

    class Meta:
        proto_class = billing_pb2.BillingRequest


class MsgSerializer(ProtoSerializer):
    uuid = serializers.UUIDField()
    text = TranslatableField()
    sent_on = serializers.DateTimeField()
    direction = serializers.CharField()

    class Meta:
        proto_class = billing_pb2.Msg


class ChannelSerializer(ProtoSerializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()

    class Meta:
        proto_class = billing_pb2.Channel


class ActiveContactDetailSerializer(ProtoSerializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    msg = MsgSerializer()
    channel = ChannelSerializer()

    def to_representation(self, flat_data):
        direction_map = {"I": billing_pb2.INPUT, "O": billing_pb2.OUTPUT}
        instance = {
            "uuid": flat_data["uuid"],
            "name": flat_data["name"],
            "msg": {
                "uuid": flat_data["msg__uuid"],
                "text": flat_data["msg__text"],
                "sent_on": flat_data["msg__sent_on"],
                "direction": direction_map[flat_data["msg__direction"]],
            },
            "channel": {"uuid": flat_data["channel__uuid"], "name": flat_data["channel__name"]},
        }
        return super().to_representation(instance)

    def message_to_data(self, data):
        return NotImplemented

    class Meta:
        proto_class = billing_pb2.ActiveContactDetail
