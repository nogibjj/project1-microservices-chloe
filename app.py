from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(app)
app.app_context().push()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template("index.html", incomplete=incomplete, complete=complete)


@app.route("/add", methods=["POST"])
def add():
    # return '<h1>{}</h1>'.format(request.form['todoitem'])
    todo = Todo(text=request.form["todoitem"], complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/complete/<id>")
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete/<id>")
def delete(id):
    # if it does not exist, return 404
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        # redirect to home page
        return redirect("/")
    except:
        return "having trouble deleting task"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
