# ProcessWire::buildConfig($rootPath = '', $rootURL = null, array $options = array()): Config

Source: `wire/core/ProcessWire.php`

Static method to build a Config object for booting ProcessWire

## Arguments

- string $rootPath Path to root of installation where ProcessWire's index.php file is located.
- string $rootURL Should be specified only for secondary ProcessWire instances. May also include scheme & hostname, i.e. "http://hostname.com/url" to force use of scheme+host.
- array $options Options to modify default behaviors (experimental): - `siteDir` (string): Name of "site" directory in $rootPath that contains site's config.php, no slashes (default="site").

## Return value

Config
