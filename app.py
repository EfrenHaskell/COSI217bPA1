from flask import Flask, render_template, request, redirect, jsonify
from notes import NoteBook

app = Flask(__name__)
new_notebook = NoteBook("")


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/get_notes", methods=["GET"])
def get_notes():
    return jsonify(new_notebook.notes())


@app.route("/note", methods=["GET"])
def note_page():
    note_name = request.args.get("name", type=str)
    note_contents = new_notebook.get_note(note_name)
    return render_template("page.html", note_name=note_name, note_contents=note_contents)


@app.route("/add_note", methods=["POST"])
def add_note():
    new_element = request.get_json()
    new_notebook.add(new_element["name"], new_element["content"])
    return redirect("/")


@app.route("/search")
def search():
    query_term = request.args.get('term', type=str)
    search_results = new_notebook.find(query_term)
    return jsonify(search_results)


if __name__ == "__main__":
    app.run(debug=True)
