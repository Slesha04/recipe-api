from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@test.com'
        password ='testpw'
        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )

        self.assert_(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email,'testpw')

        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        '''test where users with no email causes error'''
        pass