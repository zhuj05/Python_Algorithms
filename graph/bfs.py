from collections import deque

def bfs(graph, start):
    # 初始化已訪問集合 (Visited Set)，避免重複遍歷節點導致無窮迴圈
    visited = {start}
    
    # 初始化雙端佇列 (Deque)，並將起點放入佇列中作為 BFS 的起始點
    queue = deque([start])

    # 當佇列中還有節點時，繼續搜尋
    while queue:
        # 從佇列左側取出最早進入的節點 (Popleft)，實現 FIFO (First-In-First-Out)
        node = queue.popleft()
        
        # 輸出目前的節點
        print(node, end=" ")
        
        # 遍歷目前節點的所有鄰居 (Neighbors)
        for neighbor in graph[node]:
            # 如果該鄰居節點尚未被訪問過
            if neighbor not in visited:
                # 將其標記為已訪問 (Visited)
                visited.add(neighbor)
                # 將其加入佇列末端 (Append)，排隊等待下一層搜尋
                queue.append(neighbor)

# 定義鄰接表 (Adjacency List)，表示圖的結構
graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

# 從節點 'A' 開始執行廣度優先搜尋
bfs(graph, 'A')
# 預期輸出: A B C D E F