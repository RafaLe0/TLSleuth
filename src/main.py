#!/usr/bin/env python3

"""
TLSleuth :: Created by Rafael Fron, 2025-10-27

Scanning a Network, a host to check for weak encryption, bad TLS, expired certificate... 

Usage : TLSleuth --host example.com
"""


""" For ascii """
import importlib.resources as pkg_resources
from pathlib import Path

import tlsleuth  

def loadAScii () -> str:
    try:
        return pkg_ressources.read_text("tlsleuth.assets", "TLSleuthAscii.txt")
    except Exception:
        p = Path(__file__).parent / "assets" / 	"TLSleuthAscii.txt"
        try:
            return p.read_text(encoding="utf-8")
        except Exception:
            return "TLSleuth - Banner not found.\n"

print(loadAscii())
