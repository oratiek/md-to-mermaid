import os
import sys

TAB_SIZE = 4

class Node:
    def __init__(self, text):
        self.floor = self.get_floor(text)
        self.content = self.clean_content(text, self.floor)
        self.parent = ""
        self.children = []
    
    def clean_content(self, text, floor):
        return text[floor*TAB_SIZE:].strip("\n").strip(" -")

    def get_floor(self, text):
        # タブの数をみる
        floor = 0
        for char in text:
            if char != " ":
                break
            floor += 1
        return floor // TAB_SIZE

def parse(path):
    nodes = []
    prev = None
    mermaid = ""
    with open(path, "r") as f:
        for index, row in enumerate(f.readlines()):
            node = Node(row)
            nodes.append(node)
    
    mermaid = ""
    prev = nodes[0]
    for node in nodes:
        if node.floor == 0:
            mermaid += f"root --> {node.content}\n"
        # parent --> child
        if prev.floor < node.floor:
            mermaid += f"{prev.content} --> {node.content}\n"
        prev = node

    print(mermaid)




if __name__ == "__main__":
    path = "test/test.md"
    parse(path)
