#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#  OKUSON Package
#  Frank L�beck and Max Neunh�ffer

'''This is the script to make the OKUSON server stop.'''

import os,sys,getpass,urllib,time,signal

import Config         # this automatically determines our home dir
                      # but does not read the configuration file

# Fetch the "Utils" and switch error reporting to log file:

from Tools import Utils

# Now we can read our configuration file with proper error reporting
# (note that this might fail miserably):

Config.ReadConfig()
Config.PostProcessing()    # some postprocessing of configuration data


f = file("log/server.log","r")
f.seek(0,2)     # seek to end of file
p = f.tell()

pid = os.fork()
if pid == 0:
    time.sleep(0.5)   # Let the parent get hold of the log file
    # Now send the request:
    u = urllib.urlopen('http://localhost:'+str(Config.conf['Port'])+
                           '/AdminWork?Action=PID')
    spid = u.read()
    u.close()
    os.kill(int(spid), signal.SIGUSR1)
    print 'Sent server with PID '+spid+' a USR1 signal.'
    sys.exit(0)  # Terminate this child process

while 1:
    f.seek(0,2)
    np = f.tell()
    if np > p:
        f.seek(p)
        s = f.readlines()
        p = f.tell()
        for l in s:
            sys.stdout.write(l)
            sys.stdout.flush()
            if l[-15:] == 'Terminating...\n':
                sys.exit(0)
            elif l == 'Aborting.\n':
                sys.exit(0)
    time.sleep(0.5)


