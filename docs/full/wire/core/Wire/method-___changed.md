# $wire->changed($what, $old = null, $new = null)

Source: `wire/core/Wire.php`

Hookable method that is called whenever a property has changed while change tracking is enabled.

- Enables hooks to monitor changes to the object.
- Do not call this method directly, as the `Wire::trackChange()` method already does so.
- Descending classes should call `$this->trackChange('name', $oldValue, $newValue);` when a property they are tracking has changed.

## Usage

~~~~~
// basic usage
$result = $wire->changed($what);

// usage with all arguments
$result = $wire->changed($what, $old = null, $new = null);
~~~~~

## Hookable

- Hookable method name: `changed`
- Implementation: `___changed`
- Hook with: `$wire->changed()`

## Arguments

- `$what` `string` Name of property that changed
- `$old` (optional) `mixed` Previous value before change
- `$new` (optional) `mixed` New value

## See Also

- [Wire::trackChange()](method-trackchange.md)
