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

    def test_get_last_changes(self):
        date = datetime.datetime(1, 06, 2014, 10, 10)
        result = HebergementView.get_last_changes(date)
