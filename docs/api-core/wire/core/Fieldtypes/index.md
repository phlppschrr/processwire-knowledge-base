# Fieldtypes

Source: `wire/core/Fieldtypes.php`

Inherits: `WireArray`


Groups:
Group: [other](group-other.md)

ProcessWire Fieldtypes

Maintains a collection of Fieldtype modules.
$fieldtypes

Methods:
- [`__construct()`](method-__construct.md) Construct
- [`init()`](method-init.md) Construct the $fieldtypes API var (load all Fieldtype modules into it)
- [`preload()`](method-preload.md) Convert all ModulePlaceholders to Fieldtype modules
- [`isValidItem(Wire|Fieldtype $item): bool`](method-isvaliditem.md) Per WireArray interface, items added to Fieldtypes must be Fieldtype instances
- [`isValidKey(string|int $key): bool`](method-isvalidkey.md) Per the WireArray interface, keys must be strings (fieldtype class names)
- [`getItemKey(Fieldtype $item): string`](method-getitemkey.md) Per the WireArray interface, Fields are indxed by their name
- [`makeBlankItem(): null`](method-makeblankitem.md) Per the WireArray interface, return a blank copy
- [`get(string $key): Fieldtype|null`](method-get.md) Given a Fieldtype name (or class name) return the instantiated Fieldtype module.
- [`getArray()`](method-getarray.md) Below we account for all get() related functions in WireArray to preload the fieldtypes
