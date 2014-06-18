# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

import sqlalchemy.ext.declarative

from zope.component import getUtility

from affinitic.db.interfaces import IDatabase


DeclarativeBase = sqlalchemy.ext.declarative.declarative_base()


def session():
    db = getUtility(IDatabase, 'mysql')
    return db.session
