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
        "Update documentation and improve readability",
        "Fix typo in code comments",
        "Add new feature: automated logging",
        "Refactor code for better performance",
        "Improve system performance",
        "Update project dependencies",
        "Fix bug in main workflow",
        "Clean up codebase",
        "Add unit tests",
        "Minor code improvements",
        "Update configuration files",
        "Optimize database queries",
        "Enhance user interface",
        "Implement security fixes",
        "Add error handling"
    ]
    return random.choice(messages)

def write_to_log(message, timestamp):
    try:
        with open("activity.log", "a") as f:
            f.write(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    except IOError as e:
        print(f"Error writing to activity.log: {str(e)}")
        sys.exit(1)

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

    # Create activity.log if it doesn't exist
    if not os.path.exists("activity.log"):
        open("activity.log", "a").close()
        print("Created new activity.log file")

    for i in range(commit_count):
        commit_time = now + timedelta(minutes=i*random.randint(5, 30))
        commit_message = get_commit_message()
        
        # Write to activity log
        write_to_log(commit_message, commit_time)
        print(f"Logged commit: {commit_message}")

        # Git operations
        run_command(["git", "add", "activity.log"])
        run_command(["git", "commit", "-m", f"{commit_message} - {commit_time.strftime('%Y-%m-%d %H:%M:%S')}"])

        if i < commit_count - 1:
            # More realistic delays between commits (2-15 minutes)
            delay = random.randint(120, 900)
            print(f"⏱️ Sleeping {delay}s before next commit...")
            time.sleep(delay)

except Exception as e:
    print(f"Unexpected error in main execution: {str(e)}")
    sys.exit(1)
