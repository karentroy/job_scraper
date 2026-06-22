# job_scraper
python code that scrapes biomedical engineering jobs

├── config.py
├── db.py
├── collector.py
├── filters.py
├── queries.py
├── jobs_source.py
├── main.py
│
├── data/
│   └── jobs.duckdb

to run, run main.py, which will output a .csv file called latest_jobs.csv

you may need to get your own API key for jobs_source.py.  You can request one for free from adzuna, which is a job consolidator
jobs keywords are located in filters.py
other filtering info located in config.py.

The current version is set to grab all jobs with certain keywords in northeast states, PLUS all jobs from a 
certain list of companies that hire BME students with some frequency, regardless of keywords and location.
