"""PytSite Vkontakte Content Export Plugin Event Handlers
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import content_export as _content_export
from plugins import vkontakte


def odm_entity_pre_save_content_export(entity: _content_export.model.ContentExport):
    if 'access_token' in entity.driver_opts and 'screen_name' not in entity.driver_opts:
        driver_opts = dict(entity.driver_opts)
        s = vkontakte.session.Session(entity.driver_opts['access_token'])
        driver_opts['title'] = s.get_screen_name(entity.driver_opts['user_id'])
        entity.f_set('driver_opts', driver_opts)
