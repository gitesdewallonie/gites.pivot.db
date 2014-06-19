# encoding: utf-8
"""
gites.pivot.db

Created by francois
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import sqlalchemy as sa
from gites.pivot.db.mapper import PivotMappedClassBase


class HebLitsView(PivotMappedClassBase):
    __tablename__ = u'heb_lits_view'

    codeCGT = sa.Column('codeCGT', sa.String(20), primary_key=True)
    heb_nbr_lits_sup = sa.Column('heb_nbr_lits_sup', sa.Integer)
    heb_nbr_lits_simple = sa.Column('heb_nbr_lits_simple', sa.Integer)
    heb_nbr_lits_double = sa.Column('heb_nbr_lits_double', sa.Integer)
    heb_nbr_lits_enfant = sa.Column('heb_nbr_lits_enfant', sa.Integer)


class ChLitsView(PivotMappedClassBase):
    __tablename__ = u'ch_lits_view'

    fk_toffres_codeCGT = sa.Column('fk_toffres_codeCGT', sa.String(20), primary_key=True)
    ch_nbr_lits_sup = sa.Column('ch_nbr_lits_sup', sa.Integer)
    ch_nbr_lits_simple = sa.Column('ch_nbr_lits_simple', sa.Integer)
    ch_nbr_lits_double = sa.Column('ch_nbr_lits_double', sa.Integer)
    ch_nbr_lits_enfant = sa.Column('ch_nbr_lits_enfant', sa.Integer)


class HebergementView(PivotMappedClassBase):
    __tablename__ = u'hebergement_view'

    codeCGT = sa.Column('codeCGT', sa.String(20), primary_key=True)
    nom = sa.Column('nom', sa.String(255))
    nom_nl = sa.Column('nom_nl', sa.String(255))
    nom_en = sa.Column('nom_en', sa.String(255))
    nom_de = sa.Column('nom_de', sa.String(255))
    bce = sa.Column('bce', sa.String(255))
    rue = sa.Column('rue', sa.String(255))
    rue_cplt = sa.Column('rue_cplt', sa.String(255))
    numero = sa.Column('numero', sa.String(255))
    boite = sa.Column('boite', sa.String(45))
    cp = sa.Column('cp', sa.String(255))
    localite = sa.Column('localite', sa.String(255))
    commune = sa.Column('commune', sa.String(255))
    province = sa.Column('province', sa.String(255))
    mdt = sa.Column('mdt', sa.String(100))
    coord_geo_longitude = sa.Column('coord_geo_longitude', sa.Float)
    coord_geo_latitude = sa.Column('coord_geo_latitude', sa.Float)
    classement_num = sa.Column('classement_num', sa.Integer)
    capacite1 = sa.Column('capacite1', sa.Integer)
    capacite2 = sa.Column('capacite2', sa.Integer)
    nbr_chambre = sa.Column('nbr_chambre', sa.Integer)
    descriptif = sa.Column('descriptif', sa.Text)
    descriptif_nl = sa.Column('descriptif_nl', sa.Text)
    descriptif_en = sa.Column('descriptif_en', sa.Text)
    descriptif_de = sa.Column('descriptif_de', sa.Text)
    points_forts = sa.Column('points_forts', sa.Text)
    points_forts_nl = sa.Column('points_forts_nl', sa.Text)
    points_forts_en = sa.Column('points_forts_en', sa.Text)
    points_forts_de = sa.Column('points_forts_de', sa.Text)
    pmr_acceptes = sa.Column('pmr_acceptes', sa.Boolean())
    animaux_admis = sa.Column('animaux_admis', sa.Boolean())
    non_fumeur = sa.Column('non_fumeur', sa.Boolean())
    date_creation = sa.Column('date_creation', sa.Date)
    date_modification = sa.Column('date_modification', sa.Date)
    fk_ttypesoffres_id_type_offre = sa.Column('fk_ttypesoffres_id_type_offre', sa.Integer)
    heb_nbr_lits_sup = sa.Column('heb_nbr_lits_sup', sa.Integer)
    heb_nbr_lits_simple = sa.Column('heb_nbr_lits_simple', sa.Integer)
    heb_nbr_lits_double = sa.Column('heb_nbr_lits_double', sa.Integer)
    heb_nbr_lits_enfant = sa.Column('heb_nbr_lits_enfant', sa.Integer)
    ch_nbr_lits_sup = sa.Column('ch_nbr_lits_sup', sa.Integer)
    ch_nbr_lits_simple = sa.Column('ch_nbr_lits_simple', sa.Integer)
    ch_nbr_lits_double = sa.Column('ch_nbr_lits_double', sa.Integer)
    ch_nbr_lits_enfant = sa.Column('ch_nbr_lits_enfant', sa.Integer)

    @classmethod
    def get_last_changes(cls, date):
        """Return the modified lines since the given date"""
        query = cls._session().query(cls)
        query = query.filter(cls.date_modification >= date)
        return query.all()
