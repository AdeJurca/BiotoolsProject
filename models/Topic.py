from typing import Optional

from pydantic import BaseModel


class Topic(BaseModel):
    uri: Optional[str]
    item: Optional[str]
