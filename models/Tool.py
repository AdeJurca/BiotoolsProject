import string
from typing import List, Optional, Dict

import pydantic
import spdx_license_list
from pydantic import BaseModel

from models.Documentation import Documentation
from models.Function import Function
from models.OtherID import OtherID
from models.Publication import Publication
from models.Topic import Topic

class CustomError(Exception):

    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Tool(BaseModel):
    name: str
    description: str
    homepage: Optional[str]
    biotoolsID: Optional[str]
    biotoolsCURIE: Optional[str]
    version: List[str]
    otherID: Optional[List[OtherID]] = []
    relation: Optional[List[str]]
    function: List[Function] = []
    toolType: Optional[List[str]] = []
    topic: List[Topic]
    operatingSystem: Optional[List[str]] = []
    language: Optional[List[str]] = []
    license: str
    collectionID: Optional[List[str]] = []
    elixirPlatform: Optional[List[str]] = []
    elixirNode: Optional[List[str]] = []
    link: List[Dict]
    download: List[Dict]
    publication: Optional[List[Publication]] = []
    credit: List[Dict]
    confidence_flag: Optional[str] = None
    documentation: Optional[List[Documentation]] = []

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
