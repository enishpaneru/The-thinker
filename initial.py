import numpy as np
import math


class state():
    def __init__(self, grid_num, goal):
        self.goal = goal

        self.MATRIX_ROW = grid_num * grid_num

        self.R = np.matrix(np.zeros(shape=(self.MATRIX_ROW, 4)))

    def initialize(self):
        grid_num = int(math.sqrt(self.MATRIX_ROW))
        for i in range(grid_num):
            for j in range(grid_num):
                if (i, j + 1) == self.goal:
                    self.R[(j + (i * grid_num), 1)] = 100
                elif (i, j - 1) == self.goal:
                    self.R[(j + (i * grid_num), 0)] = 100
                elif (i + 1, j) == self.goal:
                    self.R[(j + (i * grid_num), 3)] = 100
                elif (i - 1, j) == self.goal:
                    self.R[(j + (i * grid_num), 2)] = 100

            if i == 0:
                for j in range(grid_num):
                    self.R[(j + (i * grid_num), 2)] = -1
                    self.R[(i + (j * grid_num), 0)] = -1
            if i == grid_num - 1:
                for j in range(grid_num):
                    self.R[(j + (i * grid_num), 3)] = -1
                    self.R[(i + (j * grid_num), 1)] = -1
        self.R[(self.goal[1] + (self.goal[0] * grid_num), 0)] = -1
        self.R[(self.goal[1] + (self.goal[0] * grid_num), 1)] = -1
        self.R[(self.goal[1] + (self.goal[0] * grid_num), 2)] = -1
        self.R[(self.goal[1] + (self.goal[0] * grid_num), 3)] = -1

        return self.R
