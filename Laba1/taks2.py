import json
from datetime import datetime, timedelta
from pathlib import Path

import requests


today = datetime.today()
week_ago = today - timedelta(days=7)

start = week_ago.strftime("%Y%m%d")
end = today.strftime("%Y%m%d")

url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
params = {
    "start": start,
    "end": end,
    "valcode": "usd",
    "sort": "exchangedate",
    "order": "asc",
    "json": "",
}

print("→ Отримання курсу USD за останній тиждень...")
response = requests.get(url, params=params)

if response.ok:
    data = response.json()

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    file_path = results_dir / "usd_rates.json"
    file_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    for item in data:
        print(f"{item['exchangedate']}: {item['rate']} грн")
else:
    print("Помилка запиту:", response.status_code)
