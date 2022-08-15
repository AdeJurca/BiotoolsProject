from typing import List, Optional

from pydantic import BaseModel


class Credit(BaseModel):
    name: Optional[str]
    email: Optional[str]
    url: Optional[str]
    orcidid: Optional[str]
    gridid: Optional[str]
    rorid: Optional[str]
    fundrefid: Optional[str]
    typeEntity: str
    typeRole: List[str]
    note: Optional[str]

