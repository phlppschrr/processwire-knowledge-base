# $wire->resetTrackChanges($trackChanges = true): $this

Source: `wire/core/Wire.php`

Clears out any tracked changes and turns change tracking ON or OFF

~~~~
// Clear any changes that have been tracked and start fresh
$page->resetTrackChanges();
~~~~

## Arguments

- `$trackChanges` (optional) `bool` True to turn change tracking ON, or false to turn OFF. Default of true is assumed.

## Return value

$this
