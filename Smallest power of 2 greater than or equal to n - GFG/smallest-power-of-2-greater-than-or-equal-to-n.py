#User function Template for python3

class Solution:
    def nearestPowerOf2(self,n):
        #code here
        if (n & (n-1))==0:
            return n
        
        count = 0
        while n:
            n = n >> 1
            count += 1
        
        return 1<<count
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.nearestPowerOf2(N))
# } Driver Code Ends