"""Construit les présentations : python run.py GCI 1 3 5   (ou: python run.py GCI all)."""
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import Deck
from courses import ALL

LABS = {
    "GCI": {
        "LAB-01": "Arbitrer le portefeuille de l'ANPP",
        "LAB-02": "Fixer les capacités cibles de la BANQUE SANAGA",
        "LAB-03": "Dérouler la cascade des objectifs de la BANQUE SANAGA",
        "LAB-04": "Évaluer la capacité de BAI06 et de DSS02",
        "LAB-05": "Tester les contrôles généraux informatiques de l'ANPP",
        "LAB-06": "Prioriser et analyser les tickets de KRIBILOG",
        "LAB-07": "Évaluer et décider un changement de la BANQUE SANAGA",
        "LAB-08": "Disponibilité, pénalités et reprise du suivi des conteneurs",
        "LAB-09": "Construire la matrice RACI du modèle de NOUN PAY",
        "LAB-10": "Synthèse des quatre cas : feuilles de route chiffrées",
    },
    "ACSI": {
        "LAB-01": "Construire la cartographie des risques de LiZbiZ",
        "LAB-02": "Analyser la matrice des droits de LiZbiZ",
        "LAB-03": "Coter les documents sollicités et dimensionner les échantillons",
        "LAB-04": "Contrôler une décomposition du domaine D",
        "LAB-05": "Mesurer, situer et comparer les domaines de LiZbiZ",
        "LAB-06": "Audit de conformité des paiements de l'ANPP",
        "LAB-07": "Tests substantifs sur les données de LiZbiZ",
        "LAB-08": "Audit d'infrastructure des quatre centres de LiZbiZ",
        "LAB-09": "Auditer la continuité du système central de la BANQUE SANAGA",
        "LAB-10": "Synthèse des trois cas",
    },
    "NRAC": {
        "LAB-01": "Coter le registre des risques et sa base de preuve",
        "LAB-02": "EBIOS Risk Manager : cadrage et sources de risque",
        "LAB-03": "EBIOS Risk Manager : écosystème et scénario opérationnel",
        "LAB-04": "Quantifier un risque cyber avec FAIR",
        "LAB-05": "Décomposer, coter, conclure",
        "LAB-06": "Confronter une déclaration d'applicabilité aux preuves",
        "LAB-07": "Une base commune, plusieurs référentiels",
        "LAB-08": "Auditer un SMSI",
        "LAB-09": "Audit technique sur exports figés",
        "LAB-10": "Synthèse GRC : obligations, matrice, indicateurs",
    },
}

HERE = os.path.dirname(os.path.abspath(__file__))


def load(sigle, name):
    path = os.path.join(HERE, "specs", sigle, name + ".py")
    spec = importlib.util.spec_from_file_location(f"{sigle}_{name}", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def complete(sigle, day, spec):
    c = ALL[sigle]
    theme, contenu, ateliers, labs = c["jours"][day]
    for d in spec:
        if d["k"] == "maison":
            d.setdefault("ateliers", [f"**Atelier {a}** : fiche {sigle}-FICHE-{a}" for a in ateliers])
            d.setdefault("labs", [f"**{sigle}-{l}** : {LABS[sigle][l]}" for l in labs])
    return spec


def build_day(sigle, day):
    c = ALL[sigle]
    spec = complete(sigle, day, load(sigle, f"J{day:02d}"))
    deck = Deck(c, day)
    out = os.path.join(c["dossier"], f"{sigle}_J{day:02d}.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


def build_global(sigle):
    c = ALL[sigle]
    spec = load(sigle, "J00")
    deck = Deck(c, None)
    out = os.path.join(c["dossier"], f"{sigle}_00_vision_globale.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


if __name__ == "__main__":
    sigle = sys.argv[1]
    days = sys.argv[2:]
    if days == ["all"]:
        days = ["0"] + [str(i) for i in range(1, 16)]
    for dd in days:
        if int(dd) == 0:
            build_global(sigle)
        else:
            build_day(sigle, int(dd))
