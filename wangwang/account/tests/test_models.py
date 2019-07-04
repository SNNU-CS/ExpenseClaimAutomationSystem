from django.test import TestCase
from account.models import User, Organization


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test1', password='test1')
        User.objects.create_user(username='test2', first_name='张', last_name='三')

    def test_user_display(self):
        test_user = User.objects.get(username='test1')
        self.assertEqual(str(test_user), 'test1()')

        test_user = User.objects.get(username='test2')
        self.assertEqual(str(test_user), 'test2(张 三)')


class OrganizationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(name='org1')

    def test_organization_name(self):
        test_org = Organization.objects.get(name='org1')
        self.assertEqual(str(test_org), 'org1')
