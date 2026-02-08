# ProcessWire::__construct()

Source: `wire/core/ProcessWire.php`

Create a new ProcessWire instance

~~~~~
// A. Current directory assumed to be root of installation
$wire = new ProcessWire();

// B: Specify a Config object as returned by ProcessWire::buildConfig()
$wire = new ProcessWire($config);

// C: Specify where installation root is
$wire = new ProcessWire('/server/path/');

// D: Specify installation root path and URL
$wire = new ProcessWire('/server/path/', '/url/');

// E: Specify installation root path, scheme, hostname, URL
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~

@param Config|string|null $config May be any of the following:
 - A Config object as returned from ProcessWire::buildConfig().
 - A string path to PW installation.
 - You may optionally omit this argument if current dir is root of PW installation.

@param string $rootURL URL or scheme+host to installation.
 - This is only used if $config is omitted or a path string.
 - May also include scheme & hostname, i.e. "http://hostname.com/url" to force use of scheme+host.
 - If omitted, it is determined automatically.

@throws WireException if given invalid arguments
