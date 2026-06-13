class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        # Iterate through the rest of the strings
        for string in strs[1:]:
            # Update the prefix by checking for the common prefix with each string
            while not string.startswith(prefix):
                prefix = prefix[:-1] 
                if not prefix:
                    return ""
        return prefix 

        '''
        def extract_list_data(strs):
            return {i + 1: strs[i] for i in range(len(strs))} 

        # Check if any string is empty, return "" immediately if so
        if any(s == "" for s in strs):
            return ""

        data = extract_list_data(strs)

        def extletter(i):
            return [value[i] for value in data.values() if value and len(value) > i] 

        ''' 

