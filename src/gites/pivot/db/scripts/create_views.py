# encoding: utf-8
"""
gites.pivot.db

Created by francois
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from affinitic.db.interfaces import IDatabase
from gites.pivot.db.scripts.utils import parseZCML
from zope.component import getUtility

import argparse
import gites.pivot.db
import os


def main():
    desc = 'Create view hebergement_view and contact_view into Pivot Database'
    parser = argparse.ArgumentParser(description=desc)
    args = parser.parse_args()
    parseZCML(gites.pivot.db, file='script.zcml')
    hebergementView = HebergementView(args)
    hebergementView.process()


class HebergementView(object):

    def __init__(self, args):
        self.args = args

    def process(self):
        session = getUtility(IDatabase, 'mysql').session

        schema_file = os.path.join(os.path.dirname(__file__),
                                   'hebergement_view.sql')
        query = open(schema_file).read()
        session.execute(query)

        schema_file = os.path.join(os.path.dirname(__file__),
                                   'contact_view.sql')
        query = open(schema_file).read()
        session.execute(query)
