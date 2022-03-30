from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__, template_folder='../templates')

# данных всех кандидатов
data = load_candidates_from_json('../candidates.json')


@app.route('/ ', )
def page_index():
    return render_template('list.html', candidates=data)


@app.route('candidate/<int:id>')
def page_profile(id):
    return render_template('single.html')


app.run(debug=True)
