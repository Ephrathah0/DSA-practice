class StockPrice:

    def __init__(self):
        self.data = {}
        self.currTime = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.currTime:
            self.currTime = timestamp
        
        self.data[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.data[self.currTime]

    def maximum(self) -> int:
        while -1 * self.maxHeap[0][0] != self.data[self.maxHeap[0][1]]:
            _, timestamp = heapq.heappop(self.maxHeap)
        return -1 * self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap[0][0] != self.data[self.minHeap[0][1]]:
            _, timestamp = heapq.heappop(self.minHeap)
        return self.minHeap[0][0]