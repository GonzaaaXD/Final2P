from flask import Blueprint, request, redirect, render_template, flash
import requests

index_bp = Blueprint("index", __name__)
API_URL = "http://127.0.0.1:5002"

@index_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@index_bp.route("/agregar", methods=["POST"])
def agregar_pelicula():
    title = request.form.get("titulo")
    genre = request.form.get("genre")
    year = request.form.get("year")
    classification = "A"  

    try:
        year = int(year)

        response = requests.post(f"{API_URL}/peliculas", json={
            "title": title,
            "genre": genre,
            "year": year,
            "classification": classification
        })

        if response.status_code == 200:
            flash("Película agregada exitosamente", "success")
        else:
            error = response.json().get("detail", "Error al agregar la película")
            flash(f"Error: {error}", "danger")

    except Exception as e:
        flash(f"Error al procesar datos: {str(e)}", "danger")

    return redirect("/")
