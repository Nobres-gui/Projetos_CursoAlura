from jogoteca import app;
from models import Usuarios;
from flask import render_template, request, redirect, session, flash, url_for;
from helpers import FormularioLogin;
from flask_bcrypt import check_password_hash;


@app.route("/login")
def login():
    proxima = request.args.get("proxima");
    form = FormularioLogin();
    return render_template("login.html", titulo = "Login", proxima=proxima, form=form);

@app.route("/autenticar", methods=["POST", ]) 
def autenticar():
    form=FormularioLogin(request.form);
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first();
    senha = check_password_hash(usuario.senha, form.senha.data);
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname;
        flash(usuario.nickname + " logado com sucesso!!!");
        proxima_Pagina = request.form["proxima"]; 
        return redirect(proxima_Pagina);      
    else:
        flash("Usuário não encontrado");
        return redirect(url_for("login", proxima=url_for("novoJogo")));
    
@app.route("/logout")
def logout():
    session["usuario_logado"] = None;
    flash("Logout efetuado com sucesso!!!");
    return redirect(url_for("index"));

