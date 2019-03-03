from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='LoremIpsum1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='lorem_user@lorem.com',
            password='Password1234',
            first_name='Hakan',
            last_name='Yalcinkaya',
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.first_name)

    def test_user_change_info(self):
        """Test user change user page"""
        url = reverse('admin:core_user_change', args=[self.user.pk])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
