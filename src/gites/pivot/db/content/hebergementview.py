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

    codeCGT = sa.Column('codeCGT', sa.String(), primary_key=True)
    heb_nbr_lits_sup = sa.Column('heb_nbr_lits_sup', sa.Integer)
    heb_nbr_lits_simple = sa.Column('heb_nbr_lits_simple', sa.Integer)
    heb_nbr_lits_double = sa.Column('heb_nbr_lits_double', sa.Integer)
    heb_nbr_lits_enfant = sa.Column('heb_nbr_lits_enfant', sa.Integer)


class ChLitsView(PivotMappedClassBase):
    __tablename__ = u'ch_lits_view'

    fk_toffres_codeCGT = sa.Column('fk_toffres_codeCGT', sa.String(), primary_key=True)
    ch_nbr_lits_sup = sa.Column('ch_nbr_lits_sup', sa.Integer)
    ch_nbr_lits_simple = sa.Column('ch_nbr_lits_simple', sa.Integer)
    ch_nbr_lits_double = sa.Column('ch_nbr_lits_double', sa.Integer)
    ch_nbr_lits_enfant = sa.Column('ch_nbr_lits_enfant', sa.Integer)


class HebergementView(PivotMappedClassBase):
    __tablename__ = u'hebergement_view'

    codeCGT = sa.Column('codeCGT', sa.String(), primary_key=True)
    nom = sa.Column('nom', sa.String())
    bce = sa.Column('bce', sa.String())
    rue = sa.Column('rue', sa.String())
    rue_cplt = sa.Column('rue_cplt', sa.String())
    numero = sa.Column('numero', sa.String())
    boite = sa.Column('boite', sa.String())
    cp = sa.Column('cp', sa.String())
    localite = sa.Column('localite', sa.String())
    commune = sa.Column('commune', sa.String())
    province = sa.Column('province', sa.String())
    mdt = sa.Column('mdt', sa.String())
    coord_geo_longitude = sa.Column('coord_geo_longitude', sa.Float)
    coord_geo_latitude = sa.Column('coord_geo_latitude', sa.Float)
    classement_num = sa.Column('classement_num', sa.Integer)
    capacite1 = sa.Column('capacite1', sa.Integer)
    capacite2 = sa.Column('capacite2', sa.Integer)
    nbr_chambre = sa.Column('nbr_chambre', sa.Integer)
    descriptif = sa.Column('descriptif', sa.String())
    descriptif_nl = sa.Column('descriptif_nl', sa.String())
    descriptif_en = sa.Column('descriptif_en', sa.String())
    descriptif_de = sa.Column('descriptif_de', sa.String())
    points_forts = sa.Column('points_forts', sa.String())
    points_forts_nl = sa.Column('points_forts_nl', sa.String())
    points_forts_en = sa.Column('points_forts_en', sa.String())
    points_forts_de = sa.Column('points_forts_de', sa.String())
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
