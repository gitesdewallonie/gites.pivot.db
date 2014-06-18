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
    civilite = sa.Column('civilite', sa.String())
    nom = sa.Column('nom', sa.String())
    prenom = sa.Column('prenom', sa.String())
    adresse = sa.Column('adresse', sa.String())
    numero = sa.Column('numero', sa.String())
    boite = sa.Column('boite', sa.String())
    cp = sa.Column('cp', sa.String())
    commune = sa.Column('commune', sa.String())
    telephone = sa.Column('telephone', sa.String())
    fax = sa.Column('fax', sa.String())
    gsm = sa.Column('gsm', sa.String())
    email = sa.Column('email', sa.String())
    url = sa.Column('url', sa.String())
