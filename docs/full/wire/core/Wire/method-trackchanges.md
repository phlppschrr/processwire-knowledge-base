# $wire->trackChanges($getMode = false): int

Source: `wire/core/Wire.php`

Returns true or 1 if change tracking is on, or false or 0 if it is not, or mode bitmask (int) if requested.

## Usage

~~~~~
// basic usage
$int = $wire->trackChanges();

// usage with all arguments
$int = $wire->trackChanges($getMode = false);
~~~~~

## Arguments

- `$getMode` (optional) `bool` When true, the track changes mode bitmask will be returned

## Return value

- `int` 0/false if off, 1/true if On, or mode bitmask if requested
