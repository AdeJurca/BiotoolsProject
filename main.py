import json
from typing import List

import requests as requests

from models.Tool import Tool


def get_by_name(value: str) -> Tool:
    with open("./data/data.json", 'r') as file:
        data = json.load(file)
        tools: List[Tool] = [Tool(**item) for item in data]
        for tool in tools:
            if tool.name == value:
                print(tool.json())
                return tool
    print(f"No tool found by name:  {value}")


def get_all_tools() -> List[Tool]:
    with open("./data/data.json") as file:
        data = json.load(file)
        tools: List[Tool] = [Tool(**item) for item in data]
        print("---")
        for tool in tools:
            print(tool.json())
        return tools

def get_tool_by_url(url: str) -> Tool:
    response = requests.get(url)
    tool: Tool = Tool(**json.loads(response.text))
    print(tool.json())
    print(tool)
    return tool


if __name__ == "__main__":
    # tool = get_by_name("AEGeAn")
    # print(tool)
    t = get_all_tools()
    print(t)
    # tool = get_tool_by_url("https://bio.tools/api/jaspar?format=json")
    # print("Printing tool from main: ", tool)