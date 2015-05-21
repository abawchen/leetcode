#  There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique. 

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if not(gas) or not(cost) or len(gas) != len(cost):
            return -1

        idx = 0
        remain = 0
        while idx < len(gas):
            remain += (gas[idx] - cost[idx])
            if remain < 0:
                remain = 0
                idx += 1
            else:
                start = idx
                for i in xrange(1, len(gas)):
                    s = (idx + i) % len(gas)
                    remain += (gas[s] - cost[s])
                    if remain < 0:
                        idx = s
                        remain = 0
                        break
                if start == idx and remain >= 0:
                    return start

                if idx == start - 1:
                    return -1

        return -1


s = Solution()

print s.canCompleteCircuit([4],[])
print s.canCompleteCircuit([],[])
print s.canCompleteCircuit([5], [6, 6])
# print s.canCompleteCircuit([5], [6])
# print s.canCompleteCircuit([5, 6], [4, 8])
# print s.canCompleteCircuit([4, 9], [5, 8])
# print s.canCompleteCircuit([5, 6, 4, 3, 2], [4, 3, 7, 2, 1])
# print s.canCompleteCircuit([50, 60, 40, 30, 20], [80, 70, 30, 1, 1])
# print s.canCompleteCircuit([50, 60, 40, 30, 20], [60, 20, 40, 70, 10])
# print s.canCompleteCircuit([50, 60, 40, 30, 20], [60, 20, 50, 70, 10])
# print s.canCompleteCircuit([50, 60, 40, 30, 200], [60, 20, 50, 70, 10])



