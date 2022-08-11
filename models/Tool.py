import string
from typing import List, Optional

import pydantic
from pydantic import BaseModel
from models import Function, OtherID, Topic, Publication
import spdx_license_list


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
    otherID: Optional[List[OtherID.OtherID]] = []
    relation: List[str]
    function: List[Function.Function] = []
    toolType: Optional[List[str]] = [] #ar trebuie default lista goala peste tot
    topic: List[Topic.Topic]
    operatingSystem: List[str] = []
    language: List[str] = []
    license: str
    collectionID: List[str] = []
    elixirPlatform: List[str] = []
    elixirNode: List[str] = []
    link: List[str] = []
    download: List[str] = []
    publication: Optional[List[Publication.Publication]] = []
    credit: List[str] = []
    confidence_flag: str = None

    #def toJSON(self):
        #return json.dumps(self, default=lambda o: o.__dict__,
                          #sort_keys=False, indent=4)

    @pydantic.validator('name')
    @classmethod
    def name_validator(cls, value):
        """CustomError raises 2 exceptions regarding the length of the name of the tool(the name needs to have at least
        one character and cannot be longer than 20 characters)"""
        if len(value) == 0:
            raise CustomError(value=value, message='Name cannot be empty')
        if len(value) > 20:
            raise CustomError(value=value, message='Name is to long')

        return value

    @pydantic.validator('description')
    @classmethod
    def description_validator(cls, value):
        """CustomError raises 2 exceptions regarding the length of the description of the tool(the description needs to
        have at least five characters and cannot be longer than 500 characters)"""
        if len(value) > 500:
            raise CustomError(value=value, message='Description is to long')
        if len(value) < 5:
            raise CustomError(value=value, message='Description is to short')

        return value

    @pydantic.validator('version')
    @classmethod
    def version_validator(cls, value):
        """CustomError raises 2 exceptions regarding the message of the version of the tool(the version cannot contain
        whitespaces or special characters"""
        for v in value:
            if any(p in v for p in string.whitespace):
                raise CustomError(value=value, message='Version number must not contain whitespaces')
            if any(p in v for p in string.punctuation.replace('.', '')):
                raise CustomError(value=value, message='Version number must not contain special characters')

            return value

    @pydantic.validator('license')
    @classmethod
    def license_validator(cls, value):
        """CustomError raises an exception regarding the fact that this license needs to be part of the list of
        commonly found licenses and exceptions -spdx- used in free and open source and other collaborative software or
        documentation"""
        if value not in spdx_license_list.LICENSES:
            raise CustomError(value=value, message=f'{value} is not a valid license')

        return value
