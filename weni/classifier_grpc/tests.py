from django.contrib.auth.models import User

from django_grpc_framework.test import RPCTransactionTestCase

from temba.orgs.models import Org
from temba.classifiers.models import Classifier
from temba.classifiers.types.bothub import BothubType
from temba.classifiers.types.wit import WitType
from temba.classifiers.types.luis import LuisType
from weni.classifier_grpc.grpc_gen import classifier_pb2, classifier_pb2_grpc

# import ipdb;


class ClassifierServiceTest(RPCTransactionTestCase):
    def make_classifiers(self, org, classifier_type, quantity):

        for index in range(quantity):
            Classifier.create(
                org,
                self.admin,
                classifier_type.slug,
                f"{org.name} {classifier_type.name} classifier {index+1}",
                {},
                sync=False,
            )

    def setUp(self):
        # ipdb.set_trace()

        super().setUp()
        self.admin = User.objects.create_user(
            username="testuser", password="123", email="test@weni.ai", is_superuser=True
        )

        self.org_weni = Org.objects.create(
            name="Weni", timezone="America/Maceio", created_by=self.admin, modified_by=self.admin
        )
        self.org_push = Org.objects.create(
            name="Push", timezone="America/Maceio", created_by=self.admin, modified_by=self.admin
        )
        self.other_org = Org.objects.create(
            name="Other org", timezone="America/Maceio", created_by=self.admin, modified_by=self.admin
        )

        self.make_classifiers(self.org_weni, BothubType, 2)
        self.make_classifiers(self.org_weni, WitType, 3)
        self.make_classifiers(self.org_weni, LuisType, 5)

        self.make_classifiers(self.org_push, BothubType, 7)
        self.make_classifiers(self.org_push, WitType, 11)
        self.make_classifiers(self.org_push, LuisType, 13)

        self.stub = classifier_pb2_grpc.ClassifierControllerStub(self.channel)

    def classifier_list_request(self, **kwargs):
        return self.stub.List(classifier_pb2.ClassifierListRequest(**kwargs))

    def test_list_orgs(self):
        # ipdb.set_trace()
        response = self.classifier_list_request(org_uuid=str(self.org_weni.uuid))
        messages = [message for message in response]

        self.assertEqual(len(messages), 6)

        response = self.classifier_list_request(org_uuid=str(self.org_push.uuid))
        messages = [message for message in response]

        self.assertEqual(len(messages), 15)

    def test_list_filter(self):
        response = self.classifier_list_request(org_uuid=str(self.org_weni.uuid), classifier_type=BothubType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 2)

        response = self.classifier_list_request(org_uuid=str(self.org_weni.uuid), classifier_type=WitType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 3)

        response = self.classifier_list_request(org_uuid=str(self.org_weni.uuid), classifier_type=LuisType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 5)

        response = self.classifier_list_request(org_uuid=str(self.org_push.uuid), classifier_type=BothubType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 7)

        response = self.classifier_list_request(org_uuid=str(self.org_push.uuid), classifier_type=WitType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 11)

        response = self.classifier_list_request(org_uuid=str(self.org_push.uuid), classifier_type=LuisType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 13)

    def test_org_with_no_classifiers(self):

        response = self.classifier_list_request(org_uuid=str(self.other_org.uuid))
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)

        response = self.classifier_list_request(org_uuid=str(self.other_org.uuid), classifier_type=BothubType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)

        response = self.classifier_list_request(org_uuid=str(self.other_org.uuid), classifier_type=WitType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)

        response = self.classifier_list_request(org_uuid=str(self.other_org.uuid), classifier_type=LuisType.slug)
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)

    def test_unknown_type(self):
        response = self.classifier_list_request(org_uuid=str(self.org_weni.uuid), classifier_type="unknown")
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)

        response = self.classifier_list_request(org_uuid=str(self.org_push.uuid), classifier_type="unknown")
        messages = [message for message in response]
        self.assertEqual(len(messages), 0)
