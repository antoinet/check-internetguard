# Check InternetGuard Status

Small helper script used to check whether a domain is on the [Bluewin](https://www.bluewin.ch) blocklist
a.k.a [InternetGuard](https://www.swisscom.ch/en/residential/help/internet/internetguard.html).

## Example

```
$ ./check-dnsguard.sh bluewin.ch igtest.bluewin.org google.com 1bet.com
pass	bluewin.ch
block	igtest.bluewin.org
pass	google.com
block	1bet.com
```

