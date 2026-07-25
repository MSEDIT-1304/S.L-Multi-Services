from flask import Flask, render_template

app = Flask(__name__)

SERVICES_SEO = {
    "electricien": {
        "titre": "Électricien",
        "description": "Travaux électriques, dépannage, rénovation et mise aux normes."
    },
    "plombier": {
        "titre": "Plombier",
        "description": "Installation, dépannage et réparation en plomberie."
    },
    "chauffagiste": {
        "titre": "Chauffagiste",
        "description": "Installation, entretien et dépannage de chauffage."
    },
    "entretien-jardin": {
        "titre": "Entretien de jardin",
        "description": "Entretien d'espaces verts, jardinage et petits travaux extérieurs."
    },
    "pose-clotures": {
        "titre": "Pose de clôtures",
        "description": "Installation et réparation de clôtures."
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

if __name__ == "__main__":
    app.run(debug=True)
