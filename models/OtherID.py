from typing import Any, Optional

from pydantic import BaseModel


class OtherID(BaseModel):
    value: str
    type: str
    version: Optional[str]

