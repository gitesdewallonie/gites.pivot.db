# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db.mysql import MySQLDB
from affinitic.pwmanager.interfaces import IPasswordManager
from zope.component import getUtility


class PivotDB(MySQLDB):
    db = 'pivot'
    verbose = False

    @property
    def url(self):
        pw_manager = getUtility(IPasswordManager, 'pivot')
        credentials = pw_manager.getLoginPassWithSeparator(':')

        return 'mysql://{0}@localhost/pivot'.format(credentials)
