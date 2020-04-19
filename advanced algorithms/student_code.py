from queue import PriorityQueue


def get_distance(A, B):
    return (((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2)

def shortest_path(M,start,goal):
    queue = PriorityQueue()
    queue.put(start, 0)
    g_score = {start: 0}
    came_from = {start: None}
    
    while not queue.empty():
        curr = queue.get()
        if curr == goal:
            get_path(came_from, start, goal)
        for n in M.roads[curr]:
            curr_n_dist = get_distance(M.intersections[curr], M.intersections[n])
            temp_score = g_score[curr] + curr_n_dist
            if n not in g_score or temp_score < g_score[n]:
                g_score[n] = temp_score
                f_score = temp_score + curr_n_dist
                queue.put(n, f_score)
                came_from[n] = curr
    res = get_path(came_from, start, goal)
    return res

def get_path(came_from,start,goal):
    curr = goal
    res = [curr]
    while curr != start:
        curr = came_from[curr]
        res.append(curr)
    res.reverse()
    return res