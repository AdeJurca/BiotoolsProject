import json
from typing import List

import requests as requests

from models.Tool import Tool


def get_by_name(value: str) -> Tool:
    """
    display a tool from data.json local file by giving the name of the tool as paramter
    """
    with open("./data/data.json", 'r') as file:
        data = json.load(file)
        tools: List[Tool] = []
        for item in data:
            tools.append(Tool(**item))
        for tool in tools:
            if tool.name == value:
                print(tool.json())
                return tool
    print(f"No tool found by name:  {value}")


def get_all_tools() -> List[Tool]:
    """
    display the list of tools from data.json
    """
    with open("./data/data.json") as file:
        data = json.load(file)
        tools: List[Tool] = []
        for item in data:
            tools.append(Tool(**item))
        print("---")
        for tool in tools:
            print(tool.json())
        return tools

def get_tool_by_url(url: str) -> Tool:
    """display the in json format from the bio.tools url of the tool"""
    response = requests.get(url)
    dict_obj = json.loads(response.text)
    tool: Tool = Tool(**dict_obj)
    print(tool.json())
    print(tool)
    return tool


if __name__ == "__main__":
    tool = get_by_name("AEGeAn")
    print(tool)
    # t = get_all_tools()
    # print(t)
    # tool = get_tool_by_url("https://bio.tools/api/jaspar?format=json")
    # print("Printing tool from main: ", tool)