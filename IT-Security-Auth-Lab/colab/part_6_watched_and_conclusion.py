# Colab Cell 6 — run after Part 5.

print("Failed attempts against watched accounts:")
for account in watched_accounts:
    print(f"  {account}: {failures_by_user.get(account, 0)}")

peak_hour = max(range(24), key=lambda h: failures_by_hour.get(h, 0))
peak_count = failures_by_hour.get(peak_hour, 0)
print(f"\nHour with most failures: {peak_hour:02d}:00 ({peak_count} failed attempts)")

over_limit_ips = {ip for ip in all_ips if failures_by_ip.get(ip, 0) > max_failures}
attack_detected = len(over_limit_ips) > 0
attack_succeeded = len(breached_ips) > 0

print(f"\nServer attacked? {'YES' if attack_detected else 'NO'}")
print(f"Attack succeeded? {'YES' if attack_succeeded else 'NO'}")
