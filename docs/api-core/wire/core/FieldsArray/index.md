# FieldsArray

Source: `wire/core/FieldsArray.php`

Inherits: `WireArray`

## Summary

ProcessWire Fields Array

Common methods:
- [`isValidItem()`](method-isvaliditem.md)
- [`isValidKey()`](method-isvalidkey.md)
- [`getItemKey()`](method-getitemkey.md)
- [`makeBlankItem()`](method-makeblankitem.md)

WireArray of Field instances, as used by Fields class

## Methods
- [`isValidItem(Wire $item): bool`](method-isvaliditem.md) Per WireArray interface, only Field instances may be added
- [`isValidKey(int $key): bool`](method-isvalidkey.md) Per WireArray interface, Field keys have to be integers
- [`getItemKey(Field $item): int`](method-getitemkey.md) Per WireArray interface, Field instances are keyed by their ID
- [`makeBlankItem(): Field`](method-makeblankitem.md) Per WireArray interface, return a blank Field
