#!/usr/bin/python3

"""

__author__ = "ChrishSec"
__copyright__ = "Copyright (C) 2024 ChrishSec"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"

Website: https://ChrishSec.com
GitHub: https://github.com/ChrishSec
Twitter: https://twitter.com/ChrishSec

"""

import socket
import ssl
import concurrent.futures
import argparse
from tabulate import tabulate
from colorama import Fore, Style, init

init()

def SSL_Checker(subdomain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((subdomain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=subdomain) as ssock:
                certificate = ssock.getpeercert()
                return subdomain, "Has SSL", Fore.GREEN + "✔" + Style.RESET_ALL
    except ssl.SSLCertVerificationError as e:
        return subdomain, "Verification Failed", Fore.RED + "✘" + Style.RESET_ALL
    except socket.timeout:
        return subdomain, "Connection Timeout", Fore.YELLOW + "!" + Style.RESET_ALL
    except socket.gaierror as e:
        return subdomain, "DNS Resolution Failed", Fore.RED + "✘" + Style.RESET_ALL
    except Exception as e:
        return subdomain, f"Error: {e}", Fore.RED + "✘" + Style.RESET_ALL

def main():
    parser = argparse.ArgumentParser(description="SSLChecker By ChrishSec.com")
    parser.add_argument("-l", "--list", required=True, help="Path to the file containing the list of subdomains.")
    args = parser.parse_args()

    try:
        with open(args.list, "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]

        if not subdomains:
            print("The subdomains list is empty.")
            return

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(SSL_Checker, subdomains)

        table_data = [(subdomain, status, icon) for subdomain, status, icon in results]
        print(tabulate(table_data, headers=["Domain/Subdomain", "Status", "Result"], tablefmt="grid"))

    except FileNotFoundError:
        print(f"File not found: {args.list}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
