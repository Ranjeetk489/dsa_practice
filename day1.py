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


#validate Subsequence

def validateSequence1(array, sequence):
  arrIndex = 0
  seqIndex = 0
  while arrIndex < len(array) and seqIndex < len(sequence):
    if(sequence[seqIndex] == array[arrIndex]):
      seqIndex+=1
    arrIndex+=1
  return seqIndex == len(sequence)


def validateSequence2(array, sequence):
  seqIndex = 0
  for item in array:
    if(seqIndex == len(sequence)):
      break
    elif sequence[seqIndex] == item:
      seqIndex+= 1
  return seqIndex == len(sequence)

print(validateSequence1([1,2,3,4,5,6,8], [2,4,6]))
print(validateSequence2([1,3,4,5,234], [3,8,5]))

#Sorted Square Array

def squareArray1(array):
  tempArr = []
  for ele in array:
    tempArr.append(ele*ele)
  tempArr.sort()
  print(tempArr)
  

def squareArray2(array):
  tempArr = [0 for _ in array]
  smallerValueIdx = 0
  largerValueIdx = len(array) - 1

  for idx in reversed(range(len(array))):
    smallerValue = array[smallerValueIdx]
    largerValue = array[largerValueIdx]
    print(smallerValue)
    print(largerValue)
    
    if abs(smallerValue) > abs(largerValue):
      tempArr[idx] = smallerValue * smallerValue
      smallerValueIdx += 1
    else:
      tempArr[idx] = largerValue * largerValue
      largerValueIdx -= 1
  return tempArr
    

squareArray1([1,2,3,4,7,5])
print(squareArray2([-3,-2,-1,2,4,6,-7]))