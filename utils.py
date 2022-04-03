import json

info = []


def load_candidates_from_json(path):
    global info
    with open(path, "r", encoding="utf-8") as file:
        info = json.load(file)
    return info


def get_candidate(candidate_id):
    for candidate in info:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }
    return {'not found': 'Ошибка ввода'}


def get_candidates_by_name(candidate_name):
    #return [candidate for candidate in info if candidate_name in candidate['name']]

    for candidate in info:
        if candidate_name.lower() in candidate['name'].lower():
            return candidate


def get_candidates_by_skill(skill_name):
    pass
