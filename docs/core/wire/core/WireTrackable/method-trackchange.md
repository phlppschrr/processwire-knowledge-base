# $wireTrackable->trackChange($what, $old = null, $new = null): $this

Source: `wire/core/Interfaces.php`

Track a change to a property in this object

The change will only be recorded if self::$trackChanges is true.

## Arguments

- `$what` `string` Name of property that changed
- `$old` (optional) `mixed` Previous value before change
- `$new` (optional) `mixed` New value

## Return value

$this
