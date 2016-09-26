class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        result = sorted(count.keys(), key = lambda x:count[x], reverse = True)
        print result
        return result[:k]
        
        
#bucket sort:
    
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        size = len(nums)
        result = []
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 0
        
        bucket = [[] for i in xrange(len(nums))]
        for i in count:
            bucket[count[i]].append(i)
        
        print bucket
        
        for i in xrange(size-1,-1,-1):
            if len(bucket[i]) != 0:
                for j in xrange(len(bucket[i])-1,-1,-1):
                    result.append(bucket[i][j])
                    k -= 1
                    if k == 0:
                        return result
                        
                        
# hash and heap
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        size = len(nums)
        result = []
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        heap = [(0,0) for i in xrange(k)]
        for i in count:
            if count[i] > heap[0][1]:
                heap[0] = (i,count[i])
                self.heapify(heap,0)
                
        return [i[0] for i in heap]
        
    def heapify(self,heap,i):
        heapSize = len(heap)
        leftChild = 2*i+1
        rightChild = 2*i+2
        smallest = i
        if leftChild < heapSize and heap[i][1] > heap[leftChild][1]:
            smallest = leftChild
        if rightChild < heapSize and heap[smallest][1] > heap[rightChild][1]:
            smallest = rightChild
        if smallest != i:
            heap[smallest], heap[i] = heap[i], heap[smallest]
            self.heapify(heap,smallest)