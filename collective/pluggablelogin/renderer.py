from plone.app.portlets.manager import ColumnPortletManagerRenderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LoginPortletManagerRenderer(ColumnPortletManagerRenderer):
    template = ViewPageTemplateFile('renderer.pt')
