Exemple comprends pas avec les chambres:
========================================

Dans pivot:
1 gites qui contient 5 chambres + 2 chambres
    CGT_0003_000005D3   LA MOLIGNEE
    CHB-01-00001D   LA MEUSE
    CHB-01-00001F   LA LESSE
  Ils ont chacun un lien vers la table tchambres. Je suppose donc que quand un hebergement est une chambre, il a un lien vers tchambres

Dans gites_wallons
3 chambres groupées
     heb_code_cgt | heb_pk |         heb_nom
    --------------+--------+-------------------------
     CHNA5044     |   2138 | La Mosane - La Lesse
     CHNA5043     |   2137 | La Mosane - La Meuse
     CHNA5045     |   2136 | La Mosane - La Molignée


Fonctionnement du nombre de chambre:
====================================

Dans gites_wallons:

 heb_pk |        heb_nom         | heb_cgt_cap_min | heb_cgt_cap_max | heb_cgt_nbre_chmbre | heb_lit_1p | heb_lit_2p | heb_lit_sup | heb_lit_enf
--------+------------------------+-----------------+-----------------+---------------------+------------+------------+-------------+-------------
   1905 | Aux Nids d'Hirondelles |               6 |               8 |                   3 | 2          | 2          | 0           | 1


Dans pivot:

fk_toffres_codecgt  denomination    nb_lits_single  nb_lits_double  nb_lits_sup  nb_lits_bebe
CGT_0002_0000078C   Chambre 1       null            1               1            1
CGT_0002_0000078C   Chambre 3       null            1               null         null
CGT_0002_0000078C   Chambre 2       null            1               1            null
