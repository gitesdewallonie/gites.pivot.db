# encoding: utf-8
"""
gites.pivot.db

Created by francois
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from gites.pivot.db import utils
from gites.pivot.db.mapper import PivotMappedClassBase
from gites.pivot.db.content.contactview import ContactView

import sqlalchemy as sa


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

    code_cgt_pivot = sa.Column('codeCGT', sa.String(20), primary_key=True)
    heb_nom = sa.Column('nom', sa.String(255))
    rue = sa.Column('rue', sa.String(255))
    rue_cplt = sa.Column('rue_cplt', sa.String(255))
    numero = sa.Column('numero', sa.String(255))
    boite = sa.Column('boite', sa.String(45))
    com_cp = sa.Column('cp', sa.String(255))
    heb_localite = sa.Column('localite', sa.String(255))
    com_nom = sa.Column('commune', sa.String(255))
    prov_nom = sa.Column('province', sa.String(255))
    mais_nom = sa.Column('mdt', sa.String(100))
    heb_gps_long = sa.Column('coord_geo_longitude', sa.Float)
    heb_gps_lat = sa.Column('coord_geo_latitude', sa.Float)
    heb_nombre_epis = sa.Column('classement_num', sa.Integer)
    heb_cgt_cap_min = sa.Column('capacite1', sa.Integer)
    heb_cgt_cap_max = sa.Column('capacite2', sa.Integer)
    heb_cgt_nbre_chmbre = sa.Column('nbr_chambre', sa.Integer)
    _heb_descriptif_fr = sa.Column('descriptif', sa.Text)
    _heb_descriptif_nl = sa.Column('descriptif_nl', sa.Text)
    _heb_descriptif_uk = sa.Column('descriptif_en', sa.Text)
    _heb_descriptif_de = sa.Column('descriptif_de', sa.Text)
    _heb_pointfort_fr = sa.Column('points_forts', sa.Text)
    _heb_pointfort_nl = sa.Column('points_forts_nl', sa.Text)
    _heb_pointsfort_uk = sa.Column('points_forts_en', sa.Text)
    _heb_pointsfort_de = sa.Column('points_forts_de', sa.Text)
    heb_gid_access_tous = sa.Column('pmr_acceptes', sa.Boolean())
    heb_animal = sa.Column('animaux_admis', sa.Boolean())
    _heb_fumeur = sa.Column('non_fumeur', sa.Boolean())
    heb_date_creation = sa.Column('date_creation', sa.Date)
    heb_date_modification = sa.Column('date_modification', sa.Date)
    fk_ttypesoffres_id_type_offre = sa.Column('fk_ttypesoffres_id_type_offre', sa.Integer)
    nbr_lits_sup = sa.Column('nbr_lits_sup', sa.Integer)
    nbr_lits_simple = sa.Column('nbr_lits_simple', sa.Integer)
    nbr_lits_double = sa.Column('nbr_lits_double', sa.Integer)
    nbr_lits_enfant = sa.Column('nbr_lits_enfant', sa.Integer)
    heb_code_cgt = sa.Column('code_interne_CGT', sa.String(255))

    @classmethod
    def get_last_changes(cls, date):
        """Return the modified lines since the given date"""
        query = cls._session().query(cls)
        query = query.filter(cls.heb_date_modification >= date)
        return query.all()

    @property
    def heb_adresse(self):
        if not self.rue:
            return
        value = self.rue
        if self.rue_cplt:
            value = u'{0} {1}'.format(value, self.rue_cplt)
        if self.numero:
            value = u'{0}, {1}'.format(value, self.numero)
            if self.boite:
                value = u'{0}{1}'.format(value, self.boite)
        return value

    @property
    def heb_fumeur(self):
        return not self._heb_fumeur

    @property
    def heb_descriptif_fr(self):
        return utils.convert_html(self._heb_descriptif_fr)

    @property
    def heb_descriptif_nl(self):
        return utils.convert_html(self._heb_descriptif_nl)

    @property
    def heb_descriptif_uk(self):
        return utils.convert_html(self._heb_descriptif_uk)

    @property
    def heb_descriptif_de(self):
        return utils.convert_html(self._heb_descriptif_de)

    @property
    def heb_pointfort_fr(self):
        return utils.convert_html(self._heb_pointfort_fr)

    @property
    def heb_pointfort_nl(self):
        return utils.convert_html(self._heb_pointfort_nl)

    @property
    def heb_pointsfort_uk(self):
        return utils.convert_html(self._heb_pointsfort_uk)

    @property
    def heb_pointsfort_de(self):
        return utils.convert_html(self._heb_pointsfort_de)

    @classmethod
    def get_first_contact(cls, session):
        query = session.query(ContactView)
        query = query.filter(ContactView.fk_toffres_codeCGT == cls.code_cgt_pivot)
        query = query.order_by(ContactView.id_contact)
        return query.first()
