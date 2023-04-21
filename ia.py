def ia(board, signe):
    if signe not in ["X", "O"]:
        return False
    possibilites = []
    for i in range(9):
        if board[i] == 0:
            # On simule le coup
            board[i] = 1 if signe == "X" else 2
            # On évalue la situation avec la fonction eval_board
            score = eval_board(board, signe)
            # On stocke l'emplacement et le score
            possibilites.append((i, score))
            # On annule le coup
            board[i] = 0
    if len(possibilites) == 0:
        return False
    # On choisit l'emplacement avec le meilleur score
    choix = max(possibilites, key=lambda x: x[1])[0]
    return choix
