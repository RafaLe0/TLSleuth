#!/usr/bin/env python3

"""
TLSleuth :: Created by Rafael Fron, 2025-10-27

Scanning a Network, a host to check for weak encryption, bad TLS, expired certificate... 

Usage:
    TLSleuth --host example.com
    TLSleuth --file hosts.txt --verbose --json
"""
import argparse
import json
import sys
from tlsleuth.utils import load_ascii
from tlsleuth.scanner import scan_host_list
from tlsleuth.logger_setup import setup_logging

logger = setup_loggin()

def parse_args():
    """Parse CLI arguments."""
    
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

def load_hosts(args):
    """Load hosts from --host or --file."""
    hosts = []
    if args.host:
        hosts.append(args.host.strip())
    if args.file:
        with open(args.file, "r", encoding="utf-8") as file:
            hosts.extend([line.strip() for line in file if line.strip()])
    except FileNotFoundError:
        logger.error(f"File not found: {args.file}")
        sys.exit(1)
    if not hosts:
        logger.error("No hosts provided. Use --host or --file to specify targets.")
        sys.exit(1)
    return hosts

def main():
    """
    Main entry point of TLSleuth.
    Prints the banner and initializes the scanner CLI.
    """
    args = parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled")
        
    logger.info("\n" + load_ascii())

    hosts = load_hosts(args)
    logger.info(f"Loaded {len(hosts)} host(s) for scanning")


    

if __name__ == "__main__":
    main()
