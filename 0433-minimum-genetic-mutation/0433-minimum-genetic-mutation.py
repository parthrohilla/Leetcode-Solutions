class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        bank = set(bank)
        bank.add(start)
        # Create a Graph from possible mutations - Change each character and add those to adjacency matrix that are in mutation_bank
        for gene in bank:
            for i in range(8):
                temp = list(gene)
                for new_char in "ACGT":
                    temp[i] = new_char
                    mutated_gene = "".join(temp)
                    if mutated_gene != gene and mutated_gene in bank:
                        graph[gene].append(mutated_gene)
        # Generic BFS traversal - Just count minimum edges to reach the "end" string
        Q = deque()
        Q.append((start,0))
        visited = {start}
        while Q:
            current, distance = Q.popleft() 
            for nei in graph[current]:
                if nei == end:
                    return distance + 1
                if nei not in visited:
                    Q.append((nei, distance + 1))
                    visited.add(nei)
        return -1
        