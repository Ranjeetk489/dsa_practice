#tournament winner
HOME_TEAM_WON = 1

# O(n) time & O(k) space
def tournament_winner(competitions, results):
    currentBestTeam = ""
    scores  = {currentBestTeam:0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)
        if(scores[winningTeam] > scores[currentBestTeam]):
            currentBestTeam = winningTeam
        
    return currentBestTeam

def updateScores(team, points, scores): 
    if(team not in scores):
        scores[team] = 0
    score[team] += points                                                                                                                                                                              


#Non-constructible Change

# O(nlogn) time & O(1) space
def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1



# Find Closest Value in Binary Search tree

# Average O(logn) & worst O(n) time
# Space Complexity O(logn) & worst O(n) time
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, flags("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target- closest) > abs(target - tree.value):
        closest = tree.value
    if target < target.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > target.value:
        return findClosestValueInBst(tree.right, target)
    else:
        return closest

#loop method

# Average O(logn) & worst O(n) time complexity
# Average O(1) & Worst : O(1) space complexity
def findClosestValueInBstLoop(tree, target):
    return findClosestValueInBstHelperLoop(tree, target, float("inf"))

def findClosestValueInBstHelperLoop(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target- closest) > abs(target - tree.value):
            closest = tree.value
        if target < target.value:
           currentNode = currentNode.left
        elif target > target.value:
            currentNode = currentNode.right
        else:
            break
    return closest



#Branch Sums

# O(n) time | O(n) space
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0 , sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, runningSum, sums)
    calculateBranchSums(node.right, runningSum, sums)