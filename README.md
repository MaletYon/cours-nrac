# Normes, Gestion des Risques et Audit de Cybersécurité (NRAC)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](NRAC_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE MSN-2S3-SEC08** · Master Professionnel en Sécurité des Systèmes Numériques · Semestre 3
Chaire UNESCO d'Afrique Centrale ACCES-TIC, sous la tutelle académique de l'École Nationale Supérieure Polytechnique de l'Université de Yaoundé I
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Du référentiel à la preuve : piloter, mesurer et auditer la sécurité.*

Un certificat n'est pas une preuve de sécurité, et une analyse de risque sans preuve n'est qu'une opinion chiffrée. Le cours enseigne à appliquer les normes, à gérer les risques et à auditer la cybersécurité en disant toujours ce que l'on sait, comment on le sait et ce que l'on ignore. Il couvre la famille ISO/IEC 27000, ISO 31000 et 27005, EBIOS Risk Manager, la quantification FAIR, l'audit technique, la GRC et le droit camerounais. Les cotes OUI / NON / NEK et les mesures μ, U, H du programme de l'auditologie y sont appliquées. Trois cas forment le fil rouge : la BANQUE SANAGA, LiZbiZ et l'ANPP.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`NRAC_main.pdf`](NRAC_main.pdf) | Traité complet (prologue, 16 chapitres, annexes), compilé depuis [`NRAC_main.tex`](NRAC_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations PowerPoint : vision d'ensemble et 15 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 17 fiches de 40 questions au format texte, à distribuer en attendant l'ouverture de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_NRAC.sty`](Style_NRAC.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | 0. Certifiée, et pourtant compromise | [`partie0/`](partie0/) |
| **I. Fondements : gouvernance, risque et incertitude** | 1. Gouverner la cybersécurité : du contrôle à la GRC · 2. Le risque cyber : notions, mesure, incertitude | [`partie1/`](partie1/) |
| **II. Méthodes : gérer les risques, conduire l'audit** | 3. ISO 31000 et ISO/IEC 27005 · 4. EBIOS Risk Manager · 5. Quantifier le risque cyber : FAIR · 6. Conduire un audit de cybersécurité · 7. Décomposer, coter, conclure | [`partie2/`](partie2/) |
| **III. Cadre normatif et juridique** | 8. La famille ISO/IEC 27000 · 9. Les autres référentiels et leurs correspondances · 10. Le cadre camerounais et africain, la déontologie | [`partie3/`](partie3/) |
| **IV. Pratique : SMSI, audit technique et GRC** | 11. Mettre en œuvre et auditer un SMSI · 12. L'audit technique de sécurité · 13. La GRC en pratique · 14. Études de cas intégratrices | [`partie4/`](partie4/) |
| **V. Défis avancés** | 15. Risques émergents et nouveaux objets d'audit | [`partie5/`](partie5/) |
| **VI. Recherche** | 16. Mesurer ce que l'on ne sait pas | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles de documents · D. Textes et normes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours. Il propose une fiche d'auto-évaluation par chapitre et dix laboratoires pratiques d'une heure, exécutés dans un bureau d'analyste virtuel et corrigés automatiquement. Le code de cours est **MSN-2S3-SEC08**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Sujet | Chapitre |
|---|---|---|
| NRAC-LAB-01 | Coter le registre des risques et sa base de preuve | 2 |
| NRAC-LAB-02 | EBIOS Risk Manager : cadrage et sources de risque | 4 |
| NRAC-LAB-03 | EBIOS Risk Manager : écosystème et scénario opérationnel | 4 |
| NRAC-LAB-04 | Quantifier un risque cyber avec FAIR | 5 |
| NRAC-LAB-05 | Décomposer, coter, conclure | 7 |
| NRAC-LAB-06 | Confronter une déclaration d'applicabilité aux preuves | 8 |
| NRAC-LAB-07 | Une base commune, plusieurs référentiels | 9 |
| NRAC-LAB-08 | Auditer un SMSI | 11 |
| NRAC-LAB-09 | Audit technique sur exports figés | 12 |
| NRAC-LAB-10 | Synthèse GRC : obligations, matrice, indicateurs | 13 |

## Sources de recherche

Le cours s'appuie sur deux prépublications de l'auteur, déposées sur HAL : *Vers l'auditologie* (`hal-05701007`) et *Modelling Epistemic Uncertainty in IS Audit* (`hal-05701270`). Les autres travaux cités comme « en préparation » ne sont pas encore publiés.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex NRAC_main`, `biber NRAC_main`, `makeindex NRAC_main`, puis deux fois `pdflatex NRAC_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py NRAC all` (Python 3 et python-pptx).

## Normes et documents sous licence

Les normes ISO, le guide EBIOS, le standard Open FAIR et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
