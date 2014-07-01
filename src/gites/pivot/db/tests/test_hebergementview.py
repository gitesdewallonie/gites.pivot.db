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
        date = datetime(2014, 06, 1, 0, 0)
        result = HebergementView.get_last_changes(date)
        self.assertEquals(len(result), 1)

    def test_encoding(self):
        result = HebergementView.first(heb_nom='LA TURBINE')
        description = u'Maison de caractère dans un site boisé et calme (9 ha)'
        self.assertEqual(description, result.heb_descriptif_fr)

    def test_html_content(self):
        result = HebergementView.first(heb_nom='LA TURBINE')
        self.assertEqual(u'"Maison de caractère"', result.heb_descriptif_nl)
