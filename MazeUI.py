import sys
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDockWidget, QFileDialog, QListWidget, QMessageBox

from Agent import Agent
from Ui_MazeUI import Ui_MainWindow

matplotlib.use("Qt5Agg")  # 声明使用QT5

class MyUI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyUI,self).__init__()
        self.setupUi(self)
        self.figure = plt.figure() #可选参数,facecolor为背景颜色
        self.canvas = FigureCanvas(self.figure)
        self.timer = QTimer(self)
        self.chooseMazeButton = QtWidgets.QPushButton()
        self.chooseMazeButton.setObjectName("chooseMazeButton")
        self.chooseMazeButton.setText("选择迷宫")
        self.chooseAgentButton = QtWidgets.QPushButton()
        self.chooseAgentButton.setObjectName("chooseAgentButton")
        self.chooseAgentButton.setText("选择智能体")
        self.displayMazeButton = QtWidgets.QPushButton()
        self.displayMazeButton.setObjectName("displayMazeButton")
        self.displayMazeButton.setText("显示迷宫")
        self.displayResultButton = QtWidgets.QPushButton()
        self.displayResultButton.setObjectName("displayResultButton")
        self.displayResultButton.setText("显示结果")
        self.mazeFileName = QtWidgets.QLabel()
        self.mazeFileName.setObjectName("mazeFileName")
        self.mazeFileName.setText("当前迷宫文件：无")
        self.agentFileName = QtWidgets.QLabel()
        self.agentFileName.setObjectName("agentFileName")
        self.agentFileName.setText("当前智能体文件：无")
        
        self.horizontalLayout.addWidget(self.canvas)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.addWidget(self.chooseMazeButton)
        self.verticalLayout.addWidget(self.mazeFileName)
        self.verticalLayout.addWidget(self.chooseAgentButton)
        self.verticalLayout.addWidget(self.agentFileName)
        self.verticalLayout.addWidget(self.displayMazeButton)
        self.verticalLayout.addWidget(self.displayResultButton)

        self.chooseMazeButton.clicked.connect(self.ChooseMaze)
        self.chooseAgentButton.clicked.connect(self.ChooseAgent)
        self.displayMazeButton.clicked.connect(self.DisplayMaze)
        self.displayResultButton.clicked.connect(self.DisplayResult)
        self.timer.timeout.connect(self.DisplayNext)
    
    def ChooseMaze(self):
        fileName = QFileDialog.getOpenFileName(self,"选取文件",'./',"All Files (*)")
        fileName = fileName[0]
        self.mazeFile = fileName
        self.maze = np.load(fileName)
        self.mazeFileName.setText("当前迷宫文件：" + fileName.split('/')[-1])

    def ChooseAgent(self):
        fileName = QFileDialog.getOpenFileName(self,"选取文件",'./',"All Files (*)")
        fileName = fileName[0]
        self.qTable = np.load(fileName)
        self.agentFileName.setText("当前智能体文件：" + fileName.split('/')[-1])

    def DisplayMaze(self):
        if self.mazeFileName.text()[-1] == '无':
            QMessageBox.warning(self,"Maze","请先选择迷宫文件！",QMessageBox.Ok)
        else:
            self.maze = np.load(self.mazeFile)
            self.SetCanvas(self.maze)

    def DisplayResult(self):
        if self.mazeFileName.text()[-1] == '无':
            QMessageBox.warning(self,"Maze","请先选择迷宫文件！",QMessageBox.Ok)
        elif self.agentFileName.text()[-1] == '无':
            QMessageBox.warning(self,"Maze","请先选择智能体文件！",QMessageBox.Ok)
        else:
            self.agent = Agent(self.maze)
            self.agent.maze.SetRewardAndNextStateDict()
            self.agent.qTable = self.qTable
            state = 0
            self.stateList = []
            while self.agent.maze.GetState(state) != 0.9:
                self.stateList.append(state)
                action = np.argmax(self.agent.qTable[:,state])
                state = self.agent.GetNextState(state,action)
            self.stateList.append(state)
            self.maze[0][0] = 0.8
            self.SetCanvas(self.maze)
            self.timer.start(1000)

    def DisplayNext(self):
        if len(self.stateList) == 1:
            QMessageBox.information(self, "Maze", "演示结束！", QMessageBox.Ok)
            self.timer.stop()
            return
        state = self.stateList[1]
        self.maze[state // self.agent.maze.m][state % self.agent.maze.m] = 0.8
        self.maze[self.stateList[0] // self.agent.maze.m][self.stateList[0] % self.agent.maze.m] = 1
        self.SetCanvas(self.maze)
        self.stateList.remove(self.stateList[0])
        self.timer.start(1000)

    def SetCanvas(self,maze):
        plt.grid('on')
        [nrows,ncols] = np.shape(maze)
        ax = plt.gca()
        ax.set_xticks(np.arange(0.5, nrows, 1))
        ax.set_yticks(np.arange(0.5, ncols, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        canvas = np.copy(maze)
        plt.imshow(canvas, interpolation='none', cmap='cubehelix')
        self.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mytest=MyUI()
    mytest.show()
    app.exec_()
