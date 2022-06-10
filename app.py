from utils import *
from flask import Flask, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def main_page():
    candidates: list[dict] = load_candidates()
    return render_template("list.html",
                           candidates_name=candidates)

@app.route("/candidate/<int:uid>")
def candidates_by_id(uid: int):
    candidate: dict = get_candidate(uid)
    if not candidate:
        return 'Нет такого кандидата'
    return render_template("card.html",
                           candidate=candidate)


@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)

    return render_template("search.html",
                           name=candidates,
                           )


@app.route("/skill/<skill_name>")
def search_by_skills(skill_name):
    candidates_by_skills = get_candidates_by_skill(skill_name)
    return render_template("skill.html",
                           skill_name=skill_name,
                           candidates=candidates_by_skills
                           )


app.run()
