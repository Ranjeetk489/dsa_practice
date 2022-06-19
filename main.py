# sum of two number in array as target value

def twoNumberSum1(array, targetSum):
  for ele in array: 
    firstNum = ele
    for ele2 in array:
      if(ele2+ firstNum == targetSum):
        print(firstNum, ele2)
        return [firstNum, ele2]
  return []


def twoNumberSum2(array, targetSum):
  nums= {}
  for e in array:
    potentialNum = targetSum - e
    if(potentialNum in nums):
      return [potentialNum, e]
    else:
      nums[e] = True
  return []


def twoNumberSum3(array, targetSum): 
  left = 0
  right= len(array) - 1
  array.sort()
  while left < right:
    currentSum = array[left] + array[right]
    if(currentSum < targetSum): 
      left+=1
    elif currentSum > targetSum:
      right+=1
    elif currentSum == targetSum:
      return [array[left], array[right]]
  return []

print(twoNumberSum1([1,2,3,4,5,1],7))
print(twoNumberSum2([1,2,3,4,5,1],7))
print(twoNumberSum3([1,2,3,4,5,1],7))