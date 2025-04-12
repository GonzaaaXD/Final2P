from flask import Flask, render_template, request, redirect, flash
import requests

app = Flask(__name__)
app.secret_key = "SECRETO"

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
        "http://127.0.0.1:5002/peliculas/subir",
        json={"title": title, "genre": genre, "year": int(year), "classification": classification}
    )

    return redirect("/")

@app.route("/actualizar", methods=["POST"])
def actualizar_pelicula():
    movie_id = request.form.get("id")
    title = request.form.get("title")
    genre = request.form.get("genre") 
    year = request.form.get("year")
    classification = request.form.get("classification")

    # Se crea un diccionario con los datos actualizados
    data = {}
    if title:
        data["title"] = title
    if genre:
        data["genre"] = genre
    if year:
        try:
            data["year"] = int(year)
        except ValueError:
            pass  # Si no se puede convertir a int, se ignora

    # Llamar a la API para actualizar la película
    response = requests.put(
        f"http://127.0.0.1:5002/pelicula/{movie_id}",  # Asegúrate de que el endpoint sea correcto
        json=data
    )

    # Verifica si la actualización fue exitosa
    if response.status_code == 200:
        flash("Película actualizada correctamente", "success")
    else:
        flash("Error al actualizar la película", "danger")

    return redirect("/")

@app.route('/eliminar', methods=['POST'])
def eliminar_por_id_form():
    id = request.form['id']
    try:
        response = requests.delete(f"http://127.0.0.1:5002/pelicula/delete={id}")
        if response.status_code == 200:
            flash("Película eliminada exitosamente", "success")
        else:
            flash(f"Error: {response.json().get('detail', 'Error desconocido')}", "error")
    except Exception as e:
        flash(f"Error de conexión: {e}", "error")
    return redirect('/')

@app.route("/buscar", methods=["GET"])
def buscar_pelicula():
    movie_id = request.args.get("id")

    try:
        response = requests.get(f"http://127.0.0.1:5002/movies/buscar={movie_id}")
        if response.status_code == 200:
            pelicula = response.json()
            return render_template("index.html", pelicula=pelicula)
        else:
            flash(f"No se encontró la película con ID {movie_id}", "error")
            return redirect("/")
    except Exception as e:
        flash(f"Error al buscar la película: {e}", "error")
        return redirect("/")

@app.route("/peliculas", methods=["GET"])
def mostrar_peliculas():
    response = requests.get("http://127.0.0.1:5002/movies/all")
    
    if response.status_code == 200:
        peliculas = response.json()
        return render_template("index.html", peliculas=peliculas)
    else:
        flash("Error al obtener las películas", "danger")
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    