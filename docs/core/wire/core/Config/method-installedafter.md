# $config->installedAfter($date): bool

Source: `wire/core/Config.php`

Was this ProcessWire installation installed after a particular date?

## Usage

~~~~~
// basic usage
$bool = $config->installedAfter($date);
~~~~~

## Arguments

- `$date` `int|string` Unix timestamp or strtotime() compatible date string

## Return value

- `bool`

## See Also

- [Config::installedBefore()](method-installedbefore.md)
- Config::installed

## Since

3.0.129
