#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import os,sys
import json 

f = open(os.path.join(sys.path[0], "Dockerfile"), "w+")

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from field
app_type = form.getvalue('app_type')
port  = form.getvalue('port')
cmd = form.getvalue('cmd')
run = form.getvalue('run')
env = form.getvalue('env')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s %s</h2>" % (app_type, port, cmd)
print "</body>"
print "</html>"



f = open(os.path.join(sys.path[0], "Dockerfile"), "w+")
if(app_type!=None):
  f.write("FROM: %s \n" %(app_type))
if(port!=None):
  f.write("EXPORT %s \n" %(port))
if(cmd!=None):
  f.write("CMD %s \n" %(cmd))
if(run!=None):
  runArray = run.split("\n")
  for i in runArray:
    f.write("RUN %s \n" %(json.dumps(list(i))))
if(env!=None):
    envIterator = iter(env)
    for x in envIterator:
      f.write("Env %s %s \n" %(x, next(envIterator) ))
f.close()

