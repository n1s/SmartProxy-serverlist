# VPN Configuration Rewriter for SmartProxy
This Python script converts a list of VPN endpoints (e.g., NordVPN servers) into a server list file that can be imported into the SmartProxy VPN browser extension. It allows you to bypass proprietary VPN vendor apps/extensions and use the open-source SmartProxy extension instead.

## Usage
1. Get user and pass/token from your VPN (NordVPN) provider website.
2. Set in the script or export ENV variables:
```bash
export VPN_USER="your_username"
export VPN_PASS="your_password"
```
```python
user = "your_username"
password = "your_password"
hostlist = "input.txt"
```
3. Run the script:
```bash
HOSTLIST=nordvpn.txt python3 rewrite_serverlist.py
```
4. Import `serverlist.txt` into SmartProxy.

## Example
Output (`serverlist.txt`):
```
ae49.nordvpn.com:89 [HTTPS] [ae49] [your_username] [your_password]
```
