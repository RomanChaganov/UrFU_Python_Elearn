import json
import time
import requests
import pandas as pd


def get_page(page, half_day):
    if half_day:
        params = {
            "specialization": 1,
            "found": 1,
            "per_page": 100,
            "page": page,
            "date_from": f"2022-12-12T12:00:00+0300",
            "date_to": f"2022-12-12T23:59:00+0300"
        }
    else:
        params = {
            "specialization": 1,
            "found": 1,
            "per_page": 100,
            "page": page,
            "date_from": f"2022-12-12T00:00:00+0300",
            "date_to": f"2022-12-12T11:59:00+0300"
        }
    try:
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
    except:
        return get_page(page, half_day)
    return data


columns = ["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]
df = pd.DataFrame(columns=columns)

result = []
for half_day in [False, True]:
    page = 0
    while page < 999:
        obj = json.loads(get_page(page, half_day))
        result.append(obj)
        if (obj['pages'] - page) <= 1:
            break
        time.sleep(2)
        page += 1

for page in result:
    for vac in page["items"]:
        if vac["salary"] is None:
            df.loc[len(df)] = [vac["name"], None,
                               None, None,
                               vac["area"]["name"], vac["published_at"]]
        else:
            df.loc[len(df)] = [vac["name"], vac["salary"]["from"],
                               vac["salary"]["to"], vac["salary"]["currency"],
                               vac["area"]["name"], vac["published_at"]]
df.to_csv("hh_vacs.csv", index=False)
