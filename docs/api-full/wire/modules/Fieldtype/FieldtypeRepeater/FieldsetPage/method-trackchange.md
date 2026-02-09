# $fieldsetPage->trackChange($what, $old = null, $new = null): $this

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldsetPage.php`

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.

## Usage

~~~~~
// basic usage
$result = $fieldsetPage->trackChange($what);

// usage with all arguments
$result = $fieldsetPage->trackChange($what, $old = null, $new = null);
~~~~~

## Arguments

- `$what` `string` Name of property that changed
- `$old` (optional) `mixed` Previous value before change
- `$new` (optional) `mixed` New value

## Return value

- `$this`
