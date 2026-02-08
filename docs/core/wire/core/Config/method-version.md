# $config->version($minVersion = ''): bool|string

Source: `wire/core/Config.php`

Check if current ProcessWire version is equal to or newer than given version, or return current version

If no version argument is given, it simply returns the current ProcessWire version (3.0.130+)

~~~~~
if($config->version('3.0.100')) {
  // ProcessWire version is 3.0.100 or newer
}
~~~~~

## Arguments

- string $minVersion Specify version string if you want to compare against current version

## Return value

bool|string Returns current version if no argument given (3.0.130+), OR boolean if given a version argument: - If given version is older than current, returns false. - If given version is equal to or newer than current, returns true.

## Meta

- @since 3.0.106 with no-argument behavior added in 3.0.130
