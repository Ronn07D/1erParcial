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
@app.route("/cursos")
def cursos():
    if "usuario" in session:
        return f"Bienvenido {session['usuario']} a la lista de cursos."
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
