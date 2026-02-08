# $wireTrackable->trackChange($what, $old = null, $new = null): $this

Source: `wire/core/Interfaces.php`

Track a change to a property in this object

The change will only be recorded if self::$trackChanges is true.

## Arguments

- string $what Name of property that changed
- mixed $old Previous value before change
- mixed $new New value

## Return value

$this
