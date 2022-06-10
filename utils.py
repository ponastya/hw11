import json

FILENAME = "candidates.json"


def load_candidates_from_json(path) -> list[dict]:
    """ Возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def load_candidates():
    return load_candidates_from_json(FILENAME)


def get_candidate(candidate_id: int):
    """ Возвращает одного кандидата по его id"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """ Возвращает кандидатов по имени"""
    candidates =  load_candidates()
    result_list = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            result_list.append(candidate)
    return result_list


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """ Возвращает кандидатов по навыку"""
    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', ') :
            result.append(candidate)
    return result