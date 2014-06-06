# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.pivot.db import testing


class TestFirst(testing.PivotDBTestCase):
    layer = testing.PIVOT_RDB

    def test_first(self):
        pass
