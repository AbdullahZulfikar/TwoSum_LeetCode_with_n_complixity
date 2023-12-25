class Solution:
    def __init__(self) -> None:
        self.array = [2, 7, 11, 15]

    def Find(self, number):
        index_dict = {}  # Dictionary to store elements and their indices

        for i, elem in enumerate(self.array):
            complement = number - elem

            # Check if the complement is in the dictionary
            if complement in index_dict:
                return index_dict[complement], i  # Return the indices of the pair

            # Add the current element and its index to the dictionary
            index_dict[elem] = i

        return "Not found"  # Return if no pair is found


s = Solution()
print(s.Find(26))
