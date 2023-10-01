from typing import List

# my first solution


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_counts: List = []
        for s in strs:
            letters: dict = {}
            for chr in s:
                if chr not in letters:
                    letters[chr] = 0
                letters[chr] += 1
            letter_counts.append(letters)

        letter_counts = list(zip(letter_counts, strs))
        anangrams: List = []
        passed: List = []
        for i in range(len(letter_counts)):
            if letter_counts[i][0] in passed:
                continue
            passed.append(letter_counts[i][0])
            tmp: List = [letter_counts[i][1]]
            for j in range(i, len(letter_counts)):
                if i == j:
                    continue
                if letter_counts[i][0] == letter_counts[j][0]:
                    tmp.append(letter_counts[j][1])
                    passed.append(j)
            anangrams.append(tmp)

        return anangrams


# if we sort the word, if it's an anagram is exactly the same


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output: dict = {}
        for w in strs:
            curr: str = ''.join(sorted(w))
            print(curr)
            if curr not in output:
                output[curr] = [w]
            else:
                output[curr] += [w]
        return [v for v in output.values()]


print(Solution().groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
