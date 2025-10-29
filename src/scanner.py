import ssl
import socket
import datetime
import logging
from typing import Optional, List, Dict


logger = logging.getLogger(__name__)

def scan_hosts(host, timeout=5, verbose=False) :
  """
  Function to scan hosts SSL version and protocols. 

  args : 
    - Host :: A List or a single host address depending on the user input.
    - Timeout :: 5 sec of timeout between each host. Take the value passing by the user in args if set. 
    - verbose :: Enable or not the verbose mode. Arg passed by user. Default value => False.

  Return : 
  Array containing infos such as : 
    - tls version
    - expired/not expired
    - cypher
    - name...
  """

  result = {
        "host": host,
        "tls_version": None,
        "cert_expired": None,
        "issuer": None,
        "valid_until": None,
        "weak_cipher": False,
        "error": None,
    }
  try: 
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        with socket.create_connection((host, 443), timeout=timeout) as sock:
          with context.wrap_socket(sock, server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            version = ssock.version()
            result["tls_version"] = version
            result["cipher"] = cipher[0]
            
            # Cert validation : 
            isValid = cert.get("notAfter")
            if isValid:
              


    
def scan_host_list(hosts, timeout=5, verbose=False):
    """
    Scan multiple hosts sequentially.

    args: 
    - Host :: A List or a single host address depending on the user input.
    - Timeout :: 5 sec of timeout between each host. Take the value passing by the user in args if set. 
    - verbose :: Enable or not the verbose mode. Arg passed by user. Default value => False.
    
    Returns a list of result dicts.
    """
    results = []
    for host in hosts:
        res = scan_host(host, timeout, verbose)
        results.append(res)
    return results
