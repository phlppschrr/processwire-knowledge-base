# $wireArray->import($items): $this

Source: `wire/core/WireArray.php`

Import the given item(s) into this WireArray.

- Adds imported items to the end of the WireArray.
- Skips over any items already present in the WireArray (when duplicateChecking is enabled)

## Arguments

- `$items` `array|WireArray` Items to import.

## Return value

$this

## Throws

- WireException If given items not compatible with the WireArray
