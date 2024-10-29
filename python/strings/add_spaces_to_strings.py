# First attempt, Solution works but timed out for 3 test cases.

class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        char_list = [char for char in s]
        add_spaces_count = 0
        for space in spaces:
            char_list.insert(space + add_spaces_count, ' ')
            add_spaces_count += 1
        res = "".join(char_list)
        return res

def add_spaces(s: str, spaces: list[int]) -> str:
    result = []
    last_index = 0
    for space in spaces:
        result.append(s[last_index:space])
        result.append(" ")
        last_index = space

    result.append(s[last_index:])
    return "".join(result)

res = Solution()

res.addSpaces("LeetcodeHelpsMeLearn",[8,13,15])

