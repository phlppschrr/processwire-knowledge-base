# FieldgroupsArray

Source: `wire/core/FieldgroupsArray.php`

Inherits: `WireArray`

## Summary

ProcessWire Fieldgroups Array

Common methods:
- [`isValidItem()`](method-isvaliditem.md)
- [`getItemKey()`](method-getitemkey.md)
- [`isValidKey()`](method-isvalidkey.md)
- [`makeBlankItem()`](method-makeblankitem.md)

WireArray of Fieldgroup instances as used by Fieldgroups class.

## Methods
- [`isValidItem($item)`](method-isvaliditem.md) Per WireArray interface, this class only carries Fieldgroup instances
- [`getItemKey($item)`](method-getitemkey.md) Per WireArray interface, items are keyed by their ID
- [`isValidKey($key)`](method-isvalidkey.md) Per WireArray interface, keys must be integers
- [`makeBlankItem()`](method-makeblankitem.md) Per WireArray interface, return a blank Fieldgroup
