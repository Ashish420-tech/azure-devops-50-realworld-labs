import os

dirs = ["config", "logs", "platform", "scripts"]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created directory: {d}")
