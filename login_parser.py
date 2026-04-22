import subprocess

def read_failed_logins():
    result = subprocess.run(
        ['journalctl', '--no-pager'],
        capture_output=True,
        text=True
    )

    print("=== Failed Login Attempts ===\n")
    count = 0

    for line in result.stdout.splitlines():
        if "Failed password" in line:
            count += 1
            print(f"[{count}] {line}")

    print(f"\nTotal failed attempts: {count}")

read_failed_logins()
