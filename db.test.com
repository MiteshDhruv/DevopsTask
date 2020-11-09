example.com.        IN  SOA dns.example.com. robbmanes.example.com. 2015082541 7200 3600 1209600 3600 
www A 1h 127.0.0.9
sub2 A 1h 127.0.0.10
sub3 A 1h 127.0.0.10
stats CNAME 30m .a.abc
   @   MX    1h  1 aspmx.l.google.com.
   @   MX    1h	 5 alt1.aspmx.l.google.com
   @   MX    1h  5 alt2.aaspmx.l.google.com.

TXT someTXT code 
 @    TXT        30   "go1"
 @    TXT        30   "go2"     
