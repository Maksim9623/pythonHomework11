from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

# данных всех кандидатов
data = load_candidates_from_json('candidates.json')


@app.route('/', )
def page_index():
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:id_>')
def page_profile(id_):
    candidate = get_candidate(id_)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<name>')
def page_name(name):
    names = get_candidates_by_name(name)
    #print(names)
    return render_template('search.html', candidates=names, candidates_len=len(names))


app.run(debug=True)
