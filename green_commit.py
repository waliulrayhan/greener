import random
import datetime
import os
import subprocess

# Random number of commits: 0 to 3
commit_count = random.randint(0, 3)

if commit_count == 0:
    print("No commit today 😴")
    exit(0)

for i in range(commit_count):
    now = datetime.datetime.now()
    filename = "activity.log"

    with open(filename, "a") as f:
        f.write(f"{now}: Random commit #{i+1}\n")

    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Auto commit #{i+1} on {now}"])
