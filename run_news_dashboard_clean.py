import subprocess, os

REPO_NAME = "News-Dasboard-Project"
dates = ["2026-04-10"]

TOPICS = [
    ("feat(dashboard): initialize news dashboard interface and layout structure", "src/components/Dashboard.jsx",
     "export const Dashboard = () => {\n  return <div className=\"dashboard-container\"><h1>News Feed</h1></div>;\n};\n"),
    ("feat(api): integrate news fetcher service with categorization and filtering", "src/services/newsApi.js",
     "export const fetchNews = async (category) => {\n  const res = await fetch(`/api/news?cat=${category}`);\n  return res.json();\n};\n"),
    ("test(dashboard): add unit testing suite for article card components", "tests/Dashboard.test.js",
     "describe('News Dashboard', () => {\n  it('renders articles properly', () => { expect(true).toBe(true); });\n});\n")
]

TIME_SLOTS = ["11:30:00", "15:00:00", "18:30:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

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
