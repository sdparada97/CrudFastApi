from typing import Optional
from pydantic import BaseModel,conlist

from app.models.skill import Skill

class Usuario(BaseModel):
    user_id: Optional[str]
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: conlist(Skill, min_items=1)