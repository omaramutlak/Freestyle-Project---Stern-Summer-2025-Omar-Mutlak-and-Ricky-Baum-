from data_fetcher import get_team_stats
from utils import predict_score, extract_stat
from visuals import plot_team_comparison

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    score1, score2 = predict_score(stats1, stats2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    plot_team_comparison(team1, team2, stats1, stats2)

    return f"{team1} {score1} - {score2} {team2} → Winner: {winner}"








