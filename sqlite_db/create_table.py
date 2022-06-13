import sqlite3 
con = sqlite3.connect('baseball_history.db')

cur = con.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS team_franchise (
        franchise_id text NOT NULL PRIMARY KEY,
        franchise_name text,
        active text,
        na_assoc text
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        year integer,
        league_id text,
        team_id text,
        franchise_id text,
        div_id text,
        rank integer,
        FOREIGN KEY(franchise_id) REFERENCES team_franchise(franchise_id)
    )
""")

con.commit()

con.close()