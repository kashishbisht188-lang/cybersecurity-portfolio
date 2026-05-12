# Cybersecurity Portfolio
Learning cybersecurity through hands-on practice on Kali Linux.

## Projects
| Week | Project | Tools |
|------|---------|-------|
| 1 | Log Analysis | Bash, grep, awk, sed |
| 1 | Network Analysis | Wireshark |
| 2 | Failed Login Parser | Python, journalctl |

## How to Run

**Log Analyzer**
bash log_analyzer.sh

**Failed Login Parser**
python3 parser.py --file auth.log

## Sample Output — Failed Login Parser
Top Failed Login Attempts:
```
Top Failed Login Attempts:
------------------------------
192.168.1.105        4 attempts
10.0.0.22            2 attempts
10.0.0.55            1 attempts
```
