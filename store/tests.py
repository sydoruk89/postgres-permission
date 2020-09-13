from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Store

class StoreTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='password')
        testuser1.save()

        testpost = Store.objects.create(
            author=testuser1,
            title='T-shirts',
            body='We do sale t-shirts.',
        )
        testpost.save()
    
    def test_blog_content(self):
        store = Store.objects.get(id=1)
        actual_author = str(store.author)
        actual_title = str(store.title)
        actual_body = str(store.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'T-shirts')
        self.assertEqual(actual_body, 'We do sale t-shirts.')
