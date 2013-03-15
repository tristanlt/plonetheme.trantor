from plone.app.layout.viewlets.common import ViewletBase, PathBarViewlet
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PathBarViewlet(ViewletBase):
    render = ViewPageTemplateFile('path_bar.pt')
    def update(self):
        super(PathBarViewlet, self).update()
        self.navigation_root_url = self.portal_state.navigation_root_url()
        self.is_rtl = self.portal_state.is_rtl()
        breadcrumbs_view = getMultiAdapter((self.context, self.request), name='breadcrumbs_view')
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()


