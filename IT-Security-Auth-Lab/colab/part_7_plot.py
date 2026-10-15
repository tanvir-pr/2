# Colab Cell 7 — run after Part 6. Saves figure then shows it.

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

ips_sorted = sorted(all_ips, key=lambda ip: failures_by_ip.get(ip, 0))
fail_counts = [failures_by_ip.get(ip, 0) for ip in ips_sorted]
colors = [
    "crimson" if count > max_failures else "steelblue" for count in fail_counts
]
hours = list(range(24))
hourly_failures = [failures_by_hour.get(h, 0) for h in hours]

fig, (ax_ip, ax_hour) = plt.subplots(2, 1, figsize=(10, 9))

ax_ip.barh(ips_sorted, fail_counts, color=colors)
ax_ip.axvline(max_failures, color="black", linestyle="--", linewidth=1.5)
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
ax_hour.set_xlabel("Hour of day")
ax_hour.set_ylabel("Failed login attempts")
ax_hour.set_title("Failed attempts by hour of day")
ax_hour.set_xticks(hours)
ax_hour.grid(True, axis="y", alpha=0.3)
ax_hour.legend(loc="upper right")

fig.tight_layout()
fig.savefig("auth_analysis.png", dpi=120)
plt.show()
