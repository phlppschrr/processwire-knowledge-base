# $wireLog->getFilename($name): string

Source: `wire/core/WireLog.php`

Get the full filename (including path) for the given log name

## Usage

~~~~~
// basic usage
$string = $wireLog->getFilename($name);
~~~~~

## Arguments

- `$name` `string` Name of log (not including extension)

## Return value

- `string` Filename to log file

## Exceptions

- `WireException` If given invalid log name
