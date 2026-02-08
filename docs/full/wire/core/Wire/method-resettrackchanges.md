# Wire::resetTrackChanges()

Source: `wire/core/Wire.php`

Clears out any tracked changes and turns change tracking ON or OFF

~~~~
// Clear any changes that have been tracked and start fresh
$page->resetTrackChanges();
~~~~


@param bool $trackChanges True to turn change tracking ON, or false to turn OFF. Default of true is assumed.

@return $this
