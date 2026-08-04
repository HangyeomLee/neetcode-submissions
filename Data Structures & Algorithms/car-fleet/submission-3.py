# how to match sorted position and speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        match = sorted(list(zip(position, speed)),reverse = True)
        stk = []
        output = 0
        count = 0
        max_time = 0
        for i in range(len(match)):
            pos,spd = match[i]
            if max_time < (target - pos)/spd:
                max_time = (target - pos)/spd
                count += 1
        return count

        