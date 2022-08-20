from typing import List, Optional

from pydantic import BaseModel


class Documentation(BaseModel):
    url: str
    type: List[str]
    note: Optional[str]
