import numpy as np

class Maze(object):
    def __init__(self,maze):
        self.maze = maze
        self.up = {}
        self.down = {}
        self.left = {}
        self.right = {}
    def GetState(self,state):
        return self.maze[state // self.m][state % self.m]
    def SetRewardAndNextStateDict(self):
        [self.m, self.n] = np.shape(self.maze)
        self.reward = np.zeros([4,self.m * self.n])
        for i in range(4):
            for j in range(self.m * self.n):
                if i == 0: # 上
                    if self.maze[j // self.m][j % self.m] == 1:
                        if (j // self.m - 1) < 0: # 超出边界回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.up[j] = j
                        elif self.maze[j // self.m - 1][j % self.m] == 0: # 撞墙回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.up[j] = j
                        elif self.maze[j // self.m - 1][j % self.m] == 0.5: # 踩到老鼠夹回报设为-5
                            self.reward[i][j] = -5
                            self.up[j] = (j // self.m - 1) * self.m + j % self.m
                        elif self.maze[j // self.m - 1][j % self.m] == 0.9: # 抵达回报设为+1
                            self.reward[i][j] = 1
                            self.up[j] = (j // self.m - 1) * self.m + j % self.m
                        elif (j // self.m - 1) == 0 and j % self.m == 0: # 回到起点回报设为-2
                            self.reward[i][j] = -2
                            self.up[j] = (j // self.m - 1) * self.m + j % self.m
                        else:
                            self.reward[i][j] = -0.1
                            self.up[j] = (j // self.m - 1) * self.m + j % self.m
                elif i == 1: # 下
                    if self.maze[j // self.m][j % self.m] == 1:
                        if (j // self.m + 1) == self.m: # 超出边界回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.down[j] = j
                        elif self.maze[j // self.m + 1][j % self.m] == 0: # 撞墙回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.down[j] = j
                        elif self.maze[j // self.m + 1][j % self.m] == 0.5: # 踩到老鼠夹回报设为-5
                            self.reward[i][j] = -5
                            self.down[j] = (j // self.m + 1) * self.m + j % self.m
                        elif self.maze[j // self.m + 1][j % self.m] == 0.9: # 抵达回报设为+1
                            self.reward[i][j] = 1
                            self.down[j] = (j // self.m + 1) * self.m + j % self.m
                        elif (j // self.m + 1) == 0 and j % self.m == 0: # 回到起点回报设为-2
                            self.reward[i][j] = -2
                            self.down[j] = (j // self.m + 1) * self.m + j % self.m
                        else:
                            self.reward[i][j] = -0.1
                            self.down[j] = (j // self.m + 1) * self.m + j % self.m
                elif i == 2: # 左
                    if self.maze[j // self.m][j % self.m] == 1:
                        if (j % self.m - 1) < 0: # 超出边界回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.left[j] = j
                        elif self.maze[j // self.m][j % self.m - 1] == 0: # 撞墙回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.left[j] = j
                        elif self.maze[j // self.m][j % self.m - 1] == 0.5: # 踩到老鼠夹回报设为-5
                            self.reward[i][j] = -5
                            self.left[j] = (j // self.m) * self.m + j % self.m - 1
                        elif self.maze[j // self.m][j % self.m - 1] == 0.9: # 抵达回报设为+1
                            self.reward[i][j] = 1
                            self.left[j] = (j // self.m) * self.m + j % self.m - 1
                        elif j // self.m == 0 and (j % self.m - 1) == 0: # 回到起点回报设为-2
                            self.reward[i][j] = -2
                            self.left[j] = (j // self.m) * self.m + j % self.m - 1
                        else:
                            self.reward[i][j] = -0.1
                            self.left[j] = (j // self.m) * self.m + j % self.m - 1
                elif i == 3: # 右
                    if self.maze[j // self.m][j % self.m] == 1:
                        if (j % self.m + 1) == self.n: # 超出边界回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.right[j] = j
                        elif self.maze[j // self.m][j % self.m + 1] == 0: # 撞墙回报设为-0.75
                            self.reward[i][j] = -0.75
                            self.right[j] = j
                        elif self.maze[j // self.m][j % self.m + 1] == 0.5: # 踩到老鼠夹回报设为-5
                            self.reward[i][j] = -5
                            self.right[j] = (j // self.m) * self.m + j % self.m + 1
                        elif self.maze[j // self.m][j % self.m + 1] == 0.9: # 抵达回报设为+1
                            self.reward[i][j] = 1
                            self.right[j] = (j // self.m) * self.m + j % self.m + 1
                        elif j // self.m == 0 and (j % self.m + 1) == 0: # 回到起点回报设为-2
                            self.reward[i][j] = -2
                            self.right[j] = (j // self.m) * self.m + j % self.m + 1
                        else:
                            self.reward[i][j] = -0.1
                            self.right[j] = (j // self.m) * self.m + j % self.m + 1
