import time


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)


def get_vals(start, end):
    res = set()
    current = start
    while current != end:
        res.add(current.val)
        current = current.next

    res.add(current.val)
    return res


def main():
    labels = '186524973'
#    labels = '389125467'
    data = [int(x) for x in labels]
   
    max_val = max(data) 
    data.extend(range(max_val + 1, 10 ** 6 + 1))
    max_val = 10 ** 6
    nodes = [Node(x) for x in data]
    
    for i in range(len(data)):
        nodes[i].next = nodes[(i + 1) % len(data)]
        nodes[i].prev = nodes[(i - 1) % len(data)]

    cache = {node.val: node for node in nodes}
    current_node = nodes[0]

    for i in range(10 ** 7):
        end_node = current_node.next.next.next.next
        
        picked_start = current_node.next
        picked_end = current_node.next.next.next
        
        current_node.next = end_node
        end_node.prev = current_node 

        picked_vals = get_vals(picked_start, picked_end)
        to_find = current_node.val - 1 if current_node.val > 1 else max_val
        while to_find in picked_vals: 
            to_find = to_find - 1 if to_find > 1 else max_val
       
        dest_node = cache[to_find]
        next_node = dest_node.next

        dest_node.next = picked_start
        picked_start.prev = dest_node
        next_node.prev = picked_end
        picked_end.next = next_node    

        current_node = current_node.next

    node = cache[1]
    print(node.next.val * node.next.next.val) 


if __name__ == '__main__':
    main()
