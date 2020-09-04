#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from field
app_type = form.getvalue('app_type')
port  = form.getvalue('port')
cmd = form.getvalue('cmd')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s %s</h2>" % (app_type, port, cmd)
print "</body>"
print "</html>"
