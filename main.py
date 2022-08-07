import json
from typing import List

import requests as requests

from models.Tool import Tool


def get_by_name(value):
    with open("./data/data.json") as file:
        data = json.load(file)
        tools: List[Tool] = [Tool(**item) for item in data]
        for tool in tools:
            if tool.name == value:
                print(tool.toJSON())
                return
    print(f"No tool found by name:  {value}")


def get_all():
    with open("../data/data.json") as file:
        data = json.load(file)
        tools: List[Tool] = [Tool(**item) for item in data]
        for tool in tools:
            print(tool.toJSON())


def get_by_url(value):
    response = requests.get(value)
    tool: Tool = Tool(**json.loads(response.text))
    print(tool.toJSON())


if __name__ == "__main__":
    get_by_name("AEGeAn")
    # get_by_url("https://bio.tools/api/clustalw2_ebi?format=json")
