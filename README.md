# misc
Collection of miscellaneous code.

## BackupGitGerritRedmineToOneDrive.py

This python program is built using the Microsoft OneDrive SDK for Python (https://github.com/OneDrive/onedrive-sdk-python). It completes the client authentication, find the target folder item from the given path "/SmartConn/Backup/Gerrit", and upload a file "test.txt" to the folder. This program works on a client machine with a browser but doesn't work on a server machine without a browser, since the authorization code has to be extracted from the redirect uri which will be displayed in the browser.
