from flask import Flask, render_template, request

app = Flask(__name__)

# Placeholder stats so everything WORKS now.
# Replace values later with real stats when you want.
TEAMS = {
    "Seahawks": {
        "legacy": {
            "name": "Steve Largent",
            "tag": "SEA • WR",
            "photo": "seahawks_largent.png",
            "stats": {"Seasons": 14, "Games": 200, "Yards": 13089, "TDs": 100}
        },
        "modern": {
            "name": "Jaxon Smith-Njigba",
            "tag": "SEA • WR",
            "photo": "seahawks_jsn.png",
            "stats": {"Seasons": 2, "Games": 34, "Yards": 1200, "TDs": 6}
        }
    },
    "49ers": {
        "legacy": {
            "name": "Joe Montana",
            "tag": "SF • QB",
            "photo": "niners_montana.png",
            "stats": {"Seasons": 16, "Games": 192, "Yards": 40551, "TDs": 273}
        },
        "modern": {
            "name": "Brock Purdy",
            "tag": "SF • QB",
            "photo": "niners_purdy.png",
            "stats": {"Seasons": 3, "Games": 40, "Yards": 9000, "TDs": 60}
        }
    },
    "Rams": {
        "legacy": {
            "name": "Kurt Warner",
            "tag": "LAR • QB",
            "photo": "rams_warner.png",
            "stats": {"Seasons": 12, "Games": 124, "Yards": 32344, "TDs": 208}
        },
        "modern": {
            "name": "Matthew Stafford",
            "tag": "LAR • QB",
            "photo": "rams_stafford.png",
            "stats": {"Seasons": 16, "Games": 200, "Yards": 56000, "TDs": 360}
        }
    },
    "Cardinals": {
        "legacy": {
            "name": "Larry Fitzgerald",
            "tag": "ARI • WR",
            "photo": "cardinals_fitzgerald.png",
            "stats": {"Seasons": 17, "Games": 263, "Yards": 17492, "TDs": 121}
        },
        "modern": {
            "name": "Marvin Harrison Jr.",
            "tag": "ARI • WR",
            "photo": "cardinals_mhj.png",
            "stats": {"Seasons": 1, "Games": 17, "Yards": 900, "TDs": 6}
        }
    }
}

STAT_ORDER = ["Seasons", "Games", "Yards", "TDs"]

@app.route("/")
def home():
    return render_template("index.html", teams=list(TEAMS.keys()))

@app.route("/compare", methods=["GET", "POST"])
def compare():
    team = request.form.get("team") or request.args.get("team") or "Seahawks"
    if team not in TEAMS:
        team = "Seahawks"

    legacy = TEAMS[team]["legacy"]
    modern = TEAMS[team]["modern"]

    rows = []
    for stat in STAT_ORDER:
        a = legacy["stats"].get(stat, 0)
        b = modern["stats"].get(stat, 0)
        m = max(a, b, 1)
        rows.append({
            "stat": stat,
            "legacy": a,
            "modern": b,
            "legacy_pct": int(round((a / m) * 100)),
            "modern_pct": int(round((b / m) * 100)),
        })

    return render_template(
        "page1.html",
        teams=list(TEAMS.keys()),
        selected_team=team,
        legacy=legacy,
        modern=modern,
        rows=rows
    )

@app.route("/about")
def about():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)