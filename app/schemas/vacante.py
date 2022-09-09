def vacancyEntity(vacante) -> dict:
    return {
        "vancancy_id": str(vacante["_id"]),
        "position_name": vacante["position_name"],
        "company_name": vacante["company_name"],
        "currency": vacante["currency"],
        "vancancy_link": vacante["vancancy_link"],
        "required_skills":vacante["required_skills"]
    }

def vacanciesEntity(vacantes) -> list:
    return [vacancyEntity(vacante) for vacante in vacantes]