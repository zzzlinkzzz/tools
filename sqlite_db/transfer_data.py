import sqlite3 
con = sqlite3.connect('The_History_of_Baseball.sqlite')

cur = con.cursor()

team_franchise = []

for row in cur.execute("SELECT * FROM team_franchise;"):
    team_franchise.append(row)

team = []

for row in cur.execute("SELECT * FROM team;"):
    team.append(row)

con.close()

con = sqlite3.connect('baseball_history.db')
cur = con.cursor()

for _,row in enumerate(team_franchise):
    print(_,row)
    cur.execute(f"""
        INSERT INTO team_franchise
        VALUES (
            "{row[0]}",
            "{row[1]}",
            "{row[2]}",
            "{row[3]}"
        )
        ;
    """)

for _,row in enumerate(team):
    print(_,row)
    cur.execute(f"""
        INSERT INTO team (year, league_id, team_id, franchise_id, div_id, rank)
        VALUES (
            {row[0]},
            "{row[1]}",
            "{row[2]}",
            "{row[3]}",
            "{row[4]}",
            {row[5]}
        )
        ;
    """)

con.commit()
con.close()