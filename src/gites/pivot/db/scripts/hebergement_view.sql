/* heb_lits_view */
create or replace view heb_lits_view
as
select thebergements.codeCGT,
       sum(thebergements.nbr_lits_sup) heb_nbr_lits_sup,
       sum(thebergements.nbr_lits_simple) heb_nbr_lits_simple,
       sum(thebergements.nbr_lits_double) heb_nbr_lits_double,
       sum(thebergements.nbr_lits_superpose) heb_nbr_lits_enfant
from thebergements
group by thebergements.codeCGT;


/* ch_lits_view */
create or replace view ch_lits_view
as
select tchambres.fk_toffres_codeCGT,
       sum(tchambres.nb_lits_sup) ch_nbr_lits_sup,
       sum(tchambres.nb_lits_single) ch_nbr_lits_simple,
       sum(tchambres.nb_lits_double) ch_nbr_lits_double,
       sum(tchambres.nb_lits_bebe) ch_nbr_lits_enfant
from tchambres
group by tchambres.fk_toffres_codeCGT;


/* hebergement_view */
create or replace view hebergement_view
as
select toffres.codeCGT,
       toffres.nom,
       toffres.rue,
       toffres.rue_cplt,
       toffres.numero,
       toffres.boite,
       toffres.cp,
       toffres.localite,
       toffres.commune,
       toffres.province,
       toffres.mdt,
       toffres.coord_geo_longitude,
       toffres.coord_geo_latitude,
       toffres.classement_num,
       toffres.capacite1,
       toffres.capacite2,
       toffres.nbr_chambre,
       toffres.descriptif,
       toffres.descriptif_nl,
       toffres.descriptif_en,
       toffres.descriptif_de,
       toffres.points_forts,
       toffres.points_forts_nl,
       toffres.points_forts_en,
       toffres.points_forts_de,
       toffres.pmr_acceptes,
       toffres.animaux_admis,
       toffres.non_fumeur,
       toffres.date_creation,
       toffres.date_modification,
       toffres.fk_ttypesoffres_id_type_offre,
       heb_lits_view.heb_nbr_lits_sup,
       heb_lits_view.heb_nbr_lits_simple,
       heb_lits_view.heb_nbr_lits_double,
       heb_lits_view.heb_nbr_lits_enfant,
       ch_lits_view.ch_nbr_lits_sup,
       ch_lits_view.ch_nbr_lits_simple,
       ch_lits_view.ch_nbr_lits_double,
       ch_lits_view.ch_nbr_lits_enfant
from toffres
    left outer join heb_lits_view
        on toffres.codeCGT = heb_lits_view.codeCGT
    left outer join ch_lits_view
        on toffres.codeCGT = ch_lits_view.fk_toffres_codeCGT
order by codeCGT;
