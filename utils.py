import json
import pprint


def show_all_candidates():
    """
    Показывает информацию по всем кандидатам после загрузки данных из файла json
    :return:
    """
    with open("candidates.json", encoding="utf-8") as f:
        candidates = json.load(f)
    return candidates


def show_candidate_data_by_id(uid):
    """
    Показывает информацию по кандидату на основе id
    :return:
    """
    candidates = show_all_candidates()
    for candidate in candidates:
        if candidate["id"] == int(uid):
            return candidate


def show_candidates_by_skill(skill):
    """
    Показывает кандидатов с выбранным навыком
    :return:
    """
    candidates = show_all_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        skills_purged = candidate["skills"].lower().split(", ")
        if skill_lower in skills_purged:
            skilled_candidates.append(candidate)
    return skilled_candidates

# проверки
# print(show_candidate_data_by_id(0))
# pprint.pprint(show_candidates_by_skill("go"))
