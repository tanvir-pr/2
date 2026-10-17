# Upload this lab to GitHub (part by part)

Repo used in class: **https://github.com/tanvir-pr/2**

You can upload **one part per commit** so your history matches the assignment.

---

## Part 1 — Create the folder on your PC (or Colab)

Make a folder, e.g. `auth-lab`, with only:

- `auth_events.json` (from your teacher — do not rename)

---

## Part 2 — First file: data (optional commit)

Some teachers want **only code** on GitHub. If they allow the JSON:

```bash
cd auth-lab
git init
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git add auth_events.json
git commit -m "Part 1: add auth_events.json"
git push -u origin main
```

**GitHub website instead:** Repo → **Add file** → **Upload files** → drag `auth_events.json` → commit message `Part 1: add auth_events.json`.

---

## Part 3 — Python script

Add `analyze_auth_events.py` (or paste from Colab Part 2–6 into one `.py` file).

```bash
git add analyze_auth_events.py
git commit -m "Part 2: load JSON, dictionaries, policy table, breach warning"
git push
```

---

## Part 4 — Colab notebook (if you used Colab)

```bash
git add auth_events_colab.ipynb
git commit -m "Part 3: Colab notebook (step-by-step cells)"
git push
```

---

## Part 5 — Dependencies

```bash
git add requirements.txt
git commit -m "Part 4: matplotlib dependency"
git push
```

`requirements.txt` content:

```
matplotlib>=3.8
```

---

## Part 6 — Chart output (if teacher wants the figure)

```bash
git add auth_analysis.png
git commit -m "Part 5: saved analysis figure"
git push
```

---

## Part 7 — Short README (recommended)

Create `README.md` in the same folder:

```markdown
# SSH auth log analysis

Run: `pip install -r requirements.txt` then `python analyze_auth_events.py`

Or open `auth_events_colab.ipynb` in Google Colab and upload `auth_events.json`.
```

```bash
git add README.md
git commit -m "Part 6: README with run instructions"
git push
```

---

## Already on this repo (branch)

All files are on branch **`cursor/auth-events-analysis-0341`** (PR #3).

To copy without re-uploading part by part:

```bash
git clone https://github.com/tanvir-pr/2.git
cd 2
git checkout cursor/auth-events-analysis-0341
```

---

## Colab → GitHub in one shot

1. Colab: **File → Save a copy in GitHub**
2. Pick repo and path, e.g. `IT-Security-Auth-Lab/auth_events_colab.ipynb`
3. Repeat for `.py` / `.json` if needed (or merge cells into one `.py` first)

You need a **GitHub personal access token** if Colab asks for password.
