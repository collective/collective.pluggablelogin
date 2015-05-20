from plone.portlets.interfaces import IPortletDataProvider
from zope.interface import implements
from zope.formlib.interfaces import IForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from collective.pluggablelogin import _
from plone.app.portlets.portlets import base


class IRegisterPortlet(IPortletDataProvider):
    """A portlet which can render a registration form.
    """


class Assignment(base.Assignment):
    implements(IRegisterPortlet)

    title = _(u'label_register', default=u'Register')


class Renderer(base.Renderer):

    register_page = '@@register'

    @property
    def available(self):
        mtool = getToolByName(self.context, 'portal_membership')
        if not mtool.isAnonymousUser():
            return False
        if getToolByName(self.context, 'portal_registration', None) is None:
            return False
        return mtool.checkPermission('Add portal member', self.context)

    @property
    def _form(self):
        return self.context.restrictedTraverse(self.register_page)

    @property
    def form(self):
        form = self._form
        # For z3cform based registration, form.action depends on request.URL
        if not self.is_formlib:
            form.request.URL = \
                self.context.absolute_url() + '/' + self.register_page
        form.update()
        return form

    @property
    def is_formlib(self):
        return IForm.providedBy(self._form)

    render = ViewPageTemplateFile('register_portlet.pt')


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
