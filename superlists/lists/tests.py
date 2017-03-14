from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    """Test home page."""

    def test_root_url_is_home_page(self):
        """Unit test, checks whether the home page is at the expected url."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
