create or replace view tarif_view
as
select ttarifs.id_tarif,
       ttarifs.categorie,
       ttarifs.type,
       ttarifs.type_nl,
       ttarifs.type_en,
       ttarifs.type_de,
       ttarifs.complement_info,
       ttarifs.complement_info_nl,
       ttarifs.complement_info_en,
       ttarifs.complement_info_de,
       ttarifs.date,
       ttarifs.prix_min,
       ttarifs.prix_max,
       ttarifs.fk_toffres_codeCGT,
       toffres.code_interne_CGT as code_interne_CGT
from ttarifs
    left join toffres
        on ttarifs.fk_toffres_codeCGT = toffres.codeCGT
order by id_tarif;
