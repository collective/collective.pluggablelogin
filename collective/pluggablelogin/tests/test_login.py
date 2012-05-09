import unittest2 as unittest
import transaction
from plone.testing.z2 import Browser
from collective.pluggablelogin.testing import FUNCTIONAL_TESTING


class TestLogin(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        # turn on registration
        portal = self.layer['portal']
        from plone.app.controlpanel.security import ISecuritySchema
        ISecuritySchema(portal).enable_self_reg = True
        portal.validate_email = False
        transaction.commit()

    def test_login_portlet(self):
        browser = Browser(self.layer['portal'])
        # access the login screen and submit the login form
        browser.open('http://nohost/plone/login')
        browser.getControl('Log in').click()
        # make sure we were redirected to login_form with a failed message.
        self.assertEqual('http://nohost/plone/login_form', browser.url)
        self.assertTrue('Login failed' in browser.contents)

    def test_register_portlet(self):
        browser = Browser(self.layer['portal'])
        # access the login screen and submit the registration form
        browser.open('http://nohost/plone/login')
        browser.handleErrors = False
        browser.getControl('Register').click()
        # make sure we were redirected to @@register with a failed message.
        self.assertEqual('http://nohost/plone/@@register', browser.url)
        self.assertTrue('There were errors' in browser.contents)
