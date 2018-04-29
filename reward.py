from initial import *


class reward():
    def __init__(self, grid_num, goal, gamma, start,obstacles):
        self.obstacles=obstacles
        newstate = state(grid_num, goal)
        self.goal = goal
        self.grid_num = grid_num
        self.r_matrix = newstate.initialize()
        self.grid_num = grid_num
        self.gamma = gamma
        self.initial_state = start
        self.Q = np.matrix(np.zeros([grid_num * grid_num, 4]))
        print(self.r_matrix)

    def available_actions(self, state):
        current_state_row = self.r_matrix[state[1] + (state[0] * self.grid_num),]
        av_act = np.where(current_state_row >= 0)[1]
        return av_act

    def sample_next_action(self, available_actions_range):
        next_action = int(np.random.choice(available_actions_range, 1))

        return next_action

    def update(self, current_state_grid, action, gamma):
        current_state = current_state_grid[1] + (current_state_grid[0] * self.grid_num)

        next_state_grid = self.next_state(current_state_grid, action)
        next_state = next_state_grid[1] + (next_state_grid[0] * self.grid_num)
        max_index = np.where(self.Q[next_state,] == np.max(self.Q[next_state,]))[1]
        if max_index.shape[0] > 1:
            max_index = int(np.random.choice(max_index, size=1))
        else:
            max_index = int(max_index)
        max_value = self.Q[next_state, max_index]
        self.Q[current_state, action] = self.r_matrix[current_state, action] + gamma * max_value

    def next_state(self, current_state, action):
        next_action = None
        if action == 0:
            next_action = (current_state[0], current_state[1] - 1)
        elif action == 1:
            next_action = (current_state[0], current_state[1] + 1)
        elif action == 2:
            next_action = (current_state[0] - 1, current_state[1])
        elif action == 3:
            next_action = (current_state[0] + 1, current_state[1])
        return next_action


    def train(self):
        for i in range(7000):
            current_state_grid = (np.random.randint(0, self.grid_num), np.random.randint(0, self.grid_num))
            try:
                available_act = self.available_actions(current_state_grid)
                real_available_act=[]
                for each in available_act:
                    if self.next_state(current_state_grid,each) not in self.obstacles:
                        real_available_act.append(each)
                action = self.sample_next_action(real_available_act)
                self.update(current_state_grid, action, self.gamma)
            except:
                pass

    def test(self):
        # Testing
        steps = [self.initial_state]
        current_state_grid = self.initial_state

        loop_count = 0
        while current_state_grid != self.goal:
            current_state = current_state_grid[1] + (current_state_grid[0] * self.grid_num)
            if np.max(self.Q[current_state,]) <=0:
                print("no way possible")
                if len(steps)==1:
                    steps.append(self.initial_state)
                return steps
            next_step_index = np.where(self.Q[current_state,] == np.max(self.Q[current_state,]))[1]
            if next_step_index.shape[0] > 1:
                next_step_index = int(np.random.choice(next_step_index, size=1))
            else:
                next_step_index = int(next_step_index)

            current_state_grid = self.next_state(current_state_grid, next_step_index)
            steps.append(current_state_grid)
            loop_count += 1

        print("Most efficient path:")
        print(steps)
        return steps

    def get_Q(self):
        return self.Q
