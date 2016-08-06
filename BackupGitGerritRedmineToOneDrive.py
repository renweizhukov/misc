#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

def findItemBasedOnName(items, name):
    foundItem = None
    for item in items:
        if item.name == name:
            foundItem = item
            break
        else:
            pass

    return foundItem

redirect_uri = 'http://localhost:8080/'
client_secret = 'EvMDiYvjSSHZi0hHKjN1gcc'
client_id = 'e0a1b84a-2f92-4e1c-bf75-6ba37fb1c60a'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

client = onedrivesdk.get_default_client(client_id, scopes)
auth_url = client.auth_provider.get_auth_url(redirect_uri)

code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
print code
client.auth_provider.authenticate(code, redirect_uri, client_secret)

item_id = "root"
items = client.item(id = item_id).children.get()

path = "/SmartConn/Backup/Gerrit"
if path is not None and path[0] == '/':
    path = path[1:]
else:
    pass

folderNames = path.split('/')

foundItem = None
for folderName in folderNames:
    foundItem = findItemBasedOnName(items, folderName)
    if foundItem is not None:
        if foundItem.folder is not None:
            items = client.item(id = foundItem.id).children.get()
        else:
            print "%s is not a folder." % folderName
            sys.exit(1)
    else:
        print "The folder %s doesn't exist." % folderName
        sys.exit(1)

returned_item = client.item(id = foundItem.id).children['test.txt'].upload('./test.txt')
