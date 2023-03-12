import heapq
import time
import random
import matplotlib.pyplot as plt

class PriorityQueue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        heapq.heappush(self.items, -item)

    def extract_max(self):
        if not self.items:
            return None
        return -heapq.heappop(self.items)

# Inefficient implementation
def inefficient_insertion_extraction(pq, data):
    for item in data:
        pq.insert(item)
    result = []
    while len(pq.items) > 0:
        result.append(pq.extract_max())
    return result

def inefficient_priority_queue(data):
    pq = PriorityQueue()
    return inefficient_insertion_extraction(pq, data)
############################################

# Efficient implementation
def efficient_insertion_extraction(pq, data):
    for item in data:
        pq.insert(item)
    result = []
    while len(pq.items) > 0:
        result.append(pq.extract_max())
    return result[::-1]

def efficient_priority_queue(data):
    pq = PriorityQueue()
    return efficient_insertion_extraction(pq, data)
############################################

def measure_time(priority_queue):
    start_time = time.time()
    data = [random.randint(1, 1000) for i in range(1000)]
    priority_queue(data)
    end_time = time.time()
    return end_time - start_time

def experiment():
    inefficient_times = []
    efficient_times = []
    for i in range(100):
        inefficient_times.append(measure_time(inefficient_priority_queue))
        efficient_times.append(measure_time(efficient_priority_queue))
    plt.hist(inefficient_times, alpha=0.5, label='Inefficient')
    plt.hist(efficient_times, alpha=0.5, label='Efficient')
    plt.legend(loc='upper right')
    plt.xlabel('Execution time (seconds)')
    plt.ylabel('Frequency')
    plt.show()
    print('Inefficient implementation: average execution time =', sum(inefficient_times) / 100)
    print('Efficient implementation: average execution time =', sum(efficient_times) / 100)

if __name__ == '__main__':
    experiment()
