from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

# данныe всех кандидатов
data = load_candidates_from_json('candidates.json')


# представление для кандидатов
@app.route('/', )
def page_index():
    return render_template('list.html', candidates=data)


# представление одного кандидата
@app.route('/candidate/<int:id_>/')
def page_profile(id_):
    candidate = get_candidate(id_)
    return render_template('single.html', candidate=candidate)


# представление кандидатов по имени
@app.route('/search/<name>/')
def page_name(name):
    names = get_candidates_by_name(name)
    return render_template('search.html', candidates=names, candidates_len=len(names))


# представление кандидатов по skills
@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    skill_names = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=skill_names, candidates_len=len(skill_names))


if __name__ == '__main__':
    app.run()

