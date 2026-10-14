class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        '''
        UNDIRECTED EDGES
        start at 0 and end at 0
        1 second time for each edge

        apple 2
        visit set()
        deq deque([(2, 0, set())])
        current_node 2
        path_distance 0
        current_node 0
        path_distance 2
        before union {2}
        visit set()
        visit set()
        current_node 3
        path_distance 2
        current_node 6
        path_distance 2
        ans 2
        #########
        apple 4
        visit set()
        deq deque([(4, 0, set())])
        current_node 4
        path_distance 0
        current_node 1
        path_distance 2
        current_node 0
        path_distance 4
        before union {1, 4}
        visit set()
        visit set()
        current_node 5
        path_distance 4
        ans 4
        #########
        apple 5
        visit set()
        deq deque([(5, 0, set())])
        current_node 5
        path_distance 0
        current_node 1
        path_distance 2
        current_node 0
        path_distance 4
        before union {1, 5}
        visit set()
        visit set()
        current_node 4
        path_distance 4
        ans 4
        #########

        '''
        def bfs(starting_node):
          
            res = 0
            deq = deque([(starting_node, 0, set())]) # node, path_distance
            
  
            while deq:
                current_node, path_distance, path_visit = deq.popleft() #1, 2, {5}
                path_visit = path_visit.copy()
           

                if current_node == 0 or current_node in visit :
                    res += path_distance
                  
                    visit.update(path_visit)
                  
                    continue

                path_visit.add(current_node)

                for nei in graph[current_node]:
                    if nei in path_visit:
                        continue

                    deq.append((nei, path_distance + 2, path_visit))

            return res


                

               

                


        final_res = 0
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        apples_list = []

        for node in range(len(hasApple)):
            if hasApple[node] == True:
                apples_list.append(node)


        for apple in apples_list:
            print("apple", apple)
            if apple in visit:
                continue

            ans =  bfs(apple)
            final_res += ans
            print("ans", ans)
            print("#########")


        return final_res

        

        