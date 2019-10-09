class Solution:
    def threeSum(self, arr, target = 0):
        results = []
        #take first number, search for 2 sum that equals its compliment past this one
        arr = sorted(arr)
        for f in range(len(arr)-2):
            if f == 0 or arr[f] > arr[f-1]:
                s = f+1
                t = len(arr)-1
                while s < t:
                    thisSum = arr[f]+arr[s]+arr[t]
                    if thisSum == target:
                        results.append([arr[f],arr[s],arr[t]])
                        curS = s
                        while s < t and arr[s] == arr[curS]:
                            s+=1
                    elif thisSum < target:
                        curS = s                        
                        while s < t and arr[s] == arr[curS]:
                            s+=1
                    else:
                        curT = t
                        while s < t and arr[t] == arr[curT]:
                            t-=1
        return results