import os
import sys

TAB_SIZE = 4

class Node:
    def __init__(self, text):
        self.floor = self.get_floor(text)
        self.content = text[self.floor*TAB_SIZE:].strip("\n")
        self.parent = ""
        self.children = []

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
            if prev == None:
                prev = Node(row)
            else:
                # 次のノードのfloorが自分より大きいなら自分のchildになる
                node = Node(row)
                if node.floor > prev.floor:
                    mermaid += f"{prev.content} --> {node.content}\n"
                    prev = node
                else:
                    prev = node
    mermaid += prev.content

    print(mermaid)
 
if __name__ == "__main__":
    path = "test2.md"
    parse(path)
