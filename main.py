import json
from typing import List, Dict

import requests as requests

from models.Tool import Tool


def get_by_name(tool_name: str) -> Tool:
    """
    display a tool from data.json local file by giving the name of the tool as paramter
    """
    with open("./data/data.json", 'r') as file:
        data: List[Dict] = json.load(file)
        tools: List[Tool] = []
        for item in data:
            tools.append(Tool(**item))
        for tool in tools:
            if tool.name == tool_name:
                print(tool.json())
                return tool
    print(f"No tool found by name:  {tool_name}")
    return None


def get_all_tools() -> List[Tool]:
    """
    returns all the Tool objects from the data.json file
    """
    with open("./data/data.json") as file:
        data: List[Dict] = json.load(file)
        tools: List[Tool] = []
        for one_element in data:
            tool: Tool = Tool(**one_element)
            tools.append(tool)
        print("---")
        for tool in tools:
            print(tool.json())
        return tools

def get_tool_by_url(url: str) -> Tool:
    """return the Tool object from a bio.tools API url """
    response = requests.get(url)
    dict_obj = json.loads(response.text)
    tool: Tool = Tool(**dict_obj)
    print(tool.json())
    print(tool)
    return tool


if __name__ == "__main__":
    # tool = get_by_name("JASPAR")
    # print("Tool is: ")
    # print(tool)
    t = get_all_tools()
    print(t)
    # tool = get_tool_by_url("https://bio.tools/api/jaspar?format=json")
    # print("Printing tool from main: ", tool)