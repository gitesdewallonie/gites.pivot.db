# encoding: utf-8
"""
gites.pivot.db

Created by francois
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import sqlalchemy as sa
from gites.pivot.db.mapper import PivotMappedClassBase


class ContactView(PivotMappedClassBase):
    __tablename__ = u'contact_view'

    id_contact = sa.Column('id_contact', sa.Integer, primary_key=True)
    civilite = sa.Column('civilite', sa.String(100))
    pro_nom1 = sa.Column('nom', sa.String(255))
    pro_prenom1 = sa.Column('prenom', sa.String(255))
    adresse = sa.Column('adresse', sa.String(255))
    numero = sa.Column('numero', sa.String(255))
    boite = sa.Column('boite', sa.String(20))
    com_cp = sa.Column('cp', sa.String(40))
    com_nom = sa.Column('commune', sa.String(255))
    pro_tel_priv = sa.Column('telephone', sa.String(255))
    pro_fax_priv = sa.Column('fax', sa.String(255))
    pro_gsm1 = sa.Column('gsm', sa.String(255))
    pro_email = sa.Column('email', sa.String(255))
    pro_url = sa.Column('url', sa.String(255))
    fk_toffres_codeCGT = sa.Column('fk_toffres_codeCGT', sa.String(20))

    @property
    def pro_adresse(self):
        if not self.adresse:
            return
        value = self.adresse
        if self.numero:
            value = u'{0}, {1}'.format(value, self.numero)
            if self.boite:
                value = u'{0}{1}'.format(value, self.boite)
        return value

    @property
    def civ_titre(self):
        civ = {'Madame': 'Mme',
               'Monsieur': 'M.',
               'Monsieur et Madame': 'M. & Mme'}
        civ = civ.get(self.civilite)
        return civ or self.civilite
