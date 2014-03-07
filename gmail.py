#!/usr/bin/env python

import imaplib

class Ginbox:
    'A class that gives you info about a gmail inbox'
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
        self.imap_server.login(self.username, self.password)
        self.imap_server.select('INBOX',readonly=True)

    def numUnread(self):
        self.status, self.response = self.imap_server.status('INBOX', "(UNSEEN)")
        self.unreadcount = int(self.response[0].split()[2].strip(').,]'))
        return self.unreadcount

    def get_ids_unread(self):
        self.status, self.email_ids = self.imap_server.search(None, '(UNSEEN)')
        self.email_id = self.email_ids[0].split()
        return self.email_id
    def get_subjects(self, n):
	email_id = self.get_ids_unread()
        self.response = 'No Unread Messages'
        if (len(self.email_id) > max(n, 0)):
            _, self.response = self.imap_server.fetch(email_id[n], '(body[header.fields (subject)])')
            self.response = self.response[0][1].strip()
            self.response = self.response.strip('Subject: ')
        return self.response
