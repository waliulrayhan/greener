import random
import datetime
import os
import sys
from datetime import timedelta

def get_commit_message():
    messages = [
        "Late night code optimization",
        "Fix critical bug before release",
        "Implement new feature while everyone's asleep",
        "Refactor code for better performance",
        "Late night debugging session",
        "Update project documentation",
        "Fix that annoying bug that kept me up",
        "Clean up codebase at midnight",
        "Add unit tests for night build",
        "Midnight code improvements",
        "Update configuration for production",
        "Optimize database performance",
        "Enhance UI for dark mode",
        "Late night security patches",
        "Add error handling for edge cases",
        "3 AM code cleanup",
        "Night owl session: code improvements",
        "Quiet hours: major refactoring",
        "Peaceful night coding",
        "Late night inspiration struck"
    ]
    return random.choice(messages)

def write_to_log(message, timestamp):
    try:
        with open("activity.log", "a") as f:
            f.write(f"{message} - {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
    except IOError as e:
        print(f"Error writing to activity.log: {str(e)}")
        sys.exit(1)

try:
    now = datetime.datetime.now()
    
    # More likely to code on weekends at night
    if now.weekday() >= 5 and random.random() < 0.3:  # Only 30% chance to skip weekend nights
        print("🏖️ Taking a weekend break!")
        sys.exit(0)
    
    # Less likely to skip night coding sessions
    lazy_chance = 0.2 if now.weekday() >= 5 else 0.1  # Night owls rarely skip
    if random.random() < lazy_chance:
        print("🛌 Even night owls need rest sometimes.")
        sys.exit(0)

    # Night owls tend to do more in one session
    if now.weekday() < 5:  # Weekday nights
        commit_weights = (
            [2]*4 +         # Light night (2 commits)
            [3]*5 +         # Medium night (3 commits)
            [4]*4 +         # Productive night (4 commits)
            [5]*3 +         # Very productive (5)
            [6]*1           # Epic coding night
        )
    else:  # Weekend nights
        commit_weights = (
            [3]*4 +         # Light weekend night (3 commits)
            [4]*5 +         # Medium weekend night (4 commits)
            [5]*4 +         # Heavy weekend night (5 commits)
            [6]*2           # Marathon coding session
        )
    
    commit_count = random.choice(commit_weights)
    print(f"🦉 Night coding session: planning {commit_count} commits.")

    # Create activity.log if it doesn't exist
    if not os.path.exists("activity.log"):
        open("activity.log", "a").close()
        print("Created new activity.log file")

    for i in range(commit_count):
        # More realistic night-time commit spacing
        commit_time = now + timedelta(minutes=i*random.randint(15, 45))
        commit_message = get_commit_message()
        
        # Write to activity log
        write_to_log(commit_message, commit_time)
        print(f"🌙 Logged commit: {commit_message}")

except Exception as e:
    print(f"Unexpected error in main execution: {str(e)}")
    sys.exit(1)
