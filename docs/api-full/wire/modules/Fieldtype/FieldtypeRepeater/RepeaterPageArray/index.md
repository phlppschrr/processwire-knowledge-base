# RepeaterPageArray

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPageArray.php`

Inherits: `PageArray`

## Summary

ProcessWire Repeater Page Array

Common methods:
- [`setParent()`](method-setparent.md)
- [`setForPage()`](method-setforpage.md)
- [`getParent()`](method-getparent.md)
- [`getForPage()`](method-getforpage.md)
- [`setForField()`](method-setforfield.md)

Special PageArray for use by repeaters that includes a `getNewItem()` method
for adding new items to the repeater.

## Methods
- [`__construct(Page $parent, Field $field)`](method-__construct.md) Construct
- [`setForPage(Page $forPage)`](method-setforpage.md) Set page this RepeaterPageArray is for
- [`getForPage(): Page`](method-getforpage.md) Get page this RepeaterPageArray is for
- [`setForField(Field $field)`](method-setforfield.md) Set repeater field this RepeaterPageArray is for
- [`getForField(): RepeaterField`](method-getforfield.md) Get repeater field this RepeaterPageArray is for
- [`getNewItem(): RepeaterPage`](method-getnewitem.md) Return a new repeater item ready for use
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md) Track an item added
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md) Track an item removed
