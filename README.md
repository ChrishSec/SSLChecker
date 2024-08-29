## SSL Checker

Allows you to verify whether SSL certificates are present for a specified list of domains/subdomains.

### Requirements
- Python 3.x
- Unix-like operating system (tested on Ubuntu 20.04)

### Usage

1. Clone the repository:

```git clone https://github.com/ChrishSec/SSLChcker.git```

2. Install the required dependencies:

```pip3 install -r requirements.txt```

3. Run the SSL Checker:

```
$ python3 SSLChecker.py -h
usage: SSLChecker.py [-h] -l LIST

SSLChecker By ChrishSec.com

options:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  Path to the file containing the list of subdomains.

```
```
$ python3 SSLChecker.py -l examples.txt
+---------------+----------+----------+
| Subdomain     | Status   | Result   |
+===============+==========+==========+
| google.com    | Has SSL  | ✔        |
+---------------+----------+----------+
| bing.com      | Has SSL  | ✔        |
+---------------+----------+----------+
| yahoo.com     | Has SSL  | ✔        |
+---------------+----------+----------+
| chrishsec.com | Has SSL  | ✔        |
+---------------+----------+----------+
```

## Disclaimer

This tool is intended for educational and research purposes only. Use it at your own risk. The author is not responsible for any damage caused by the use or misuse of this tool.

## License

This tool is released under the GNU General Public License v3.0. Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## Author

This tool was developed by [ChrishSec](https://github.com/ChrishSec). Feel free to fork, modify, and distribute it. If you have any questions or suggestions, please reach out to the author on [Telegram](https://t.me/ChrishSec).
