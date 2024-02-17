import os
import sys

TAB_SIZE = 4

class Node:
    def __init__(self, text):
        self.floor = self.get_floor(text)
        self.content = ""
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
    with open(path, "r") as f:
        for row in f.readlines():
            nodes.append(Node(row))


if __name__ == "__main__":
    path = "test.md"
    parse(path)
