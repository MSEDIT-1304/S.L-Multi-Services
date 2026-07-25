from flask import Flask, render_template, Response

app = Flask(__name__)

SERVICES_SEO = {

    "electricien": {
        "titre": "Électricien à Rethel",
        "description": "Travaux d'électricité générale, dépannage, rénovation et mise aux normes.",
        "texte": """
S.L Multi Services réalise tous vos travaux d'électricité générale à Rethel et dans les communes voisines.
Nous intervenons pour les dépannages électriques, les rénovations complètes, les mises aux normes,
le remplacement de tableaux électriques, les prises, les interrupteurs, l'éclairage intérieur et extérieur,
ainsi que les installations électriques dans les logements et petits bâtiments.

Notre entreprise intervient notamment à Rethel, Signy-l'Abbaye, La Romagne, Lalobbe,
Draize, Saint-Jean-aux-Bois, Montmeillant, Chaumont-Porcien et dans les communes environnantes.

Chaque intervention est réalisée avec sérieux, dans le respect des normes en vigueur,
avec un devis gratuit avant travaux.
"""
    },

    "plombier": {
        "titre": "Plombier à Rethel",
        "description": "Installation, dépannage et réparation de plomberie.",
        "texte": """
S.L Multi Services intervient pour tous vos travaux de plomberie.
Recherche de fuite, remplacement de robinetterie, réparation de canalisations,
installation de sanitaires, remplacement de chauffe-eau et dépannage rapide.

Nous intervenons à Rethel ainsi que dans les communes voisines.
"""
    },

    "chauffagiste": {
        "titre": "Chauffagiste à Rethel",
        "description": "Installation et entretien de chauffage.",
        "texte": """
Installation de radiateurs, entretien de chauffage,
remplacement d'équipements et interventions rapides
dans le secteur de Rethel et des Ardennes.
"""
    },

    "entretien-jardin": {
        "titre": "Entretien de jardin à Rethel",
        "description": "Entretien de jardins et espaces verts.",
        "texte": """
Tonte, taille de haies, débroussaillage,
nettoyage de terrains et entretien extérieur
à Rethel et dans les communes voisines.
"""
    },

    "pose-clotures": {
        "titre": "Pose de clôtures à Rethel",
        "description": "Installation de clôtures et portillons.",
        "texte": """
Pose de clôtures rigides, grillages,
portillons et réparations de clôtures
pour particuliers.
"""
    }

}

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/regions")
def regions():
    return render_template("regions.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")


@app.route("/<service>")
def seo(service):

    if service not in SERVICES_SEO:
        return "Page introuvable", 404

    return render_template(
        "seo.html",
        service=SERVICES_SEO[service]
    )

@app.route("/sitemap.xml")
def sitemap():

    xml = render_template(
        "sitemap.xml",
        services=SERVICES_SEO.keys()
    )

    return Response(xml, mimetype="application/xml")

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")
    
if __name__ == "__main__":
    app.run(debug=True)
