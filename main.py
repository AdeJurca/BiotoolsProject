import json
from typing import List, Dict

import requests as requests

from models.Tool import Tool


def get_by_name(tool_name: str) -> Tool | None:
    """
    display a tool from data.json local file by giving the name of the tool as paramter
    """
    with open("./data/data.json", 'r') as file:
        data: List[Dict] = json.load(file)
        tools: List[Tool] = []
        for item in data:
            tools.append(Tool(**item))
        for tool in tools:
            if tool.name.lower() == tool_name.lower():
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


def change_tool_name(old_name: str, new_name: str) -> Tool | None:
    """change the tool name by giving the old name"""
    tool = get_by_name(old_name)
    if tool is None:
        return tool
    with open("./data/data.json", 'r', encoding='utf-8') as file:
        data: List[Dict] = json.load(file)
        tool.name = new_name
        for one_element in data:
            if str(one_element["name"]).lower() == old_name:
                one_element["name"] = str(one_element["name"]).lower().replace(old_name, new_name)
                file = open("./data/data.json", 'w+', encoding='utf-8')
                file.write(json.dumps(data, ensure_ascii=False, indent=2))
                file.close()
                return tool
    return tool


if __name__ == "__main__":
    # tool = get_by_name("JASPAR")
    # print("Tool is: ")
    # print(tool)
    # t = get_all_tools()
    # print(t)
    # tool = get_tool_by_url("https://bio.tools/api/jaspar?format=json")
    # print("Printing tool from main: ", tool)
    print(change_tool_name("aegean", "test"))
