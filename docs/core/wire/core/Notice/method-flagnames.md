# $notice->flagNames($flags = null, $getString = false): array|string

Source: `wire/core/Notice.php`

Get string of names for given flags integer

## Usage

~~~~~
// basic usage
$array = $notice->flagNames();

// usage with all arguments
$array = $notice->flagNames($flags = null, $getString = false);
~~~~~

## Arguments

- `$flags` (optional) `null|int` Specify flags integer or omit to return all flag names (default=null)
- `$getString` (optional) `bool` Get a space separated string rather than an array (default=false)

## Return value

- `array|string`

## Since

3.0.149
