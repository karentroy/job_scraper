# db.py

import duckdb
import os

DB_PATH = "data/jobs.duckdb"

os.makedirs("data", exist_ok=True)

def get_conn():
    return duckdb.connect(DB_PATH)


def init_db():
    conn = get_conn()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        title VARCHAR,
        company VARCHAR,
        location VARCHAR,
        description VARCHAR,
        url VARCHAR,
        source VARCHAR,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS snapshots (
        date TIMESTAMP,
        total_jobs INTEGER,
        total_companies INTEGER
    )
    """)

    conn.close()


def insert_jobs(jobs):


    if not jobs:
        print("No jobs to insert — skipping DB write.")
        return
        
    conn = get_conn()

    conn.executemany("""
    INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, [
        (
            j["title"],
            j["company"],
            j["location"],
            j["description"],
            j["url"],
            j["source"]
        )
        for j in jobs
    ])

    conn.close()