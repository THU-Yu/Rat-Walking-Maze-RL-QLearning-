# Rat Walking Maze(RL-QLearning)
Platform: Window10  
Version: 1.0.0  
Author: Chen YuHong  
## Section I: Dependency

Python3.7 is needed.  
Install necessary modules using pip:

程序运行环境为Python3.7，除此之外还需要安装相应的模块，可以使用pip命令安装：

`$pip3 install pyqt5`  
`$pip3 install matplotlib`  
`$pip3 install numpy`

## Section II: Introdution of folders and files

1.Introduction of each python scripts:  
	(1)Python scripts for UI:  
	----Ui_MazeUI.py: This Ui can display the maze and the result.  
	(2)Other Python scripts:  
	----Maze.py: Define class-Maze(including function).  
	----Agent.py: Define class-Agent(including function).  
	----MazeUI.py: This scripts is to display the result.  
	----Train.py: This scripts is to train agent.  
2.Introduction of folder:  
	----folder Agent: this folder saves the result of trained agent.  
	----folder Maze: this folder saves the maze.  
3.Introduction of *.ui:  
All *.ui files are made by Qt designer. You can check the details of each UI in Qt designer.

1.Python脚本介绍：  
	（1）UI界面脚本（在Ui File文件夹中）：  
	----Ui_MazeUI.py：这个UI界面可以显示迷宫和训练结果。  
	（2）其他脚本：  
	----Maze.py：这里定义了Maze类（包含其中的函数）。  
	----Agent.py：这里定义了Agent类（包含其中的函数）。  
	----MazeUI.py：这个脚本用来显示结果。  
	----Train.py：这个脚本用来训练智能体。  
2.文件夹介绍：  
	----Agent文件夹：这个文件夹保存训练好的智能体qTable。  
	----Maze文件夹：这个文件夹保存Maze文件。  
3.ui文件介绍：  
所有的ui文件都是由Qt designer设计而成，可以使用Qt designer查看各个ui界面的设计。

## Section III: How to use

First, you need to give some maze and save to .npy files.  
Second, run Train.py to train an agent based on the maze you give. After training, you can save the qTable of the agent.  
Third, run MazeUI.py and click the button to choose the maze and agent.  
Fourth, click the button(Display result) and you can see the result.

第一，给出地图资讯并保存成.npy文件。  
第二，执行Train.py脚本，训练一个基于你给定的地图的智能体，训练完后，会保存智能体的qTable。  
第三，执行MazeUI.py脚本，点击按钮选择地图和训练好的智能体。  
第四，点击显示结果按钮以显示训练后的结果。  