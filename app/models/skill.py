from pickletools import int4
from typing import Optional
from pydantic import BaseModel,conlist


class Skill(BaseModel):
    skill_name: str
    years_experience_skill: int