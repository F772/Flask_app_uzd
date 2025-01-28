from models import db, Automobiliai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("searchlaukelis")
    if search_text:
        filtered_rows = Automobiliai.query.filter(Automobiliai.gamintojas.ilike(f"{search_text}%"))
        return render_template("index.html", project=filtered_rows)
    else:
        all_projects = Automobiliai.query.all()
        return render_template("index.html", projects=all_projects)


@app.route("/auto/<int:row_id>")
def one_auto(row_id):
    project = Automobiliai.query.get(row_id)
    if project:
        return render_template("one_auto.html", project=project)
    else:
        return f"Automobilio su id {row_id} nera"


@app.route("/auto/redaguoti/<int:row_id>", methods=["get", "post"])
def update_auto(row_id):
    project = Automobiliai.query.get(row_id)
    if not project:
        return f"Automobilio su id {row_id} nera"
    if request.method == "GET":
        return render_template("update_project_forma.html", project=project)
    elif request.method == "POST":
        name = request.form.get("spalvalaukelis")
        price = float(request.form.get("kainalaukelis"))
        project.spalva = name
        project.kaina = price
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/auto/trynimas/<int:row_id>", methods=["post"])
def delete_auto(row_id):
    project = Automobiliai.query.get(row_id)
    if not project:
        return f"Automobilio su id {row_id} nera"
    else:
        db.session.delete(project)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/auto/naujas", methods=["get", "post"])
def create_auto():
    if request.method == "GET":
        return render_template("create_auto_form.html")
    if request.method == "POST":
        name = request.form.get("gamintojaslaukelis")
        model = request.form.get("modelislaukelis")
        color = request.form.get("spalvalaukelis")
        year = request.form.get("metailaukelis")
        price = float(request.form.get("kainalaukelis"))
        if name and model and color and year and price:
            new_auto = Automobiliai(gamintojas=name,
                                    modelis=model,
                                    spalva=color,
                                    metai=year,
                                    kaina=price)
            db.session.add(new_auto)
            db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=5001, debug=True)