#!/usr/bin/env python3

from __future__ import print_function
import imaplib
import os

email    = os.environ['EMAIL']
password = os.popen('security find-generic-password -w -s email -a "' + email + '"').read().replace('\n', '')

imap = imaplib.IMAP4_SSL('imap.gmail.com', '993')
imap.login(email, password)
imap.select()

fp = open('/tmp/GMAIL_UNREAD', 'w')
print(len(imap.search(None,'UnSeen')[1][0].split()), file=fp)
