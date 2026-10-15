# Colab Cell 4 — run after Part 3.

print(f"{'IP address':<18} {'Failures':>8} {'Successes':>10}  Assessment")
print("-" * 60)

for ip in all_ips:
    failures = failures_by_ip.get(ip, 0)
    successes = successes_by_ip.get(ip, 0)
    if failures > max_failures:
        assessment = f"OVER limit ({max_failures})"
    elif failures == max_failures:
        assessment = f"AT limit ({max_failures})"
    else:
        assessment = f"within limit ({max_failures})"
    print(f"{ip:<18} {failures:>8} {successes:>10}  {assessment}")
