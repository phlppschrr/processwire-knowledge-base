# $wire->trackChange($what, $old = null, $new = null): $this

Source: `wire/core/Wire.php`

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.

## Arguments

- `$what` `string` Name of property that changed
- `$old` (optional) `mixed` Previous value before change
- `$new` (optional) `mixed` New value

## Return value

$this
