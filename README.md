# DevopsTask
https://github.com/coredns/coredns

https://gitlab.isc.org/isc-projects/bind9


Server this list(list can be json) on startup

For .example.com

www A 1h 127.0.0.5

sub2 A 1h 127.0.0.8


Also have entries for AAAA,CNAME,MX and TXT


While the server is running call a script/command to add .service.com
 

www A 1h 127.0.0.9

sub2 A 1h 127.0.0.10

sub3 A 1h 127.0.0.10

stats CNAME 30m .a.abc

@

MX

1h

1 aspmx.l.google.com.

5 alt1.aspmx.l.google.com.

5 alt2.aspmx.l.google.com.

TXT someTxt code

@

TXT

30m

"go1”

"go2”



        Add a script to change the list of domains(can be json) .. while the coreDNS or bind9 is running.
