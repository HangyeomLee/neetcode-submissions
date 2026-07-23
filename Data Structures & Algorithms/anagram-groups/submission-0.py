class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Check the lists
        #len is not right exclude and take a new one 
        #비교값을 만들어서 비교값끼리 비교를 하면 편할듯 하다 그래서 
        groups = {}
        #아 그럼 seen 에다가 비굣값을 넣어주면 되구나 먼말알
        for i, target in enumerate(strs):
            key = tuple(sorted(tuple(target)))
            if key not in groups:
                groups[key] = []
            groups[key].append(target) 
        return list(groups.values())