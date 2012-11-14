from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase, PathBarViewlet
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.common import ContentActionsViewlet
from plone.app.contentmenu.view import  ContentMenuProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.contentmenu.interfaces import IContentMenuView
from zope.contentprovider.provider import ContentProviderBase
from zope.interface import implements
from zope.component import getUtility
from zope.browsermenu.interfaces import IBrowserMenu

class PathBarViewlet(ViewletBase):
    render = ViewPageTemplateFile('path_bar.pt')
    def update(self):
        super(PathBarViewlet, self).update()
        self.navigation_root_url = self.portal_state.navigation_root_url()
        self.is_rtl = self.portal_state.is_rtl()
        breadcrumbs_view = getMultiAdapter((self.context, self.request), name='breadcrumbs_view')
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()


#class ContentActions(ContentActionsViewlet):
#    render = ViewPageTemplateFile("contentactions.pt")

class TrantorContentMenuProvider(ContentProviderBase):
    """Content menu provider for the "view" tab: displays the menu
    """

    implements(IContentMenuView)

    index = ViewPageTemplateFile('contentmenu.pt')

    def render(self):
        return self.index()

    # From IContentMenuView

    def available(self):
        return True

    def menu(self):
        menu = getUtility(IBrowserMenu, name='plone_contentmenu')
        items = menu.getMenuItems(self.context, self.request)
        items.reverse()
        return items