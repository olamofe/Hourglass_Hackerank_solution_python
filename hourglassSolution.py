
##Hourglass challenge. maxisum sum if values in an hourglass
def hourglassSum(arr):
    sumlist = []
    for x in range(len(arr)-3+1):
        for y in range(len(arr)-3+1):
            sum = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
            sumlist.append(sum)
    print(sumlist)
    maxi = max(sumlist)
    return maxi





    