import random
import datetime
import os
import subprocess
import time
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

# Simulate a lazy day
if random.random() < 0.25:
    print("🛌 Taking the day off. No commits today.")
    sys.exit(0)

# Decide number of commits
commit_weights = (
    [1]*5 +         # Light day (1 commit)
    [2]*4 +         # Medium day (2 commits)
    [3]*3 +         # Heavier (3 commits)
    [4]*2 +         # Even heavier (4)
    [5]*1 + [6]*1   # Ultra workaholic days
)
commit_count = random.choice(commit_weights)
print(f"👨‍💻 Workday: making {commit_count} commits.")

# Ensure activity.log exists
if not os.path.exists("activity.log"):
    with open("activity.log", "w") as f:
        f.write("")

for i in range(commit_count):
    now = datetime.datetime.now()
    filename = "activity.log"

    with open(filename, "a") as f:
        f.write(f"{now}: Random commit #{i+1}\n")

    run_command(["git", "add", filename])
    run_command(["git", "commit", "-m", f"Commit #{i+1} on {now.strftime('%Y-%m-%d %H:%M:%S')}"])

    # Add human-like delay between commits (30s to 3m)
    if i < commit_count - 1:
        delay = random.randint(30, 180)
        print(f"⏱️ Sleeping {delay}s before next commit...")
        time.sleep(delay)
