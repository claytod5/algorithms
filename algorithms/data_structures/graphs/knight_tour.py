from graph import Graph


def knight_graph(bdSize):
    """
    Create the knight's tour graph.

    Args:
        bdSize (int): Represents the roots of a perfect square for the size of the
        board. For example, 8 for an 8x8 board.

    Returns:
        ktGraph: A Graph object representing the knight's possible moves.
    """
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = pos_to_node_id(row, col, bdSize)
            newPositions = gen_legal_moves(row, col, bdSize)
            for e in newPositions:
                nid = pos_to_node_id(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def pos_to_node_id(row, column, board_size):
    return (row * board_size) + column


def gen_legal_moves(x, y, bdSize):
    newMoves = []
    moveOffsets = [
        (-1, -2),
        (-1, 2),
        (-2, -1),
        (-2, 1),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legal_coord(newX, bdSize) and legal_coord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legal_coord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knight_tour(n, path, u, limit):
    """
    Conduct a knight's tour using DFS.

    Args:
        n: current depth of the search tree.
        path: a list of vertices visited up to this point.
        u: the vertex we wish to explore.
        limit: the number of nodes in the path.

    Returns:
        done (bool)
    """
    visited = set(u)
    path.append(u)
    if n < limit:
        nbrList = list(u.get_connections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i] in visited:
                done = knight_tour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            visited.remove(u)
    else:
        done = True
    return done
