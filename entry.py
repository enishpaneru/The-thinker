from reward import reward
obstacle_states=[(0,1),(1,1),(1,2),(2,2),(2,3),(1,4),(2,0),(6,1),]
goal_pos=(int(1), int(3))
thinker_pos=(int(0), int(0))
def init_thinker(goal_pos,thinker_pos,obstacle_states):
    newstate = reward(8, goal_pos, 0.8,thinker_pos ,obstacle_states)
    return newstate

def start_think(newstate):
    newstate.train()
    return newstate.test()
