/* heb_lits_view */
create or replace view pivot.heb_lits_view
as
select pivot.thebergements.codeCGT,
       sum(pivot.thebergements.nbr_lits_sup) heb_nbr_lits_sup,
       sum(pivot.thebergements.nbr_lits_simple) heb_nbr_lits_simple,
       sum(pivot.thebergements.nbr_lits_double) heb_nbr_lits_double,
       sum(pivot.thebergements.nbr_lits_superpose) heb_nbr_lits_enfant
from pivot.thebergements
group by pivot.thebergements.codeCGT;


/* ch_lits_view */
create or replace view pivot.ch_lits_view
as
select pivot.tchambres.fk_toffres_codeCGT,
       sum(pivot.tchambres.nb_lits_sup) ch_nbr_lits_sup,
       sum(pivot.tchambres.nb_lits_single) ch_nbr_lits_simple,
       sum(pivot.tchambres.nb_lits_double) ch_nbr_lits_double,
       sum(pivot.tchambres.nb_lits_bebe) ch_nbr_lits_enfant
from pivot.tchambres
group by pivot.tchambres.fk_toffres_codeCGT;


/* hebergement_view */
create or replace view pivot.hebergement_view
as
select pivot.toffres.codeCGT,
       pivot.toffres.nom,
       pivot.toffres.bce,
       pivot.toffres.rue,
       pivot.toffres.rue_cplt,
       pivot.toffres.numero,
       pivot.toffres.boite,
       pivot.toffres.cp,
       pivot.toffres.localite,
       pivot.toffres.commune,
       pivot.toffres.province,
       pivot.toffres.mdt,
       pivot.toffres.coord_geo_longitude,
       pivot.toffres.coord_geo_latitude,
       pivot.toffres.classement_num,
       pivot.toffres.capacite1,
       pivot.toffres.capacite2,
       pivot.toffres.nbr_chambre,
       pivot.toffres.descriptif,
       pivot.toffres.descriptif_nl,
       pivot.toffres.descriptif_en,
       pivot.toffres.descriptif_de,
       pivot.toffres.points_forts,
       pivot.toffres.points_forts_nl,
       pivot.toffres.points_forts_en,
       pivot.toffres.points_forts_de,
       pivot.toffres.pmr_acceptes,
       pivot.toffres.animaux_admis,
       pivot.toffres.non_fumeur,
       pivot.toffres.date_creation,
       pivot.toffres.date_modification,
       pivot.toffres.fk_ttypesoffres_id_type_offre,
       heb_lits_view.heb_nbr_lits_sup,
       heb_lits_view.heb_nbr_lits_simple,
       heb_lits_view.heb_nbr_lits_double,
       heb_lits_view.heb_nbr_lits_enfant,
       ch_lits_view.ch_nbr_lits_sup,
       ch_lits_view.ch_nbr_lits_simple,
       ch_lits_view.ch_nbr_lits_double,
       ch_lits_view.ch_nbr_lits_enfant
from pivot.toffres
    left outer join pivot.heb_lits_view
        on pivot.toffres.codeCGT = heb_lits_view.codeCGT
    left outer join pivot.ch_lits_view
        on pivot.toffres.codeCGT = ch_lits_view.fk_toffres_codeCGT
order by codeCGT;
