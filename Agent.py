import numpy as np
from Maze import Maze

class Agent(object):
    def __init__(self,maze):
        self.maze = Maze(maze)
        self.maze.SetRewardAndNextStateDict()
        self.stateNum = self.maze.m * self.maze.n
        self.qTable = np.zeros([4, self.stateNum])
    def GetNextState(self,state,action):
        if action == 0:
            return self.maze.up[state]
        elif action == 1:
            return self.maze.down[state]
        elif action == 2:
            return self.maze.left[state]
        elif action == 3:
            return self.maze.right[state]