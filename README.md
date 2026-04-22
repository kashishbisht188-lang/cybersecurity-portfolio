# Failed Login Parser

A Python tool that detects failed SSH login attempts on Linux systems using journalctl.

## How to run
python3 login_parser.py

## What it does
- Pulls system logs using journalctl
- Filters lines containing failed login attempts
- Displays each attempt numbered with a total count

## Built with
- Python 3
- subprocess module
- Kali Linux
