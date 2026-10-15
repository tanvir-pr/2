# Colab Cell 2 — run after Part 1.

import json

with open(DATA_FILE, encoding="utf-8") as f:
    report = json.load(f)

server = report["server"]
window = report["window"]
collector = report["collector"]
policy = report["policy"]
last_review = report["last_review"]
events = report["events"]
max_failures = policy["max_failures_per_ip"]
watched_accounts = policy["watched_accounts"]

print(f"Server: {server}")
print(
    f"Observation window: {window['start']} to {window['end']} "
    f"({window['length_hours']} hours)"
)
print(f"Collector version: {collector['version']}")
print(f"last_review: {last_review!r}")
assert last_review is None, "last_review must be Python None, not the string 'null'"
print("Confirmed: last_review is None.")
print(f"Events: {len(events)}")
