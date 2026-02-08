# $wireLog->deleteAll($throw = false): array

Source: `wire/core/WireLog.php`

Delete all log files

## Usage

~~~~~
// basic usage
$array = $wireLog->deleteAll();

// usage with all arguments
$array = $wireLog->deleteAll($throw = false);
~~~~~

## Arguments

- `$throw` (optional) `bool` Throw WireException if any delete fails? (default=false)

## Return value

- `array` Basenames of deleted log files

## Since

3.0.214
