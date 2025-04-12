from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
app.secret_key = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar", methods=["POST"])
def agregar_pelicula():
    title = request.form["title"]
    genre = request.form["genre"]
    year = request.form["year"]
    classification = request.form["classification"]

    # Hacer petición al API
    response = requests.post(
        "http://127.0.0.1:5002/movies",
        json={"title": title, "genre": genre, "year": int(year), "classification": classification}
    )

    return redirect("/")
