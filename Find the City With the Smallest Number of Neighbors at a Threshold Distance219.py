class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph_map = {i: [] for i in range(n)}
        for edge in edges:
            graph_map[edge[0]].append((edge[2], edge[1]))
            graph_map[edge[1]].append((edge[2], edge[0]))
            
        ans_city, min_cities = -1, 101
        for city in range(n):
            distance = [float('inf')] * n
            distance[city] = 0
            visited = set()
            heap = []
            heapq.heappush(heap, (0, city))
            while len(heap):
                dist, ct = heapq.heappop(heap)
                visited.add(ct)
                if dist >= distanceThreshold:
                    continue
                for weight, nei in graph_map[ct]:
                    if nei not in visited and weight + dist < distance[nei]:
                        distance[nei] = weight + dist
                        heapq.heappush(heap, (distance[nei], nei))
            cities = -1
            for dist in distance:
                if dist <= distanceThreshold:
                    cities+=1
            if cities <= min_cities:
                ans_city = city
                min_cities = cities
                
        return ans_city
