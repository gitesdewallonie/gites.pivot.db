# encoding: utf-8
"""
gites.pivot.db

Created by schminitz
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import sqlalchemy as sa
from affinitic.db import mapper
from gites.pivot.db.mapper import PivotMappedClassBase
from gites.pivot.db.content.hebergementview import HebergementView


class TarifValidView(PivotMappedClassBase):
    __tablename__ = u'tarif_valid_view'
    id_tarif = sa.Column('id_tarif', sa.Integer, primary_key=True)


class TarifView(PivotMappedClassBase):
    __tablename__ = u'tarif_view'

    id_tarif = sa.Column('id_tarif', sa.Integer, primary_key=True)
    categorie = sa.Column('categorie', sa.Integer(1))
    type = sa.Column('type', sa.String(255))
    type_nl = sa.Column('type_nl', sa.String(255))
    type_en = sa.Column('type_en', sa.String(255))
    type_de = sa.Column('type_de', sa.String(255))
    cmt = sa.Column('complement_info', sa.Text)
    complement_info_nl = sa.Column('complement_info_nl', sa.Text)
    complement_info_en = sa.Column('complement_info_en', sa.Text)
    complement_info_de = sa.Column('complement_info_de', sa.Text)
    date = sa.Column('date', sa.Date)
    min = sa.Column('prix_min', sa.Float)
    max = sa.Column('prix_max', sa.Float)
    fk_toffres_codeCGT = sa.Column('fk_toffres_codeCGT', sa.String(20))
    heb_code_cgt = sa.Column('code_interne_CGT', sa.String(255))

    @classmethod
    def get_last_changes(cls, date):
        """Return the modified lines since the given date"""
        query = cls._session().query(cls)
        query = query.filter(cls.date >= date)
        return query.all()
