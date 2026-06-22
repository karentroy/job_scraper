# collector.py
from config import NORTHEAST_STATES, ROLE_QUERIES, KEY_COMPANIES
from jobs_source import jobs_source


def fetch_jobs():
    jobs = []

    for state in NORTHEAST_STATES:  # your list of roles to search
        for q in ROLE_QUERIES:
            results = jobs_source(role=q, location=state)

            for j in results:
                display_name = getattr(j, "location", "")
                full_desc = getattr(j, "description", "")

                text = (getattr(j, "title", "") + " " + full_desc).lower()

                # Skip overly senior jobs
                if any(k in j.title.lower() for k in ["senior", "lead", "manager", "director", "professor",
                                                      "faculty", "principal", "lecturer", "supervisor",
                                                      "adjunct", "tenure", "doctorate", "doctoral", "postdoctoral",
                                                      "president", "cardiologist", "supervisor", "sr.",
                                                      "scientist", "phd"]):
                    continue

                jobs.append({
                    "title": getattr(j, "title", ""),
                    "company": getattr(j, "company", ""),
                    "location": display_name,
                    "state": state,  # guaranteed from the loop
                    "description": full_desc,
                    "url": getattr(j, "apply_url", ""),
                    "source": getattr(j, "source", "")
                })
        for company in KEY_COMPANIES:
            results = jobs_source(
                role=company,
                location=""
            )

            for j in results:
                display_name = getattr(j, "location", "")
                full_desc = getattr(j, "description", "")

                text = (getattr(j, "title", "") + " " + full_desc).lower()
                if any(k in j.title.lower() for k in ["senior", "lead", "manager", "director", "professor",
                                                      "faculty", "principal", "lecturer", "supervisor",
                                                      "adjunct", "tenure", "doctorate", "doctoral", "postdoctoral",
                                                      "president", "cardiologist", "supervisor", "sr.",
                                                      "scientist", "phd"]):
                    continue

                jobs.append({
                    "title": getattr(j, "title", ""),
                    "company": getattr(j, "company", ""),
                    "location": display_name,
                    "state": state,  # guaranteed from the loop
                    "description": full_desc,
                    "url": getattr(j, "apply_url", ""),
                    "source": getattr(j, "source", "")
                })

    return jobs
