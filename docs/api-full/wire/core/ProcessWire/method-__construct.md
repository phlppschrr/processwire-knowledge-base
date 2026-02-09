# $processWire->__construct($config = null, $rootURL = '/')

Source: `wire/core/ProcessWire.php`

Create a new ProcessWire instance

## Example

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

## Usage

~~~~~
// basic usage
$result = $processWire->__construct();

// usage with all arguments
$result = $processWire->__construct($config = null, $rootURL = '/');
~~~~~

## Arguments

- `$config` (optional) `Config|string|null` May be any of the following: - A Config object as returned from ProcessWire::buildConfig(). - A string path to PW installation. - You may optionally omit this argument if current dir is root of PW installation.
- `$rootURL` (optional) `string` URL or scheme+host to installation. - This is only used if $config is omitted or a path string. - May also include scheme & hostname, i.e. "http://hostname.com/url" to force use of scheme+host. - If omitted, it is determined automatically.

## Exceptions

- `WireException` if given invalid arguments
