create view pivot.contact_view
as
select pivot.tcontacts.id_contact,
       pivot.tcontacts.civilite,
       pivot.tcontacts.nom,
       pivot.tcontacts.prenom,
       pivot.tcontacts.adresse,
       pivot.tcontacts.numero,
       pivot.tcontacts.boite,
       pivot.tcontacts.cp,
       pivot.tcontacts.commune,
       pivot.tcontacts.telephone,
       pivot.tcontacts.fax,
       pivot.tcontacts.gsm,
       pivot.tcontacts.email,
       pivot.tcontacts.url
from pivot.tcontacts
order by id_contact;
