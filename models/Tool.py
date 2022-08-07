import json
import string
from typing import List, Optional, Any

import pydantic
from pydantic import BaseModel
from models import Function, OtherID, Topic, Publication


class CustomError(Exception):

    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Tool(BaseModel):
    name: str
    description: str
    homepage: str
    biotoolsID: str
    biotoolsCURIE: str
    version: List[str]
    otherID: List[OtherID.OtherID]
    relation: List[str]
    function: List[Function.Function]
    toolType: List[str]
    topic: List[Topic.Topic]
    operatingSystem: List[str]
    language: List[str]
    collectionID: List[str]
    elixirPlatform: List[str]
    elixirNode: List[str]
    link: List[Any]
    download: List[Any]
    publication: Optional[List[Publication.Publication]]
    credit: List[Any]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    @pydantic.validator("name")
    @classmethod
    def name_validator(cls, value):
        if len(value) == 0:
            raise CustomError(value=value, message="Name cannot be empty")
        if len(value) > 20:
            raise CustomError(value=value, message="Name is to long")
        else:
            return value

    @pydantic.validator("description")
    @classmethod
    def description_validator(cls, value):
        if len(value) > 500:
            raise CustomError(value=value, message="Description is to long")
        if len(value) < 5:
            raise CustomError(value=value, message="Description is to short")
        else:
            return value

    @pydantic.validator("version")
    @classmethod
    def version_validator(cls, value):
        for v in value:
            if any(p in v for p in string.whitespace):
                raise CustomError(value=value, message="Version number must not contain whitespaces")
            if any(p in v for p in string.punctuation.replace(".", "")):
                raise CustomError(value=value, message="Version number must not contain special characters")
        else:
            return value

