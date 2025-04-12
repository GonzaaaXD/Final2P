from flask import Flask, render_template
from routes.movies import movie_bp

app = Flask(__name__)

# Registrar Blueprint para las rutas de películas
app.register_blueprint(movie_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
