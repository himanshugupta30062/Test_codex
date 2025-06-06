import subprocess
from typing import List


def list_files_in_branch(branch: str = "main") -> List[str]:
    """Return a list of files tracked in the given git branch."""
    result = subprocess.run(
        ["git", "ls-tree", "--name-only", branch],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    files = result.stdout.strip().splitlines()
    return files

if __name__ == "__main__":
    for f in list_files_in_branch():
        print(f)
