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
from gites.pivot.db.db import PivotDB
from zope.component import getUtility
from zope.component import provideUtility
from zope.configuration import xmlconfig

import gites.pivot.db
import gocept.testdb
import os
import sqlalchemy


class PivotTestDB(PivotDB):

    @property
    def url(self):
        return self.dsn


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
        self.engine = sqlalchemy.create_engine(self.db.dsn)
        self.engine.connect()
        self.mysql = PivotTestDB()
        self.mysql.dsn = self.db.dsn

        self._create_views()
        provideUtility(self.mysql, IDatabase, 'mysql')

    def _create_views(self):
        """
        Create table views from sql files
        """
        # Tables are created automatically by mappers (?),
        # So I have to drop them before I can create the views
        self.mysql.session.execute("""
            drop table contact_view;
            drop table hebergement_view;
            drop table heb_lits_view;
            drop table ch_lits_view;
            drop table tarif_valid_view;
            drop table tarif_view;""")

        contact_view_path = os.path.join(os.path.dirname(__file__), 'scripts',
                                         'contact_view.sql')
        self.mysql.session.execute(open(contact_view_path).read())

        hebergement_view_path = os.path.join(os.path.dirname(__file__), 'scripts',
                                             'hebergement_view.sql')
        self.mysql.session.execute(open(hebergement_view_path).read())

        tarif_view_path = os.path.join(os.path.dirname(__file__), 'scripts',
                                       'tarif_view.sql')
        self.mysql.session.execute(open(tarif_view_path).read())


PIVOT_RDB = PivotRDBLayer(name='PIVOT_RDB')


class PivotDBTestCase(DatabaseTestCase):
    databases = ('pivot', )

    @property
    def pivot_session(self):
        return getUtility(IDatabase, 'mysql').session
