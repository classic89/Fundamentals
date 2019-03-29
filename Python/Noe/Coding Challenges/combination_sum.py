candidates = [2,3,6,7]
target = 7

def combinations(candidates, target):
    combinations = []
    combination = []
    buildCombinations(candidates, target, 0, 0, combination, combinations)
    return combinations

def buildCombinations(candidates, target, index, sum, combination, combinations):
    if sum == target:
        combinations.append(combination)
    elif sum < target:
        for i, c in enumerate(candidates):
            if i >= index:
                print(combination+[c])
                buildCombinations(candidates, target, i, sum+c, combination+[c], combinations)

print(combinations(candidates, target))