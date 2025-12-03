from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

players_games = {
    "Jaxon Smith-Njigba": [
        {"week": 1, "opponent": "Rams",     "rec": 3, "yards": 25, "td": 0},
        {"week": 2, "opponent": "Lions",    "rec": 5, "yards": 34, "td": 0},
        {"week": 3, "opponent": "Panthers", "rec": 4, "yards": 48, "td": 1},
        {"week": 4, "opponent": "Giants",   "rec": 6, "yards": 63, "td": 0},
        {"week": 5, "opponent": "49ers",    "rec": 2, "yards": 41, "td": 0},
    ],
    "DK Metcalf": [
        {"week": 1, "opponent": "Rams",     "rec": 5, "yards": 47, "td": 1},
        {"week": 2, "opponent": "Lions",    "rec": 6, "yards": 75, "td": 1},
        {"week": 3, "opponent": "Panthers", "rec": 8, "yards": 112, "td": 1},
        {"week": 4, "opponent": "Giants",   "rec": 4, "yards": 60, "td": 0},
        {"week": 5, "opponent": "49ers",    "rec": 3, "yards": 52, "td": 0},
    ],
    "Tyler Lockett": [
        {"week": 1, "opponent": "Rams",     "rec": 2, "yards": 10, "td": 0},
        {"week": 2, "opponent": "Lions",    "rec": 8, "yards": 59, "td": 2},
        {"week": 3, "opponent": "Panthers", "rec": 5, "yards": 64, "td": 0},
        {"week": 4, "opponent": "Giants",   "rec": 4, "yards": 54, "td": 1},
        {"week": 5, "opponent": "49ers",    "rec": 3, "yards": 33, "td": 0},
    ],
}

def get_summary(game_list):
    if not game_list:
        return {
            "games": 0,
            "total_rec": 0,
            "total_yards": 0,
            "total_td": 0,
            "avg_yards": 0,
        }

    games = len(game_list)
    total_rec = sum(g["rec"] for g in game_list)
    total_yards = sum(g["yards"] for g in game_list)
    total_td = sum(g["td"] for g in game_list)
    avg_yards = round(total_yards / games, 1) if games > 0 else 0

    return {
        "games": games,
        "total_rec": total_rec,
        "total_yards": total_yards,
        "total_td": total_td,
        "avg_yards": avg_yards,
    }


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/page1")
def page1():
    teams = [
        {"name": "Seahawks", "wins": 9, "losses": 8, "ppg": 23.9},
        {"name": "49ers",    "wins": 12, "losses": 5, "ppg": 28.9},
    ]
    return render_template("page1.html", teams=teams)


@main.route("/page2", methods=["GET", "POST"])
def page2():
    player_names = list(players_games.keys())
    selected_player = player_names[0]
    games = players_games[selected_player]
    summary = get_summary(games)

    if request.method == "POST":
        selected_player = request.form.get("player_name", selected_player)
        if selected_player in players_games:
            games = players_games[selected_player]
            summary = get_summary(games)

    return render_template(
        "page2.html",
        player_names=player_names,
        selected_player=selected_player,
        games=games,
        summary=summary,
    )