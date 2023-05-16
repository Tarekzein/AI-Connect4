def MinMax(depth, board, maximizingPlayer):
    if depth <= 0:
        return 0

    winner = board.Winner
    if winner == 2:
        return depth
    if winner == 1:
        return -depth
    if board.IsFull:
        return 0

    bestValue = -1 if maximizingPlayer else 1
    for i in range(board.Columns):
        if not board.DropCoin(2 if maximizingPlayer else 1, i):
          continue
        
        v = MinMax(depth - 1, board, not maximizingPlayer)
        bestValue = max(bestValue, v) if maximizingPlayer else min(bestValue, v)
        board.RemoveTopCoin(i)
    
    return bestValue
