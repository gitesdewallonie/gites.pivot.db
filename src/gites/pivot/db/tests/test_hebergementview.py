# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from datetime import datetime
from gites.pivot.db import testing
from gites.pivot.db.content import HebergementView


class TestHebergementView(testing.PivotDBTestCase):
    layer = testing.PIVOT_RDB
    pivot_sql_file = ('toffres')

    def test_get_last_changes(self):
        date = datetime(2014, 06, 1, 10, 10)
        result = HebergementView.get_last_changes(date)
