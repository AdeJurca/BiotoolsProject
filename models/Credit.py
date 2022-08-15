from typing import List, Optional

from pydantic import BaseModel


class Credit(BaseModel):
    name: str
    email: str
    url: str
    orcidid: Optional[str]
    gridid: Optional[str]
    rorid: Optional[str]
    fundrefid: Optional[str]
    typeEntity: List[str]
    typeRole: str
    note: Optional[str]