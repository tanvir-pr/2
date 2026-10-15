# Colab Cell 3 — run after Part 2.

failures_by_ip = {}
successes_by_ip = {}
failures_by_user = {}
failures_by_hour = {}

for event in events:
    ip = event["ip"]
    user = event["user"]
    hour = int(event["time"][11:13])

    if event["result"] == "fail":
        failures_by_ip[ip] = failures_by_ip.get(ip, 0) + 1
        failures_by_user[user] = failures_by_user.get(user, 0) + 1
        failures_by_hour[hour] = failures_by_hour.get(hour, 0) + 1
    elif event["result"] == "success":
        successes_by_ip[ip] = successes_by_ip.get(ip, 0) + 1

all_ips = sorted({e["ip"] for e in events})
