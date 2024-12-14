from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = "".join(sorted(i))  # Removed space in join
        dfdict[sorted_i].append(i)
    return list(dfdict.values())  # Convert dict_values to list

# Example usage:
anagrams = ["listen", "silent", "enlist", "hello", "olleh"]
print(group_anagrams(anagrams))
