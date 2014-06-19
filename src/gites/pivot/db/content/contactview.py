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
    nom = sa.Column('nom', sa.String(255))
    prenom = sa.Column('prenom', sa.String(255))
    adresse = sa.Column('adresse', sa.String(255))
    numero = sa.Column('numero', sa.String(255))
    boite = sa.Column('boite', sa.String(20))
    cp = sa.Column('cp', sa.String(40))
    commune = sa.Column('commune', sa.String(255))
    telephone = sa.Column('telephone', sa.String(255))
    fax = sa.Column('fax', sa.String(255))
    gsm = sa.Column('gsm', sa.String(255))
    email = sa.Column('email', sa.String(255))
    url = sa.Column('url', sa.String(255))

    @classmethod
    def get_last_changes(cls, date):
        """Return the modified lines since the given date"""
        pass
