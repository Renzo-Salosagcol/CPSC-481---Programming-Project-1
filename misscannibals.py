from search import *


class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    # YOUR CODE GOES HERE
    def goal_test(self, state):
        # print(str(state[0]) + ", " + str(state[1]) + ", " + str(state[2]))
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

        # print(action)
        # return new state
        return(newNumMiss, newNumCann, not state[2])


    def actions(self, state):
        # actions = ['M', 'MM', 'MC', 'CC', 'C']
        # startMiss = self.M
        # startCann = self.C
        #
        # tempState = state
        # if state[2] == False: #Reverse if on Right bank
        #     state = (startMiss - state[0], startCann - state[1], False)

        # ************DO NOT DELETE************
        # #Check each possible actions
        # if (state[0] - 1 != state[1] and state[0] != 1) or state[0] < 1:
        #     actions.remove('M')
        # if (state[0] - 2 < state[1] and state[0] != 2) or state[0] <= 1:
        #     actions.remove('MM')
        # if (state[0] != state[1]) or state[0] < 1 or state[1] < 1:
        #     actions.remove('MC')
        # if (state[1] - 2 < startMiss - state[0] and state[0] != 0) or state[1] <= 1:
        #     actions.remove('CC')
        # if (state[1] - 1 < state[0] and state[0] != 0 and startMiss != state[0]) or state[1] < 1:
        #     actions.remove('C')
        # ************DO NOT DELETE************
        actions = []
        removeValues = []

        # LEFT side possible values
        if state[2]:
            if state[0] >= 1:
                actions.append('M')
            if state[0] >= 2:
                actions.append('MM')
            if state[0] >= 1 and state[1] >= 1:
                actions.append('MC')
            if state[1] >= 2:
                actions.append('CC')
            if state[1] >= 1:
                actions.append('C')

            # REMOVE unusable values
            # for i in actions:
            #     if 'MC' == i:
            #         if state[0] != state[1]:
            #             removeValues.append(i)
            #     elif 'M' in i and state[0] + i.count('M') != 0:
            #         if state[0] - (1 * i.count('M')) < state[1]:
            #             removeValues.append(i)
            #     elif 'C' in i and self.initial[0] - state[0] != 0:
            #         if self.initial[1] - state[1] + (1 * i.count('C')) > self.initial[0] - state[0]:
            #             removeValues.append(i)

            for action in actions:
                new_state = self.result(state, action)
                if not self.is_valid(new_state):
                    removeValues.append(action)

        elif not state[2]:
            if self.initial[0] - state[0] >= 1:
                actions.append('M')
            if self.initial[0] - state[0] >= 2:
                actions.append('MM')
            if self.initial[0] - state[0] >= 1 and self.initial[1] - state[1] >= 1:
                actions.append('MC')
            if self.initial[1] - state[1] >= 2:
                actions.append('CC')
            if self.initial[1] - state[1] >= 1:
                actions.append('C')

            rightMiss = self.initial[0] - state[0]
            rightCann = self.initial[1] - state[1]

            for action in actions:
                new_state = self.result(state, action)
                if not self.is_valid(new_state):
                    removeValues.append(action)

            # for i in actions:
            #     if 'MC' == i:
            #         if state[0] != state[1]:
            #             removeValues.append(i)
            #     elif 'M' in i and rightMiss != 0 and state[0] != 0:
            #         if rightMiss - (1 * i.count('M')) < rightCann:
            #             removeValues.append(i)
            #     elif 'C' in i and rightMiss != 0 and state[0] != 0:
            #         if state[1] + (1 * i.count('C')) > state[0]:
            #             removeValues.append(i)

        for i in removeValues:
            actions.remove(i)

        return actions

    def is_valid(self, state):
        numMiss, numCann = state[0], state[1]
        if numMiss < 0 or numCann < 0 or numMiss > self.M or numCann > self.C:
            return False
        if numMiss > 0 and numMiss < numCann:
            return False
        if self.M - numCann > 0 and self.M - numMiss < self.C - numCann:
            return False
        return True

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=0)
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']

    #Test left side of bank
    # print(mc.actions((3, 3, True))) # MC, CC, C
    # print(mc.actions((3, 2, True))) # M, CC, C
    # print(mc.actions((3, 1, True))) # MM, C
    # print(mc.actions((2, 2, True))) # MM, MC
    # print(mc.actions((0, 3, True))) # CC, C
    # print(mc.actions((0, 2, True))) # CC, C
    # print(mc.actions((1, 1, True))) # M, MC

    # Test right side of bank
    # print(mc.actions((2, 2, False))) # M, MC
    # print(mc.actions((3, 1, False))) # CC, C
    # print(mc.actions((3, 2, False))) # C
    # print(mc.actions((3, 0, False))) # CC, C
    # print(mc.actions((1, 1, False))) # MM, MC
    # print(mc.actions((0, 2, False))) # MM, C
    # print(mc.actions((0, 1, False))) # M, CC, C

    # Test MissCannibals(3,1)
    # print(mc.actions((3, 1, True)))

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)