import requests

# ----------------------------
# CONFIG (YOU MUST ADD YOUR KEYS)
# ----------------------------

APP_ID = "378f5884"
APP_KEY = "bcc3db41f638f3bcdaadb85f444438a2"

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"


# ----------------------------
# MAIN SEARCH FUNCTION
# ----------------------------

def jobs_source(role, location):

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": role,
        "where": location,
        "results_per_page": 50,
        "content-type": "application/json"
    }

    try:
        r = requests.get(BASE_URL, params=params, timeout=15)
#        print(f"Status code: {r.status_code}")
#        print(r.text[:500])
        data = r.json()
        results = []

        for item in data.get("results", []):
            # Keep the display_name as the location string
            results.append(type("Job", (), {
                "title": item.get("title"),
                "company": item.get("company", {}).get("display_name"),
                "location": item.get("location", {}).get("display_name", ""),  # string only
                "description": item.get("description"),
                "apply_url": item.get("redirect_url"),
                "source": "adzuna"
            })())

        return results

    except Exception as e:
        print("Error fetching jobs:", e)
        return []