from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):
    """Test home page."""

    def test_root_url_is_home_page(self):
        """Unit test, checks whether the home page is at the expected url."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_html(self):
        """Unit test checking that home page html is as expected."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_save_POST(self):
        """Unit test checking that home page can save a post request."""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
