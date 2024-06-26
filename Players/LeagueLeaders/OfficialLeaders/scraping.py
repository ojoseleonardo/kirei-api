import pandas as pd
import requests

season_types = ['Regular Season', 'Playoffs', 'All Star']
stat_categorys = ["MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "EFF", "AST/TOV", "STL/TOV"] 
seasons = ["2023-24", "2022-23", "2021-22", "2020-21", "2019-20", "2018-19", "2017-18", "2016-17", "2015-16", "2014-15", 
           "2013-14", "2012-13", "2011-12", "2010-11", "2009-10", "2008-09", "2007-08", "2006-07", "2005-06", "2004-05", 
           "2003-04", "2002-03", "2001-02", "2000-01", "1999-00", "1998-99", "1997-98", "1996-97", "1995-96", "1994-95", 
           "1993-94", "1992-93", "1991-92", "1990-91", "1989-90", "1988-89", "1987-88", "1986-87", "1985-86", "1984-85", 
           "1983-84", "1982-83", "1981-82", "1980-81", "1979-80", "1978-79", "1977-78", "1976-77", "1975-76", "1974-75", 
           "1973-74", "1972-73", "1971-72", "1970-71", "1969-70", "1968-69", "1967-68", "1966-67", "1965-66", "1964-65", 
           "1963-64", "1962-63", "1961-62", "1960-61", "1959-60", "1958-59", "1957-58", "1956-57", "1955-56", "1954-55", 
           "1953-54", "1952-53", "1951-52", "1950-51", "1949-50", "1948-49", "1947-48", "1946-47"]

def retornaJSON(season, season_type, stat_category, per_mode):
    pd.set_option('display.max_columns', None)
    url = f'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode={per_mode}&Scope=S&Season={season}&SeasonType={season_type}&StatCategory={stat_category}'
    OfficialLeagueLeadersJSON = requests.get(url=url).json()

    OfficialLeagueLeadersJSON = OfficialLeagueLeadersJSON['resultSet']['rowSet']
    
    return OfficialLeagueLeadersJSON

def retornaJSONRookies(season, season_type, stat_category, per_mode):
    pd.set_option('display.max_columns', None)
    url = f'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode={per_mode}&Scope=Rookies&Season={season}&SeasonType={season_type}&StatCategory={stat_category}'
    OfficialLeagueLeadersJSON = requests.get(url=url).json()

    OfficialLeagueLeadersJSON = OfficialLeagueLeadersJSON['resultSet']['rowSet']
    
    return OfficialLeagueLeadersJSON