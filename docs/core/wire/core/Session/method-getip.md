# Session::getIP()

Source: `wire/core/Session.php`

Get the IP address of the current user

~~~~~
$ip = $session->getIP();
echo $ip; // outputs 111.222.333.444
~~~~~


@param bool $int Return as a long integer? (default=false)
 - IPv6 addresses cannot be represented as an integer, so please note that using this int option makes it return a CRC32
   integer when using IPv6 addresses (3.0.184+).

@param bool|int $useClient Give preference to client headers for IP? HTTP_CLIENT_IP and HTTP_X_FORWARDED_FOR (default=false)
	- Specify integer 2 to include potential multiple CSV separated IPs (when provided by client).

@return string|int Returns string by default, or integer if $int argument indicates to.
