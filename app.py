from flask import Flask, render_template, redirect, url_for, session, request

# Crea la aplicación Flask
app = Flask(__name__)
app.secret_key = "unaclav3"

# Usuarios simuados
usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

# pagina principal
@app.route("/")
def home():
    return render_template("index.html")

# pagina de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        # Validar usuario y contraseña
        if usuario in usuarios and usuarios[usuario] == contraseña:
            session["usuario"] = usuario  # Guardar en sesión
            return redirect(url_for("cursos"))
        else:
            return "Usuario o contraseña incorrectos."

    return render_template("login.html")

# pagina de cursos 

curso = [
    {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
    {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
    {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
]

@app.route("/cursos")
def cursos():
    if "usuario" in session:
        return render_template("cursos.html", cursos=curso, usuario=session["usuario"])
    else:
        return redirect(url_for("login"))



# Perfil protegido
@app.route("/perfil")
def perfil():
    if "usuario" in session:
        return render_template("perfil.html", usuario=session["usuario"])
    else:
        return redirect(url_for("login"))

# Cerrar sesion
@app.route("/logout")
def logout():
    session.pop("usuario", None)  # Eliminar sesión
    return redirect(url_for("home"))

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
