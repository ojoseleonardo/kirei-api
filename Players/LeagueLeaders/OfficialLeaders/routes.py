from flask import jsonify, Blueprint
from Players.LeagueLeaders.OfficialLeaders.scraping import retornaJSON
from Players.LeagueLeaders.OfficialLeaders.scraping import retornaJSONRookies
from Players.LeagueLeaders.OfficialLeaders.scraping import stat_categorys
from Players.LeagueLeaders.OfficialLeaders.scraping import season_types
from Players.LeagueLeaders.OfficialLeaders.scraping import seasons

official_leaders_bp = Blueprint('official_leaders', __name__)

# ✎ All Players

@official_leaders_bp.route('/leagueLeaders/players/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>', methods=['GET'])
def search_leagueLeaders(season, season_type, stat_category, per_mode):
    return jsonify(retornaJSON(season, season_type, stat_category, per_mode))

@official_leaders_bp.route('/leagueLeaders/player/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Rank=<int:rank>',  methods=['GET'] )
def search_leagueLeaders_by_rank(season, season_type, stat_category, per_mode, rank):
    matching_players = []
    for leagueLeader in retornaJSON(season, season_type, stat_category, per_mode):
            if leagueLeader[1] == rank:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with rank {}'.format(rank)})
    
@official_leaders_bp.route('/leagueLeaders/player/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Name=<string:name>',  methods=['GET'] )
def search_leagueLeaders_by_name(season, season_type, stat_category, per_mode, name):
    matching_players = []
    for leagueLeader in retornaJSON(season, season_type, stat_category, per_mode):
            if leagueLeader[2] == name:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with name {}'.format(name)})
    
@official_leaders_bp.route('/leagueLeaders/players/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Team=<string:team>',  methods=['GET'] )
def search_leagueLeaders_by_team(season, season_type, stat_category,per_mode, team):
    matching_players = []
    for leagueLeader in retornaJSON(season, season_type, stat_category, per_mode):
            if leagueLeader[4] == team:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with name {}'.format(team)})
    
# ✎ Rookies

@official_leaders_bp.route('/leagueLeaders/rookies/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>', methods=['GET'])
def search_leagueLeaders_rookies(season, season_type, stat_category, per_mode):
    return jsonify(retornaJSONRookies(season, season_type, stat_category, per_mode))

@official_leaders_bp.route('/leagueLeaders/rookie/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Rank=<int:rank>',  methods=['GET'] )
def search_leagueLeaders_rookies_by_rank(season, season_type, stat_category, per_mode, rank):
    matching_players = []
    for leagueLeader in retornaJSONRookies(season, season_type, stat_category, per_mode):
            if leagueLeader[1] == rank:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with rank {}'.format(rank)})
    
@official_leaders_bp.route('/leagueLeaders/rookie/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Name=<string:name>',  methods=['GET'] )
def search_leagueLeaders_rookies_by_name(season, season_type, stat_category, per_mode, name):
    matching_players = []
    for leagueLeader in retornaJSONRookies(season, season_type, stat_category, per_mode):
            if leagueLeader[2] == name:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with name {}'.format(name)})
    
@official_leaders_bp.route('/leagueLeaders/rookies/Season=<string:season>&SeasonType=<string:season_type>&StatCategory=<string:stat_category>&PerMode=<string:per_mode>&Team=<string:team>',  methods=['GET'] )
def search_leagueLeaders_rookies_by_team(season, season_type, stat_category,per_mode, team):
    matching_players = []
    for leagueLeader in retornaJSONRookies(season, season_type, stat_category, per_mode):
            if leagueLeader[4] == team:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with name {}'.format(team)})