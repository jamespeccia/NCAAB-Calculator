import pandas as pd

def calculate(away_team, home_team):

    df = pd.read_csv('kenpom_rankings.csv')
    df.set_index("Team" , inplace = True)
    pyth_exponent = 11.5
    hcao = 1.007
    hcad = 0.993

    #variables
    away_adjo = df.loc[away_team, 'AdjO'] * hcad
    away_adjd = df.loc[away_team, 'AdjD'] * hcao
    away_adjt = df.loc[away_team, 'AdjT']
    home_adjo = df.loc[home_team, 'AdjO'] * hcao
    home_adjd = df.loc[home_team, 'AdjD'] * hcad
    home_adjt = df.loc[home_team, 'AdjT']

    #constants
    average_tempo = df["AdjT"].mean()
    average_points = df["AdjO"].mean()

    #calculations
    away_win_percentage_season = (away_adjo ** pyth_exponent) / ((away_adjo ** pyth_exponent) + (away_adjd ** pyth_exponent))
    home_win_percentage_season = (home_adjo ** pyth_exponent) / ((home_adjo ** pyth_exponent) + (home_adjd ** pyth_exponent))

    away_win_percentage_game = ((away_win_percentage_season - (away_win_percentage_season * home_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))
    home_win_percentage_game = ((home_win_percentage_season - (home_win_percentage_season * away_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))

    away_tempo_plus = away_adjt / average_tempo
    home_tempo_plus = home_adjt / average_tempo

    expected_tempo = away_tempo_plus * home_tempo_plus * average_tempo

    away_adjo_plus = away_adjo / average_points
    home_adjo_plus = home_adjo / average_points

    away_adjd_plus = away_adjd / average_points
    home_adjd_plus = home_adjd / average_points

    away_adj_score = away_adjo_plus * home_adjd_plus * average_points
    home_adj_score = home_adjo_plus * away_adjd_plus * average_points

    away_predicted_score = away_adj_score * (expected_tempo / 100)
    home_predicted_score = home_adj_score * (expected_tempo / 100)

    total_score = home_predicted_score + away_predicted_score
    home_spread = away_predicted_score - home_predicted_score

    return round(away_predicted_score,2), round(home_predicted_score,2), round(away_win_percentage_game*100,2), round(home_win_percentage_game*100,2), round(total_score,2), round(home_spread,2)