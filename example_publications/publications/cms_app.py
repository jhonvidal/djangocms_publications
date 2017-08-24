from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PublicationsApphook(CMSApp):
    name = _("Publicarions")
    urls = ["publications.urls"]


apphook_pool.register(PublicationsApphook)
