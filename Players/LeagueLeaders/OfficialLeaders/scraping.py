import pandas as pd
import requests

pd.set_option('display.max_columns', None)
url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS'
OfficialLeagueLeadersJSON = requests.get(url=url).json()

OfficialLeagueLeadersJSON = OfficialLeagueLeadersJSON['resultSet']['rowSet']