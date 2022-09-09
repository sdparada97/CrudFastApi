from typing import Optional
from pydantic import BaseModel,conlist

class Usuario(BaseModel):
    user_id: Optional[str]
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: conlist(dict, min_items=1)