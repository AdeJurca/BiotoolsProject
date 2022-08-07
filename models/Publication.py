from typing import Optional, List

from pydantic import BaseModel


class Publication(BaseModel):
    doi: str
    pmid: Optional[str]
    pmcid: Optional[str]
    type: Optional[List[str]]
    note: Optional[str]
    version: Optional[str]
