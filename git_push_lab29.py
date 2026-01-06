import os
import subprocess
import sys

LAB_DIR = "lab-29-jenkins-kubernetes"
COMMIT_MSG = "Lab 29: Jenkins + Kubernetes + Helm with rollback"

def run_cmd(cmd, error_msg):
    try:
        result = subprocess.run(
            cmd, shell=True, check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"\n❌ ERROR: {error_msg}")
        print(e.stderr)
        sys.exit(1)

def main():
    print("\n🚀 Git Push Automation Started\n")

    # 1️⃣ Check git repo
    if not os.path.isdir(".git"):
        print("❌ ERROR: This directory is NOT a git repository")
        sys.exit(1)

    # 2️⃣ Check lab directory
    if not os.path.isdir(LAB_DIR):
        print(f"❌ ERROR: '{LAB_DIR}' not found in this repo")
        sys.exit(1)

    # 3️⃣ Get current branch
    branch = run_cmd(
        "git branch --show-current",
        "Unable to detect current git branch"
    )
    print(f"✅ Current branch: {branch}")

    # 4️⃣ Check remote origin
    remotes = run_cmd(
        "git remote",
        "Unable to list git remotes"
    )

    if "origin" not in remotes:
        print("❌ ERROR: Remote 'origin' not configured")
        print("➡️ Run: git remote add origin <repo-url>")
        sys.exit(1)

    print("✅ Remote 'origin' exists")

    # 5️⃣ Git add
    run_cmd(
        f"git add {LAB_DIR}",
        "Failed to add Lab-29 files"
    )
    print("✅ Files staged")

    # 6️⃣ Commit
    status = run_cmd(
        "git status --porcelain",
        "Failed to check git status"
    )

    if not status:
        print("⚠️ No changes to commit (already committed?)")
    else:
        run_cmd(
            f'git commit -m "{COMMIT_MSG}"',
            "Git commit failed"
        )
        print("✅ Commit created")

    # 7️⃣ Push
    run_cmd(
        f"git push origin {branch}",
        "Git push failed (auth/branch issue)"
    )

    print("\n🎉 SUCCESS: Lab-29 pushed to GitHub!")
    print(f"📦 Branch: {branch}")
    print("🔗 Verify on GitHub")

if __name__ == "__main__":
    main()
