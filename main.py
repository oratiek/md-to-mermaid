import os
import sys

class Node:
    def __init__(self, text):
        self.content = ""
        self.parent = ""
        self.children = []

def parse(path):
    nodes = []
    with open(path, "r") as f:
        for row in f.readlines():
            print(row)

if __name__ == "__main__":
    path = "test.md"
    parse(path)
