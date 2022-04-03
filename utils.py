import json

info = []

# функция возвращает список всех кандидатов
def load_candidates_from_json(path):
    global info
    with open(path, "r", encoding="utf-8") as file:
        info = json.load(file)
    return info


# функция возвращает одного кандидата по его id
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


# функция возвращает кандидатов по имени
def get_candidates_by_name(candidate_name):
    return [candidate for candidate in info if candidate_name.lower() in candidate['name'].lower()]

    # не могу понять почему не так отрабатывает цикл.
    # for candidate in info:
        # if candidate_name.lower() in candidate['name'].lower():
            # return candidate


# функция возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name):
    candidate = []
    for candidates in info:
        skills = candidates['skills'].lower().split(', ')
        if skill_name in skills:
            candidate.append(candidates)
    return candidate


