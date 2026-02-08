# $config->installedBefore($date): bool

Source: `wire/core/Config.php`

Was this ProcessWire installation installed before a particular date?

## Usage

~~~~~
// basic usage
$bool = $config->installedBefore($date);
~~~~~

## Arguments

- `$date` `int|string` Unix timestamp or strtotime() compatible date string

## Return value

- `bool`

## See Also

- [Config::installedAfter()](method-installedafter.md)
- Config::installed

## Since

3.0.129
