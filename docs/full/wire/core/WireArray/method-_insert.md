# $wireArray->_insert($item, $existingItem, $insertBefore = true): $this

Source: `wire/core/WireArray.php`

Insert an item either before or after another

Provides the implementation for the insertBefore and insertAfter functions

## Arguments

- `$item` `int|string|array|object` Item you want to insert
- `$existingItem` `int|string|array|object` Item already present that you want to insert before/afer
- `$insertBefore` (optional) `bool` True if you want to insert before, false if after

## Return value

$this

## Throws

- WireException if given an invalid item
