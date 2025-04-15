import random
import datetime
import os
import sys
from datetime import timedelta
import pytz

def get_commit_message(hour):
    morning_messages = [
        "Early morning code optimization",
        "Start the day with some clean code",
        "Morning coffee and code cleanup",
        "Early bird debugging session",
        "Morning code review and fixes",
        "Start the day with fresh commits",
        "Early morning feature implementation",
        "Morning code refactoring",
        "Start the day with unit tests",
        "Morning code improvements"
    ]
    
    afternoon_messages = [
        "Afternoon code optimization",
        "Lunch break coding session",
        "Midday feature implementation",
        "Afternoon debugging session",
        "Code cleanup after lunch",
        "Afternoon code review",
        "Midday refactoring",
        "Afternoon performance improvements",
        "Post-lunch coding session",
        "Afternoon code fixes"
    ]
    
    evening_messages = [
        "Evening code optimization",
        "Post-work coding session",
        "Evening feature implementation",
        "Late afternoon debugging",
        "Evening code cleanup",
        "End of day code review",
        "Evening refactoring",
        "After hours performance improvements",
        "Evening coding session",
        "End of day fixes"
    ]
    
    night_messages = [
        "Late night code optimization",
        "Midnight coding session",
        "Night owl feature implementation",
        "Late night debugging",
        "Midnight code cleanup",
        "Night time code review",
        "Late night refactoring",
        "Night owl performance improvements",
        "Peaceful night coding",
        "Late night inspiration struck"
    ]
    
    if 5 <= hour < 12:
        return random.choice(morning_messages)
    elif 12 <= hour < 17:
        return random.choice(afternoon_messages)
    elif 17 <= hour < 22:
        return random.choice(evening_messages)
    else:
        return random.choice(night_messages)

def write_to_log(message, timestamp):
    try:
        with open("activity.log", "a") as f:
            f.write(f"{message} - {timestamp.strftime('%Y-%m-%d %H:%M:%S')} (GMT+6)\n")
    except IOError as e:
        print(f"Error writing to activity.log: {str(e)}")
        sys.exit(1)

try:
    # Get current time in Bangladesh timezone
    dhaka_tz = pytz.timezone('Asia/Dhaka')
    now = datetime.datetime.now(dhaka_tz)
    current_hour = now.hour
    
    # More likely to code on weekends
    if now.weekday() >= 5 and random.random() < 0.2:  # Only 20% chance to skip weekends
        print("🏖️ Taking a weekend break!")
        sys.exit(0)
    
    # Less likely to skip coding sessions
    lazy_chance = 0.15 if now.weekday() >= 5 else 0.1
    if random.random() < lazy_chance:
        print("🛌 Taking a short break.")
        sys.exit(0)

    # Increased commit frequency
    if now.weekday() < 5:  # Weekdays
        commit_weights = (
            [3]*4 +         # Light session (3 commits)
            [4]*5 +         # Medium session (4 commits)
            [5]*4 +         # Productive session (5 commits)
            [6]*3 +         # Very productive (6 commits)
            [7]*2 +         # Super productive (7 commits)
            [8]*1           # Epic coding session
        )
    else:  # Weekends
        commit_weights = (
            [4]*4 +         # Light weekend (4 commits)
            [5]*5 +         # Medium weekend (5 commits)
            [6]*4 +         # Heavy weekend (6 commits)
            [7]*3 +         # Very heavy weekend (7 commits)
            [8]*2           # Marathon coding session
        )
    
    commit_count = random.choice(commit_weights)
    print(f"👨‍💻 Coding session: planning {commit_count} commits.")

    # Create activity.log if it doesn't exist
    if not os.path.exists("activity.log"):
        open("activity.log", "a").close()
        print("Created new activity.log file")

    for i in range(commit_count):
        # More realistic commit spacing (10-30 minutes)
        commit_time = now + timedelta(minutes=i*random.randint(10, 30))
        commit_message = get_commit_message(commit_time.hour)
        
        # Write to activity log
        write_to_log(commit_message, commit_time)
        print(f"📝 Logged commit: {commit_message}")

except Exception as e:
    print(f"Unexpected error in main execution: {str(e)}")
    sys.exit(1)
