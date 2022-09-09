from enum import IntEnum
from typing import Optional
from pydantic import BaseModel,conlist

class CurrencyEnum(IntEnum):
    COP = 1
    USD = 2

class Vacante(BaseModel):
    vancancy_id: Optional[str]
    position_name: str
    company_name: str
    currency: Optional[CurrencyEnum]
    vancancy_link: str
    required_skills: conlist(dict, min_items=1)