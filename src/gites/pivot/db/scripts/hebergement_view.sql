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
       pivot.thebergements.nbr_lits_sup,
       pivot.thebergements.nbr_lits_simple,
       pivot.thebergements.nbr_lits_double,
       pivot.thebergements.nbr_lits_superpose,
       pivot.tchambres.id_chambre,
       pivot.tchambres.nb_lits_single,
       pivot.tchambres.nb_lits_double,
       pivot.tchambres.nb_lits_sup,
       pivot.tchambres.nb_lits_bebe
from pivot.toffres
    left outer join pivot.thebergements
        on pivot.toffres.codeCGT = pivot.thebergements.codeCGT
    left outer join pivot.tchambres
        on pivot.toffres.codeCGT = pivot.tchambres.fk_toffres_codeCGT
order by codeCGT;
