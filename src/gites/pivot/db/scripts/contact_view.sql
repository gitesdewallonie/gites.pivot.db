create or replace view contact_view
as
select tcontacts.id_contact,
       tcontacts.civilite,
       tcontacts.nom,
       tcontacts.prenom,
       tcontacts.adresse,
       tcontacts.numero,
       tcontacts.boite,
       tcontacts.cp,
       tcontacts.commune,
       tcontacts.telephone,
       tcontacts.fax,
       tcontacts.gsm,
       tcontacts.email,
       tcontacts.url
from tcontacts
order by id_contact;
