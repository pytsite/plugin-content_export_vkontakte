"""PytSite Vkontakte Content Export Driver
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, events
    from plugins import content_export
    from . import _driver, _eh

    # Resources
    lang.register_package(__name__, alias='content_export_vkontakte')

    # Register content export driver
    content_export.register_driver(_driver.Driver())

    events.listen('pytsite.odm.entity.pre_save.content_export', _eh.odm_entity_pre_save_content_export)


_init()
