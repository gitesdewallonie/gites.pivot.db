# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db import utils
from gites.pivot.db import DeclarativeBase


def set_mysql_mappers(metadata, event=None):
    utils.initialize_declarative_mappers(DeclarativeBase, metadata)
    utils.initialize_defered_mappers(metadata)
