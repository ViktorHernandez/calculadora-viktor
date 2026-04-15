import os
import datetime
import subprocess

LOG_FILE = "backup.log"

def get_git_log():
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-10"],
            capture_output=True, text=True
        )
        return result.stdout.strip() if result.returncode == 0 else "No git history available"
    except Exception:
        return "Git not available"

def get_file_list():
    files = []
    for root, _, filenames in os.walk("dist"):
        for f in filenames:
            path = os.path.join(root, f)
            size = os.path.getsize(path)
            files.append(f"  {path} ({size} bytes)")
    return "\n".join(files)

timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
build_id  = os.environ.get("CODEBUILD_BUILD_ID", "local-build")
commit    = os.environ.get("CODEBUILD_RESOLVED_SOURCE_VERSION", "unknown")[:8]

entry = f"""
========================================
BACKUP LOG — {timestamp}
========================================
Build ID : {build_id}
Commit   : {commit}

Archivos desplegados:
{get_file_list()}

Historial de commits recientes:
{get_git_log()}
----------------------------------------
"""

with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"backup.log actualizado: {timestamp}")
