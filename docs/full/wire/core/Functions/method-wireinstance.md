# $functions->wireInstance(?Wire $wire = null): ProcessWire

Source: `wire/core/Functions.php`

Get or set the current ProcessWire instance

## Usage

~~~~~
// basic usage
$processWire = $functions->wireInstance();

// usage with all arguments
$processWire = $functions->wireInstance(?Wire $wire = null);
~~~~~

## Arguments

- `$wire` (optional) `Wire|null` To set specify ProcessWire instance or any Wire-derived object in it, or omit to get current instance.

## Return value

- `ProcessWire`

## Since

3.0.125
