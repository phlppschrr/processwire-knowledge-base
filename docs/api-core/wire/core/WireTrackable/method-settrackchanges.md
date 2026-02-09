# $wireTrackable->setTrackChanges($trackChanges = true): $this

Source: `wire/core/Interfaces.php`

Turn change tracking ON or OFF

## Usage

~~~~~
// basic usage
$result = $wireTrackable->setTrackChanges();

// usage with all arguments
$result = $wireTrackable->setTrackChanges($trackChanges = true);
~~~~~

## Arguments

- `$trackChanges` (optional) `bool|int` True to turn on, false to turn off. Integer to specify bitmask.

## Return value

- `$this`
