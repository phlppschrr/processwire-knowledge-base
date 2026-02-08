# $wireArray->_insert($item, $existingItem, $insertBefore = true): $this

Source: `wire/core/WireArray.php`

Insert an item either before or after another

Provides the implementation for the insertBefore and insertAfter functions

## Arguments

- int|string|array|object $item Item you want to insert
- int|string|array|object $existingItem Item already present that you want to insert before/afer
- bool $insertBefore True if you want to insert before, false if after

## Return value

$this

## Throws

- WireException if given an invalid item
