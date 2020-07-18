"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()

        # enqueue our starting node
        q.enqueue(starting_vertex)

        # make a set to track if we've been here before
        visited = set()

        # while our queue isn't empty
        while q.size() > 0:
            # dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()

            # if we haven't visited this node yet,
            if current_node not in visited:
                print(current_node)

                # mark as visited
                visited.add(current_node)

                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors,
                # add to queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)

        return None

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()

        # push our starting node
        s.push(starting_vertex)

        # make a set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while s.size() > 0:
            # pop off whatever's at the front of our line, this is our current_node
            current_node = s.pop()

            # if we haven't visited this node yet,
            if current_node not in visited:
                print(current_node)

                # mark as visited
                visited.add(current_node)

                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors, add to stack
                for neighbor in neighbors:
                    s.push(neighbor)
        return None

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # NOTES FROM CLASS

        # (default visited is set())

        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        # implied base case
        # if len(neighbors == 0):
        #     return

        # for each neighbor
        for neighbor in neighbors:
            # if it's visited
            if neighbor not in visited:
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)

        # FIRST ATTEMPT
        # # print starting_vertex
        # print(starting_vertex)

        # # if none have been visited make a set to track if we've been here before
        # if visited is None:
        #     visited = set()

        # # add starting_vertex to visited set
        # visited.add(starting_vertex)

        # # loop to find if children have been visited
        # for neighbor in self.vertices[starting_vertex]:
        #     # if not visited, then call dft_recursive()
        #     if neighbor not in visited:
        #         self.dft_recursive(neighbor, visited)

        # return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # create empty queue
        q = Queue()

        # enqueue a path to starting vertex ID
        path = [starting_vertex]
        q.enqueue(path)

        # make a set to track if we've been here before
        visited = set()

        # while queue is not empty
        while q.size() > 0:

            # dequeue first path
            current_path = q.dequeue()
            # grab last current node from the current path
            current_node = current_path[-1]

            # if that current node has not been visited + check if it's our target
            if current_node is destination_vertex:
                # if so, return it
                return current_path

            # if not in visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

            # loop to add path to its neighbors to back of the queue
                for neighbor in neighbors:
                    # copy the path, so we don't mutate original path for diff nodes
                    path_copy = list(current_path)
                    path_copy.append(neighbor)
                    # add to our queue
                    q.enqueue(path_copy)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create empty queue
        s = Stack()

        # enqueue a path to starting vertex ID
        path = [starting_vertex]
        s.push(path)

        # make a set to track if we've been here before
        visited = set()

        # while queue is not empty
        while s.size() > 0:

            # dequeue first path
            current_path = s.pop()
            # grab last current node from the current path
            current_node = current_path[-1]

            # if that current node has not been visited + check if it's our target
            if current_node is destination_vertex:
                # if so, return it
                return current_path

            # if not in visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

            # loop to add path to its neighbors to back of the queue
                for neighbor in neighbors:
                    # copy the path, so we don't mutate original path for diff nodes
                    path_copy = list(current_path)
                    path_copy.append(neighbor)
                    # add to our queue
                    s.push(path_copy)

        return None

        # # create empty stack
        # s = Stack()

        # # push starting node to stack
        # s.push([starting_vertex])

        # # make a set to track if we've been here before
        # visited = set()

        # # while stack is not empty
        # while s.size() > 0:

        #     # pop first path
        #     path = s.pop()
        #     # grab last vertex from the path
        #     v = path[-1]

        # # if that vertex has not been visited
        # if v not in visited:
        #     # check if it's the target
        #     if v == destination_vertex:
        #         # if so, return it
        #         return path

        #     # mark visited
        #     visited.add(v)

        # # loop to add path to its neighbors to stack
        # for next_vert in self.get_neighbors(v):
        #     # copy the path, append the neighbor
        #     new_path = list(path)
        #     new_path.append(next_vert)
        #     s.push(new_path)

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # mark our node as visited
        visited.add(vertex)

        # check if it's our target node
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)

        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)

        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse with a path for each of the neighbors
                result = self.dfs_recursive(neighbor, destination_vertex,
                                            path + [neighbor], visited)
        # if this recursion returns a path
                if result is not None:
                    # return from here
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
