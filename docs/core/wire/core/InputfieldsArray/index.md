# InputfieldsArray

Source: `wire/core/InputfieldsArray.php`

Inherits: `WireArray`

A WireArray of Inputfield instances, as used by InputfieldWrapper.

The default numeric indexing of a WireArray is not overridden.

Methods:
- [`isValidItem(Wire $item): bool`](method-isvaliditem.md) Per WireArray interface, only Inputfield instances are accepted.
- [`find(string $selector): WireArray|InputfieldsArray`](method-find.md) Extends the find capability of WireArray to descend into the Inputfield children
