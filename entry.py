from reward import reward
obstacle_states=[(0,1),(1,1),(1,2),(2,2),(2,3),(1,4),(2,0),(6,1),]
newstate = reward(8, (int(1), int(3)), 0.8, (int(0), int(0)),obstacle_states)

newstate.train()
print(newstate.get_Q())
newstate.test()
