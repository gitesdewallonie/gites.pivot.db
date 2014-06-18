# -*- coding: utf-8 -*-
"""
gites.pivot.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.pivot.db.mapper import PivotMappedClassBase


class HebergementView(PivotMappedClassBase):
    __tablename__ = u'hebergement_view'
