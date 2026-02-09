# $wireTrackable->getChanges($getValues = false): array

Source: `wire/core/Interfaces.php`

Return an array of properties that have changed while change tracking was on.

## Usage

~~~~~
// basic usage
$array = $wireTrackable->getChanges();

// usage with all arguments
$array = $wireTrackable->getChanges($getValues = false);
~~~~~

## Arguments

- `$getValues` (optional) `bool` If true, then an associative array will be retuned with field names and previous values.

## Return value

- `array`
