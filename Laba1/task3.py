import json
import matplotlib.pyplot as plt

with open("results/usd_rates.json", encoding="utf-8") as f:
    data = json.load(f)

dates = []
rates = []

for item in data:
    dates.append(item["exchangedate"])
    rates.append(item["rate"])

plt.plot(dates, rates)
plt.title("Курс USD за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Грн")
plt.grid()

plt.savefig("results/usd_plot.png")
plt.show()
