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
       tcontacts.url,
       treloffrecontact.fk_toffres_codeCGT
from tcontacts
    left join treloffrecontact
    on (tcontacts.id_contact = treloffrecontact.fk_tcontacts_id_contact
    and treloffrecontact.type like 'Propri_taire')
group by id_contact
order by id_contact;
