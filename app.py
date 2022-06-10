from utils import *
from flask import Flask, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def main_page():
    candidates = load_candidates()
    workers = {}
    for candidate in candidates:
        workers[candidate['name']] = candidate['id']
    print(workers)
    return render_template("list.html",
                           candidates_name=workers,
                           )

@app.route("/candidate/<int:uid>")
def candidates_by_id(uid: int):
    candidate = get_candidate(uid)
    return render_template("card.html",
                           name=candidate['name'],
                           position=candidate['position'],
                           skills=candidate['skills'],
                           img=candidate['picture']
                           )


@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)

    return render_template("search.html",
                           count=len(candidates),
                           name=candidates,
                           )


@app.route("/skill/<skill_name>")
def search_by_skills(skill_name):
    candidates_by_skills = get_candidates_by_skill(skill_name)
    return render_template("skill.html",
                           count=len(candidates_by_skills),
                           skill_name=skill_name,
                           candidates=candidates_by_skills
                           )


app.run()
