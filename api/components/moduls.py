from pydantic import BaseModel
from typing import Literal



class FreeTextSearch(BaseModel):
    search: str
    operator: Literal['or', 'and']
