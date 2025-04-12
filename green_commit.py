import random
import datetime
import os
import subprocess
import time
import sys
from datetime import timedelta

def run_command(command):
    try:
        print(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Command output: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print(f"Error output: {e.stderr}")
        print(f"Return code: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

def get_commit_message():
    messages = [
        "Update documentation",
        "Fix typo",
        "Add new feature",
        "Refactor code",
        "Improve performance",
        "Update dependencies",
        "Fix bug",
        "Clean up code",
        "Add tests",
        "Minor changes"
    ]
    return random.choice(messages)

try:
    now = datetime.datetime.now()
    
    # No commits on weekends (70% chance)
    if now.weekday() >= 5 and random.random() < 0.7:
        print("🏖️ Weekend break! No commits today.")
        sys.exit(0)
    
    # Simulate a lazy day (15% chance on weekdays, 40% chance on weekends)
    lazy_chance = 0.4 if now.weekday() >= 5 else 0.15
    if random.random() < lazy_chance:
        print("🛌 Taking the day off. No commits today.")
        sys.exit(0)

    # Decide number of commits based on day of week
    if now.weekday() < 5:  # Weekday
        commit_weights = (
            [1]*5 +         # Light day (1 commit)
            [2]*4 +         # Medium day (2 commits)
            [3]*3 +         # Heavier (3 commits)
            [4]*2 +         # Even heavier (4)
            [5]*1           # Super productive day
        )
    else:  # Weekend
        commit_weights = (
            [1]*7 +         # Most likely 1 commit
            [2]*3           # Occasionally 2 commits
        )
    
    commit_count = random.choice(commit_weights)
    print(f"👨‍💻 Workday: making {commit_count} commits.")

    # Ensure activity.log exists and directory is writable
    try:
        with open("activity.log", "a") as f:
            f.write("")
    except IOError as e:
        print(f"Error accessing activity.log: {str(e)}")
        sys.exit(1)

    for i in range(commit_count):
        filename = "activity.log"

        print(f"Writing to {filename}")
        with open(filename, "a") as f:
            f.write(f"{now}: {get_commit_message()}\n")

        print("Adding file to git")
        run_command(["git", "add", filename])
        
        print("Creating commit")
        commit_message = get_commit_message()
        run_command(["git", "commit", "-m", commit_message])

        if i < commit_count - 1:
            # More realistic delays between commits (2-15 minutes)
            delay = random.randint(120, 900)
            print(f"⏱️ Sleeping {delay}s before next commit...")
            time.sleep(delay)

except Exception as e:
    print(f"Unexpected error in main execution: {str(e)}")
    sys.exit(1)
