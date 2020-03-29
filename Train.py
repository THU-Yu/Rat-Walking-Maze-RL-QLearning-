import numpy as np
import random
from Maze import Maze
from Agent import Agent

mazeFileName = input("请输入迷宫文件：")
maze = np.load(mazeFileName)
mazeTraining = Maze(maze)
mazeTraining.SetRewardAndNextStateDict()
agentTraining = Agent(maze)
preTrain = input("是否使用预训练模型？（y/n）:")
if preTrain == 'y':
    agentFileName = input("请输入智能体的预训练模型文件名：")
    agentTraining.qTable = np.load(agentFileName)
trainingTime = int(input("请输入训练次数："))
epsilon = 1
learningRate = 0.5
gamma = 1
for i in range(trainingTime):
    epsilon -= 1 / (trainingTime // 2) # epsilon递减
    # 随机初始化训练起点
    state = np.random.randint(agentTraining.stateNum)
    while mazeTraining.GetState(state) != 1:
        state = np.random.randint(agentTraining.stateNum)
    time = 0
    while mazeTraining.GetState(state) != 0.9:
        # epsilon贪心策略
        if False not in (agentTraining.qTable[:,state] == [0,0,0,0]):
            action = np.random.randint(4)
        else:
            if random.random() < epsilon:
                action = np.random.randint(4)
            else:
                action = np.argmax(agentTraining.qTable[:,state])
        nextState = agentTraining.GetNextState(state,action)
        # 更新Q表
        agentTraining.qTable[action,state] =(1 - learningRate) * agentTraining.qTable[action,state] +\
            learningRate * (agentTraining.maze.reward[action,state] + gamma * np.amax(agentTraining.qTable[:,nextState]))
        state = nextState
        time += 1
        if time > 200: # 避免陷入同一个状态一致一直循环
            break
        if mazeTraining.GetState(state) == 0.5:
            break
    # 显示训练进度
    if i % (trainingTime / 10) == 0 and i != 0:
        print('episodes:' + str(i) + '/' + str(trainingTime))
print('episodes:' + str(trainingTime) + '/' + str(trainingTime))
print('训练完成！')
agentSaveFileName = input('请输入训练结果保存的文件名：')
if '.npy' in agentSaveFileName:
    agentSaveFileName = agentSaveFileName[0:-4]
np.save(agentSaveFileName,agentTraining.qTable)