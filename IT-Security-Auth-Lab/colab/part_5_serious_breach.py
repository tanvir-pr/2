# Colab Cell 5 — run after Part 4.

breached_ips = [
    ip
    for ip in all_ips
    if failures_by_ip.get(ip, 0) > max_failures and successes_by_ip.get(ip, 0) > 0
]

for ip in breached_ips:
    first_success = next(
        e for e in events if e["ip"] == ip and e["result"] == "success"
    )
    failures_before = sum(
        1
        for e in events
        if e["ip"] == ip
        and e["result"] == "fail"
        and e["time"] < first_success["time"]
    )
    print("*** WARNING: SERIOUS BREACH ***")
    print(f"Address: {ip}")
    print(f"Account reached: {first_success['user']}")
    print(f"Failures before success: {failures_before}")
    print(
        "Worse than many failures with no login: the attacker got in "
        "and can use the compromised account."
    )

if not breached_ips:
    print("No address both exceeded the failure limit and logged in successfully.")
