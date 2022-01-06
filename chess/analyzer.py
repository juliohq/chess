from treelib import Tree, Node

class Analyzer:
    def __init__(self, board=None, depth=5):
        self.board = board
        self.tree = Tree()
        self.depth = depth
    
    def feed(self, player):
        d = 0
        while d <= self.depth:
            pass