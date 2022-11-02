class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        bank = set(bank)
        
        bank.add(start)
        for gene in bank:
            for i in range(8):
                temp = list(gene)
                for new_char in "ACGT":
                    temp[i] = new_char
                    mutated_gene = "".join(temp)
                    # print(mutated_gene)
                    if mutated_gene != gene and mutated_gene in bank:
                        graph[gene].append(mutated_gene)
        
        print(graph)
        Q = deque()
        Q.append((start, 0))
        visited = set()
        visited.add(start)
        while Q:
            current, distance = Q.popleft()
                
            for nei in graph[current]:
                if nei == end:
                    return distance + 1
                if nei not in visited:
                    Q.append((nei, distance + 1))
                    visited.add(nei)
        
        return -1
        