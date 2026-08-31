class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output= []
        sort_dict = defaultdict(list)
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str in sort_dict:
                sort_dict[sort_str].append(str)
            else:
                sort_dict[sort_str]=[str]
        for str in sort_dict.values():
            output.append(str)
        return output

            
        