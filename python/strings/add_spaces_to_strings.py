class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        char_list = [char for char in s]
        add_spaces_count = 0
        for space in spaces:
            char_list.insert(space + add_spaces_count, ' ')
            add_spaces_count += 1
        res = "".join(char_list)
        return res


res = Solution()

res.addSpaces("LeetcodeHelpsMeLearn",[8,13,15])

