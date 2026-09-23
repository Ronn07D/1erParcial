from flask import Flask, render_template, redirect, url_for, session, request, make_response

# Crea la aplicación Flask
app = Flask(__name__)
app.secret_key = "unaclav3"


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Cookie creada correctamente")
    resp.set_cookie("usuario_cookie", "juan")  # Guardamos el valor en el navegador
    return resp

#lee la cookie
@app.route("/get_cookie")
def get_cookie():
    usuario = request.cookies.get("usuario_cookie")
    if usuario:
        return f"La cookie dice que el usuario es: {usuario}"
    else:
        return "No existe la cookie."

#elimina
@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("Cookie eliminada")
    resp.delete_cookie("usuario_cookie")
    return resp


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
        usuario = session["usuario"]
        resp = make_response(render_template("cursos.html", cursos=curso, usuario=usuario))
        resp.set_cookie("usuario_cookie", usuario)  # Guardamos el usuario en cookie
        return resp
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
