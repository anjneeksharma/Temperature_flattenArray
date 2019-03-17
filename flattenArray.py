def flattenArray(inputArray):
    flatList = []
    # Loop over every element one by one
    for item in inputArray:
        # If item is nested array, join it with output flatList
        # else just add  element to the flatarray

        flatList += item if type(item) is list else [item]
    return flatList


jumbledArray = [1, 2, 3, [4, 5], 6, 11, [7, 8], 9, [11, 12], 15, [16, 17]]
flatarray = flattenArray(jumbledArray)
print(flatarray)
