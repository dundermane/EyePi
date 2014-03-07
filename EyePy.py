#!/usr/bin/env python

import curses
import time
from gmail import Ginbox
import wifi

'Gmail Login Stuff'
gmail_sn = ''
gmail_pw = ''

'set up our screen'
stdscr = curses.initscr()
stdscr.nodelay(1)
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdsize = stdscr.getmaxyx()
LINES = stdsize[0]
COLUMNS = stdsize[1]


'lets initialize some color pairs'
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)

'set up our main window'
begin_x = 1; begin_y = 1
height = LINES - 2 * begin_y
width = COLUMNS - 2 * begin_x
win = curses.newwin(height, width, begin_y, begin_x)
win.border()


'start our mail window'
mailwin = curses.newwin(3,18, height+begin_y - 3, begin_x + width-18)
mailwin.border(0,0,curses.ACS_BULLET,curses.ACS_BULLET,curses.ACS_BULLET,curses.ACS_BULLET,curses.ACS_BULLET,curses.ACS_BULLET)

'check our mail'
mail = Ginbox(gmail_sn , gmail_pw)

unread = mail.numUnread()
q = -1
exit = 0
while(q < 0):
    q = stdscr.getch()
    win.redrawwin()
    mailwin.redrawwin()
    win.refresh()
    mailwin.refresh()
    win.addstr(1,1, str(time.strftime('%a %I:%M')))
    win.addstr(1,width - len(wifi.name()) - 2, wifi.name())
    win.addstr(2,width - 13, "|          |")
    win.addstr(2,width - 12, "*"*(wifi.strength()/10))
    if mail.numUnread() > unread:
        mailwin.addstr(1,1,"NEW",curses.A_REVERSE)
    else:
	mailwin.addstr(1,1,"   ")
    win.addstr( height-2, 1, ' '*(width-8))
    win.addstr( height-2, 1, 'Latest: '+str(mail.get_subjects(-1))[:(width-20)])
    unread = mail.numUnread()
    mailwin.addstr(1, 5, 'Gmail: ' + str(mail.numUnread()))
    time.sleep(1)

'end window'
curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()

