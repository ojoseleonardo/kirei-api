from flask import jsonify, Blueprint
from Players.LeagueLeaders.OfficialLeaders.scraping import OfficialLeagueLeadersJSON

official_leaders_bp = Blueprint('official_leaders', __name__)

@official_leaders_bp.route('/leagueLeaders', methods=['GET'])
def search_leagueLeaders():
    return jsonify(OfficialLeagueLeadersJSON)

@official_leaders_bp.route('/leagueLeaders/player/rank=<int:rank>',  methods=['GET'] )
def search_leagueLeaders_by_rank(rank):
    matching_players = []
    for leagueLeader in OfficialLeagueLeadersJSON:
            if leagueLeader[1] == rank:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with rank {}'.format(rank)})
    
@official_leaders_bp.route('/leagueLeaders/player/name=<string:name>',  methods=['GET'] )
def search_leagueLeaders_by_name(name):
    matching_players = []
    for leagueLeader in OfficialLeagueLeadersJSON:
            if leagueLeader[2] == name:
                matching_players.append(leagueLeader)
                          
    if matching_players:
        return jsonify(matching_players)
    else:
        return jsonify({'message': 'No player found with name {}'.format(name)})