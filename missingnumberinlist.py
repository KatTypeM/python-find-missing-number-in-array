# Python algorithm

# Find a missing number in a list/array

        
myArray = [
  1,  2,  3,   4,  5,  6,  7,  8,  9, 10, 11, 12,
  13, 14, 15,  16, 17, 18, 19, 20, 21, 22, 23, 24,
  25, 26, 27,  28, 29, 30, 31, 32, 33, 34, 35, 36,
  37, 38, 39,  40, 41, 43, 44, 45, 46, 47, 48,
  49, 50, 51,  52, 53, 54, 55, 56, 57, 58, 59, 60,
  61, 62, 63,  64, 65, 66, 67, 68, 69, 70, 71, 72,
  73, 74, 75,  76, 77, 78, 79, 80, 81, 82, 83, 84,
  85, 86, 87,  88, 89, 90, 91, 92, 93, 94, 95, 96,
  97, 98, 99, 100
] # 42
myArray1 = [
  1,  2,  3,   4,  5,  6,  7,  8,  9, 10, 11, 12,
  13, 14, 15,  16, 17, 18, 19, 20, 21, 22, 23, 24,
  25, 26, 27,  28, 29, 30, 31, 32, 33, 34, 35, 36,
  37, 38, 39,  40, 41, 42, 43, 44, 45, 46, 47, 48,
  49, 50, 51,  52, 53, 54, 55, 56, 57, 58, 59, 60,
  61, 62, 63,  64, 65, 66, 67, 69, 70, 71, 72,
  73, 74, 75,  76, 77, 78, 79, 80, 81, 82, 83, 84,
  85, 86, 87,  88, 89, 90, 91, 92, 93, 94, 95, 96,
  97, 98, 99, 100
] # 68
myArray2 = [
  61, 62, 63,  64, 65, 66, 67, 68, 69, 70, 71, 72,
  49, 50, 51,  52, 53, 54, 55, 56, 57, 58, 59, 60,
  73, 74, 75,  76, 77, 78, 79, 80, 81, 82, 83, 84,
  1,  2,  3,   4,  5,  6,  7,  8,  9, 10, 11, 12,
  13, 14, 15,  16, 17, 18, 19, 20, 21, 22, 23, 24,
  86, 87,  88, 89, 90, 91, 92, 93, 94, 95, 96,
  97, 98, 99, 100,
  37, 38, 39,  40, 41, 42, 43, 44, 45, 46, 47, 48,
  25, 26, 27,  28, 29, 30, 31, 32, 33, 34, 35, 36
] # 85


# this method compares the sum of each array 
def methodOne(numArray):
    numArray.sort()
    a = 0
    b = 0
    c = 0
    for i in range(1, len(numArray) + 2):
        a += i
    for j in numArray:
        b += j
    c = a - b
    return c

print("This Method compares the sum of each array")
print("Missing number in the array is:",methodOne(myArray))
print("Missing number in the array is:",methodOne(myArray1))
print("Missing number in the array is:",methodOne(myArray2))    


# this method compares if the next number in the array is +1 from the number in the array
def methodTwo(numArray):
    numArray.sort()
    a = 0
    b = 0
    for i in range(0, len(numArray) + 1):
        if(numArray[i + 1] <= len(numArray)):
            a = numArray[i + 1]
        b = numArray[i] + 1
        
        if(a == b):
            continue
        else:
            return b

print("This method checks if each number is sequential")
print("Missing number in the array is:",methodTwo(myArray))
print("Missing number in the array is:",methodTwo(myArray1))
print("Missing number in the array is:",methodTwo(myArray2))