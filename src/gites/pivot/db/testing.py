# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db.interfaces import IDatabase
from affinitic.testing import DatabaseTestCase
from gites.db.testing import RDBLayer
from zope.component import getUtility
from zope.configuration import xmlconfig

import gocept.testdb
import os
import gites.pivot.db


class PivotRDBLayer(RDBLayer):
    dbPrefix = 'pivot'
    dbName = 'pivot'
    package = gites.pivot.db

    def setupData(self):
        pass

    def testTearDown(self):
        pass

    def invalidate(self):
        """
        Invalidates the connections to the database
        """
        self.db.drop_all()

    def setupDatabase(self):
        configurationContext = self['configurationContext']
        xmlconfig.file('testing.zcml', self.package,
                       context=configurationContext)
        configurationContext.execute_actions()
        schema_file = os.path.join(os.path.dirname(__file__), 'tests',
                                   'pivot.sql')
        self.db = gocept.testdb.MySQL(schema_path=schema_file)
        self.db.create()

PIVOT_RDB = PivotRDBLayer(name='PIVOT_RDB')


class PivotDBTestCase(DatabaseTestCase):
    databases = ('pivot', )

    @property
    def pivot_session(self):
        return getUtility(IDatabase, 'mysql').session
