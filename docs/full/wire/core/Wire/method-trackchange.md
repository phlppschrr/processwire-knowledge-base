# $wire->trackChange($what, $old = null, $new = null): $this

Source: `wire/core/Wire.php`

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.

## Arguments

- string $what Name of property that changed
- mixed $old Previous value before change
- mixed $new New value

## Return value

$this
