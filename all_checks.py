#!/usr/bin/env python3
import os
import sys

# this is the comment about the check_reboot() function
def check_reboot():
    """insert comment"""
    return os.path.exists("/run/reboot-required")

# this is new comment

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
