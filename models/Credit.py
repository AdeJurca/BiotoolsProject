from typing import List, Optional

from pydantic import BaseModel, root_validator


class Credit(BaseModel):
    name: Optional[str]
    email: Optional[str]
    url: Optional[str]
    orcidid: Optional[str]
    gridid: Optional[str]
    rorid: Optional[str]
    fundrefid: Optional[str]
    typeEntity: Optional[str]
    typeRole: Optional[List[str]]
    note: Optional[str]

    @root_validator
    def validate_name_email_url_presence(cls, values):
        if values.get('name') is None and values.get('email') is None and values.get('url') is None:
            raise ValueError('At least one of credit name, credit email or credit URL is mandatory.')
        return values


