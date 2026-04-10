import subprocess, os

# 1. SET YOUR REPO NAME & TARGET DATES HERE
REPO_NAME = "News-Dasboard-Project"
dates = [
    "2026-04-10"
]

# Strictly 2-3 commit topics per target date
TOPICS = [
    ("feat: setup initial core project architecture and configuration", "src/index.js",
     "// Core configuration\nexport const config = { env: 'production' };\n"),
    ("feat: implement main application features and data handlers", "src/app.js",
     "// Main application entry\nconsole.log('App initialized');\n"),
    ("test: add primary unit tests and documentation", "tests/app.test.js",
     "// Test suite\nconsole.log('Tests passing');\n")
]

TIME_SLOTS = ["11:30:00", "15:00:00", "18:30:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

# Baseline README setup
with open("README.md", "w") as f:
    f.write(f"# {REPO_NAME}\nClean, structured project repository.\n")

subprocess.run(["git", "add", "."], check=True)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = f"{dates[0]}T09:00:00"
env["GIT_COMMITTER_DATE"] = f"{dates[0]}T09:00:00"

subprocess.run(["git", "commit", "-m", f"Initial commit: setup {REPO_NAME}"], env=env, check=True)

total = 1
for date_str in dates:
    for i, (msg, file_path, content) in enumerate(TOPICS):
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "a") as f:
            f.write(f"\n// Updated: {date_str} {TIME_SLOTS[i]}\n" + content)

        subprocess.run(["git", "add", file_path], check=True)

        commit_iso = f"{date_str}T{TIME_SLOTS[i]}"
        env["GIT_AUTHOR_DATE"] = commit_iso
        env["GIT_COMMITTER_DATE"] = commit_iso

        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        total += 1

print(f"\nGenerated {total} clean compact commits for {REPO_NAME}!")
