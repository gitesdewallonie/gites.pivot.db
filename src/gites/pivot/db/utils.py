# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from bs4 import BeautifulSoup


def convert_html(value):
    return unicode(BeautifulSoup(value))
