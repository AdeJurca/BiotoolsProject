from typing import List, Any, Optional
from pydantic import BaseModel

from models.Operation import Operation


class Function(BaseModel):
    operation: Optional[List[Operation]]
    input: Optional[List[Any]]
    output: Optional[List[Any]]
    note: Optional[str]
    cmd: Optional[str]
