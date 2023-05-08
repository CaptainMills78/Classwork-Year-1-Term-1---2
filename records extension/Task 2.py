def country_scores():
    countries = []
    file = open("goals.txt", "r")

    for line in file:
        found = False
        data = line.split(";")
        country = data[1]
        for x in countries:
            if x[0] == country:
                x[1] += 1
                found = True
        if not found:
            countries.append([country, 1])

    file.close()
    return countries


def player_scores():
    players = []
    file = open("goals.txt", "r")

    for line in file:
        found = False
        data = line.split(";")
        player = data[0]
        for x in players:
            if x[0] == player:
                x[1] += 1
                found = True
        if not found:
            players.append([player, 1])

    file.close()
    return players


def top_country():
    count_scores = country_scores()
    top_score = 0
    top_count = ""
    for x in count_scores:
        if x[1] > top_score:
            top_count = x[0]

    print(f"Top scoring country: {top_count}")


def top_player():
    play_scores = player_scores()
    top_score = 0
    top_play = ""
    for x in play_scores:
        if x[1] > top_score:
            top_play = x[0]

    print(f"Top scoring country: {top_play}")
