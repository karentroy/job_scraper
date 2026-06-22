# main.py

from collector import fetch_jobs
from filters import is_northeast, is_entry_level, is_relevant
from db import init_db, insert_jobs
import pandas as pd

def run():

    init_db()

    print("Collecting jobs...")

    jobs = fetch_jobs()

    print("Raw jobs:", len(jobs))

    filtered = []

    for j in jobs:

        text = (j.get("title","") + j.get("description",""))

        if not is_entry_level(text):
            continue

        if not is_relevant(text):
            continue

        filtered.append(j)

    print("Filtered jobs:", len(filtered))
    print("\nSample locations:")
    for j in jobs[:5]:
        print(j.get("location"))

    insert_jobs(filtered)

    print("Done.")

    pd.DataFrame(filtered).to_csv("data/latest_jobs.csv", index=False)
    pd.DataFrame(jobs).to_csv("data/latest_jobs_unfiltered.csv", index=False)
    print("Saved CSV: data/latest_jobs.csv")

if __name__ == "__main__":
    run()