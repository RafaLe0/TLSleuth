#!/usr/bin/env python3

"""
TLSleuth :: Created by Rafael Fron, 2025-10-27

Scanning a Network, a host to check for weak encryption, bad TLS, expired certificate... 

Usage : TLSleuth --host example.com
"""
import logging
import argparse
from tlsleuth.utils import load_ascii
from tlsleuth.scanner import scan_host_list

def parse_args():
    parser = argparse.ArgumentParser(
        prog="TLSleuth",
        description="Scan hosts for weak TLS/SSL settings and certificate issues."
    )
    parser.add_argument("--host", type=str, help="Single host to scan (ex: example.com)")
    parser.add_argument("--file", type=str, help="File containing list of hosts, one per line")
    parser.add_argument("--timeout", type=int, default=5, help="Connection timeout in seconds")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output for debugging")
    return parser.parse_args()



def main():
    """
    Main entry point of TLSleuth.
    Prints the banner and initializes the scanner CLI.
    """
    print(load_ascii())
    args = parse_args()

    hosts = []
    if args.host:
        hosts.append(args.host.strip())
    if args.file:
        with open(args.file, "r", encoding="utf-8") as file:
            hosts.extend([line.strip() for line in file if line.strip()])
except FileNotFoundError:
    logg
    # TODO: Scanner logic
    print("[*] Welcome to TLSleuth. A simple tool to automate and discover weak TLS certificates Use --help for options.")
    

if __name__ == "__main__":
    main()
