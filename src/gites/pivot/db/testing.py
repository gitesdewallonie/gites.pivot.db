# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db.interfaces import IDatabase
from affinitic.testing import DatabaseTestCase
from zope.component import getUtility


class PivotDBTestCase(DatabaseTestCase):
    databases = ('pivot', )

    @property
    def pivot_session(self):
        return getUtility(IDatabase, 'mysql').session
