class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = {}
        include = []
        exclude = []
        for i in arr1:
            if i not in arr2:
                exclude += [i]
            else:
                if i not in arr1_dict:
                    arr1_dict[i] = 1
                else:
                    arr1_dict[i] += 1
        exclude.sort()
        for pos in arr2:
            include += [pos] * arr1_dict[pos]

        return include + exclude
