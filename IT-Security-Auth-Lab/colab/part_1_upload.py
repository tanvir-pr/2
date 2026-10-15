# Colab Cell 1 — paste this whole file into one cell, then run.
# Upload auth_events.json from your course folder.

from google.colab import files

uploaded = files.upload()
DATA_FILE = "auth_events.json"
assert DATA_FILE in uploaded, f"Please upload a file named {DATA_FILE}"
