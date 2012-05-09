from plone.portlets.interfaces import IPortletDataProvider
from zope.interface import implements
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

    @property
    def available(self):
        mtool = getToolByName(self.context, 'portal_membership')
        if not mtool.isAnonymousUser():
            return False
        if getToolByName(self.context, 'portal_registration', None) is None:
            return False
        return mtool.checkPermission('Add portal member', self.context)

    @property
    def form(self):
        form = self.context.restrictedTraverse('@@register')
        form.update()
        return form

    render = ViewPageTemplateFile('register_portlet.pt')


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
