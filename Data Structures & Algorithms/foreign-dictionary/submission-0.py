class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ch = set()
        for word in words:
            for c in word:
                ch.add(c)
        
        k = len(ch)
        graph = [[] for _ in range(26)]
        n = len(words)
        indegree = [0] * 26
        
        for i in range(n-1):
            a = words[i]
            b = words[i+1]

            l = min(len(a),len(b))

            if len(a) > len(b) and a[:l] == b[:l]:
                return ""

            for j in range(l):
                if a[j] != b[j]:
                    u = ord(a[j]) - ord("a")
                    v = ord(b[j]) - ord("a")
                    graph[u].append(v)
                    indegree[v] += 1
                    break
       
        q = deque()

        for c in ch:
            i = ord(c) - ord('a')
            if indegree[i] == 0:
                q.append(i)

        ans = ""
        while q:
            node = q.popleft()
            ans += chr(node + ord('a'))

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(ans) != k:
            return  ""
        
        return ans

        