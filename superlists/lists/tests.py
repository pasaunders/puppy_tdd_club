from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    """Test home page."""

    def test_root_url_is_home_page(self):
        """Unit test, checks whether the home page is at the expected url."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_html(self):
        """Unit test checking that home page html is as expected."""
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
