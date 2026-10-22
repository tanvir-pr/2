#!/usr/bin/env python3
"""Analyze SSH authentication events and assess policy violations."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

DATA_PATH = Path(__file__).resolve().parent / "auth_events.json"
FIGURE_PATH = Path(__file__).resolve().parent / "auth_analysis.png"


def main() -> None:
    with open(DATA_PATH, encoding="utf-8") as handle:
        report = json.load(handle)

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
        "Observation window: "
        f"{window['start']} to {window['end']} ({window['length_hours']} hours)"
    )
    print(f"Collector version: {collector['version']}")
    print(f"last_review: {last_review!r}")
    if last_review is not None:
        print("WARNING: expected last_review to be None")
    else:
        print("Confirmed: last_review is None (not the JSON text 'null').")
    print()

    failures_by_ip: dict[str, int] = {}
    successes_by_ip: dict[str, int] = {}
    failures_by_user: dict[str, int] = {}
    failures_by_hour: dict[int, int] = {}

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

    all_ips = sorted({event["ip"] for event in events})

    print("Per-address summary (failures / successes / policy assessment):")
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
    print()

    breached_ips = [
        ip
        for ip in all_ips
        if failures_by_ip.get(ip, 0) > max_failures and successes_by_ip.get(ip, 0) > 0
    ]

    if breached_ips:
        for ip in breached_ips:
            first_success = next(
                event
                for event in events
                if event["ip"] == ip and event["result"] == "success"
            )
            failures_before = sum(
                1
                for event in events
                if event["ip"] == ip
                and event["result"] == "fail"
                and event["time"] < first_success["time"]
            )
            print("*** WARNING: SERIOUS BREACH ***")
            print(f"Address: {ip}")
            print(f"Compromised account: {first_success['user']}")
            print(f"Failed attempts before success: {failures_before}")
            print(
                "This is worse than brute force alone because the attacker gained "
                "access and can act on the system, not merely probe credentials."
            )
            print()
    else:
        print("No address both exceeded the failure limit and logged in successfully.")
        print()

    print("Failed attempts against watched accounts:")
    for account in watched_accounts:
        count = failures_by_user.get(account, 0)
        print(f"  {account}: {count}")
    print()

    peak_hour = max(range(24), key=lambda hour: failures_by_hour.get(hour, 0))
    peak_count = failures_by_hour.get(peak_hour, 0)
    print(
        f"Hour with the most failures: {peak_hour:02d}:00 "
        f"({peak_count} failed attempts)"
    )
    print()

    over_limit_ips = {ip for ip in all_ips if failures_by_ip.get(ip, 0) > max_failures}
    attack_detected = bool(over_limit_ips) or sum(failures_by_ip.values()) > max_failures
    attack_succeeded = bool(breached_ips)

    print("Conclusion:")
    print(
        f"  Server attacked: {'YES' if attack_detected else 'NO'} "
        f"({len(over_limit_ips)} address(es) exceeded the per-IP failure limit)."
    )
    print(
        f"  Attack succeeded: {'YES' if attack_succeeded else 'NO'} "
        f"({'at least one breach after excessive failures' if attack_succeeded else 'no successful login after policy breach'})."
    )
    print()

    plot_charts(failures_by_ip, failures_by_hour, max_failures, all_ips)


def plot_charts(
    failures_by_ip: dict[str, int],
    failures_by_hour: dict[int, int],
    max_failures: int,
    all_ips: list[str],
) -> None:
    ips_sorted = sorted(all_ips, key=lambda ip: failures_by_ip.get(ip, 0))
    fail_counts = [failures_by_ip.get(ip, 0) for ip in ips_sorted]
    colors = [
        "crimson" if count > max_failures else "steelblue" for count in fail_counts
    ]

    hours = list(range(24))
    hourly_failures = [failures_by_hour.get(hour, 0) for hour in hours]

    fig, (ax_ip, ax_hour) = plt.subplots(2, 1, figsize=(10, 9))

    ax_ip.barh(ips_sorted, fail_counts, color=colors)
    ax_ip.axvline(
        max_failures,
        color="black",
        linestyle="--",
        linewidth=1.5,
    )
    ax_ip.set_xlabel("Failed login attempts")
    ax_ip.set_ylabel("Source IP address")
    ax_ip.set_title("Failed attempts per source address")
    ax_ip.grid(True, axis="x", alpha=0.3)
    ax_ip.legend(
        handles=[
            Patch(facecolor="steelblue", label="Within policy limit"),
            Patch(facecolor="crimson", label="Over policy limit"),
            Line2D(
                [0],
                [0],
                color="black",
                linestyle="--",
                label=f"Policy limit ({max_failures})",
            ),
        ],
        loc="lower right",
    )

    ax_hour.bar(hours, hourly_failures, color="steelblue", label="Failed attempts")
    ax_hour.set_xlabel("Hour of day (UTC)")
    ax_hour.set_ylabel("Failed login attempts")
    ax_hour.set_title("Failed attempts by hour of day")
    ax_hour.set_xticks(hours)
    ax_hour.grid(True, axis="y", alpha=0.3)
    ax_hour.legend(loc="upper right")

    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
