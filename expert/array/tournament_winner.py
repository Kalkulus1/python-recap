def tournamentWinner(competitions, results):
    if len(competitions) != len(results):
        return False

    winners = {}
    
    for idx, result in enumerate(results):
        if result == 0:
            winner = competitions[idx][1]
            if winner in winners:
                winners[winner] += 3
            else:
                winners[winner] = 3
        else:
            winner = competitions[idx][0]
            if winner in winners:
                winners[winner] += 3
            else:
                winners[winner] = 3
        
    return max(winners, key=winners.get)

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]
print(tournamentWinner(competitions, results))