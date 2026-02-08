# $wireDatabaseBackup->supportsExec(array $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

Determine if exec is available for the given command

Note that WireDatabaseBackup does not currently use exec() mode so this is here for future use.

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->supportsExec();

// usage with all arguments
$bool = $wireDatabaseBackup->supportsExec(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `bool`

## Exceptions

- `\Exception` on unknown exec type
