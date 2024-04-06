def asociar_estadisticas(list_names, goals, goals_avoided, assists):
    """ creo players que es una lista que va a contener la
    informacion de todos los jugadores y cada jugador 
    va a estar en un diccionario con sus estadisticas"""
    players = []
    for i in range(len(list_names)):
        player = {
            "name" : list_names[i],
            "goals" : goals[i],
            "goals_avoided" : goals_avoided[i],
            "assists" : assists[i]}
        players.append(player)
    return players

def goleador_maximo(players):
    """recorro toda la lista de los jugadores 
    comparando con max_goals y si es maximo 
    remplazo su nombre y el max_goals"""
    name = ""
    max_goals = -1
    for player in players:
        if player["goals"] > max_goals:
            name = player["name"]
            max_goals = player["goals"]
    return name, max_goals

def jugador_influyente(players):
    """sumo los puntos totales de cada jugador
    y si es maximo remplazo y guardo el nombre
    para luego retornarlo"""
    max_points = -1
    name_max = ""
    for player in players:
        total_points = player["goals"] * 1.5 + player["goals_avoided"] * 1.25 + player["assists"]
        if total_points > max_points:
            max_points = total_points
            name_max = player["name"]
    return name_max

def promedio_goles_equipo(goals_team):
    """retorno el promedio de goles sumando 
    todos los goles del equipo y dividiendolo 
    por la cantidad de partidos que son 25"""
    goals = sum(goals_team)
    matches = 25
    return goals / matches

def promedio_goles_goleador(max_goals):
    """ya tengo la cantidad de goles del jugador
    que hizo mas goles entonces paso la cantidad
    de goles que hizo por parametro y luego saco
    el promedio"""
    matches = 25
    return max_goals / matches
