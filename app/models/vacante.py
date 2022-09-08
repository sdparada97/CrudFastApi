from enum import IntEnum
from typing import Optional
from pydantic import BaseModel,conlist

from models.skill import Skill

class CurrencyEnum(IntEnum):
    COP = 1
    USD = 2

class Vacante(BaseModel):
    vancancy_id: Optional[str]
    position_name: str
    company_name: CurrencyEnum
    currency: str
    vancancy_link: str
    required_skills: conlist(Skill, min_items=1)