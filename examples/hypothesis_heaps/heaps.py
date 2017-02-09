# Heaps example courtesy of David R. MacIver's nice writeup of Hypothesis stateful testing
# http://hypothesis.works/articles/rule-based-stateful-testing/

def heapnew():
    return []


def heapempty(heap):
    return not heap


def heappush(heap, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break

def heappop(heap):
    if len(heap) == 0:
        raise ValueError("Empty heap")
    if len(heap) == 1:
        return heap.pop()
    result = heap[0]
    heap[0] = heap.pop()
    index = 0
    while index * 2 + 1 < len(heap):
        children = [index * 2 + 1, index * 2 + 2]
        children = [i for i in children if i < len(heap)]
        assert children
        children.sort(key=lambda x: heap[x])
        for c in children:
            if heap[index] > heap[c]:
                heap[index], heap[c] = heap[c], heap[index]
                index = c
                break
        else:
            break
    return result

'''
# "boring" correct version
def heapmerge(x, y):
    result = list(x)
    for v in y:
        heappush(result, v)
    return result
'''

# surprisingly subtle bug, given the algorithm is basically nonsense
def heapmerge(x, y):
    result = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    result.extend(x[i:])
    result.extend(y[j:])
    return result

