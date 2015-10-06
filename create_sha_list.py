#!/usr/bin/env python
import json
import hashlib
from base64 import b64encode

def hexdigest(site):
    hsh = hashlib.sha1()
    hsh.update(site)
    return hsh.hexdigest()

def digest(site):
    hsh = hashlib.sha1()
    hsh.update(site)
    return hsh.digest()

if __name__ == "__main__":
    with open('sites.json', 'r') as f:
        data = json.load(f)

    blacklist = set()

    for cat, sites in data.iteritems():
        for site in sites:
            blacklist.add(site)

    blacklist = sorted(list(blacklist))

    b64_blacklist = [b64encode(digest(site)) for site in blacklist]
    hex_blacklist = [hexdigest(site) for site in blacklist]

    with open('newtab.inadjacency.sha1.hex.json', 'w') as f:
        json.dump({'domains': hex_blacklist}, f)

    with open('newtab.inadjacency.sha1.b64.json', 'w') as f:
        json.dump({'domains': b64_blacklist}, f)
