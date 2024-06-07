from search import *


class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    # YOUR CODE GOES HERE
    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        newNumMiss = 0
        newNumCann = 0
        if state[2] == True:
            newNumMiss = state[0] - (1 * action.count('M'))
            newNumCann = state[1] - (1 * action.count('C'))
        elif state[2] == False:
            newNumMiss = state[0] + (1 * action.count('M'))
            newNumCann = state[1] + (1 * action.count('C'))

        # return new state
        return(newNumMiss, newNumCann, not state[2])


    def actions(self, state):
        actions = ['M', 'MM', 'MC', 'CC', 'C']
        startingNumMiss = self.initial[0]
        startingNumCann = self.initial[1]
        tempState = state
        if state[2] == False: #Reverse if on Right bank
            state = (startingNumMiss - state[0], startingNumCann - state[1], False)

        #Check each possible actions
        if (state[0] - 1 != state[1] and state[0] != 1) or state[0] < 1:
            actions.remove('M')
        if (state[0] - 2 < state[1] and state[0] != 2) or state[0] <= 1:
            actions.remove('MM')
        if (state[0] != state[1]) or state[0] < 1 or state[1] < 1:
            actions.remove('MC')
        if (state[1] - 2 < startingNumMiss - state[0] and state[0] != 0) or state[1] <= 1:
            actions.remove('CC')
        if (state[1] - 1 < state[0] and state[0] != 0 and startingNumMiss != state[0]) or state[1] < 1:
            actions.remove('C')

        state = tempState

        return actions

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=3)
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']

    #Test left side of bank
    print(mc.actions((3, 3, True))) # MC, CC, C
    print(mc.actions((3, 2, True))) # M, CC, C
    print(mc.actions((3, 1, True))) # MM, C
    print(mc.actions((2, 2, True))) # MM, MC
    print(mc.actions((0, 3, True))) # CC, C
    print(mc.actions((0, 2, True))) # CC, C
    print(mc.actions((1, 1, True))) # M, MC

    # Test right side of bank
    # print(mc.actions((2, 2, False))) # M, MC
    # print(mc.actions((3, 1, False))) # CC, C
    # print(mc.actions((3, 2, False))) # C
    # print(mc.actions((3, 0, False))) # CC, C
    # print(mc.actions((1, 1, False))) # MM, MC
    # print(mc.actions((0, 2, False))) # MM, C
    # print(mc.actions((0, 1, False))) # M, CC, C



    # path = depth_first_graph_search(mc).solution()
    # print(path)
    # path = breadth_first_graph_search(mc).solution()
    # print(path)