# 1. Write a simple RL loop in Pseudo code
'''
initialize environment
initialize agent
for episode in range(num_episodes):
    state = environment.reset()
    done = False
    while not done:
        action = agent.act(state)
        next_state, reward, done = environment.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
    agent.update()
    environment.render()
    agent.save()

environment.close()
'''