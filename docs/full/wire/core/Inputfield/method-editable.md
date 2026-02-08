# $inputfield->editable($setEditable = null): bool

Source: `wire/core/Inputfield.php`

Get or set editable state for this Inputfield

When set to false, the `Inputfield::processInput()` method won't be called by parent InputfieldWrapper,
effectively skipping over input processing entirely for this Inputfield.

## Arguments

- `$setEditable` (optional) `bool|null` Specify true or false to set the editable state, or omit just to get the editable state.

## Return value

bool Returns the current editable state.
