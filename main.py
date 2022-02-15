from flask import Flask
from utils import show_all_candidates, show_candidates_by_skill, show_candidate_data_by_id

app = Flask(__name__)


@app.route("/",)
def page_main():
    candidates = show_all_candidates()
    content = ""

    for candidate in candidates:
        content += candidate["name"] + "\n"
        content += candidate["position"] + "\n"
        content += candidate["skills"] + "\n"
        content += "\n"

    return "<pre>" + content + "</pre>"


@app.route("/candidate/<uid>",)
def candidate_by_id(uid):
    candidate = show_candidate_data_by_id(uid)
    content = ""
    picture_link = candidate["picture"]

    content += picture_link + "\n"
    content += candidate["name"] + "\n"
    content += candidate["position"] + "\n"
    content += candidate["skills"] + "\n"
    content += "\n"

    return "<pre>" + content + "</pre>"


@app.route("/skill/<skill_name>",)
def candidates_by_skill(skill_name):
    skilled_candidates = show_candidates_by_skill(skill_name)
    content = ""

    for candidate in skilled_candidates:
        content += candidate["name"] + "\n"
        content += candidate["position"] + "\n"
        content += candidate["skills"] + "\n"
        content += "\n"

    return "<pre>" + content + "</pre>"


app.run()

