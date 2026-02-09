# RepeaterPageArray

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPageArray.php`

Inherits: `PageArray`

ProcessWire Repeater Page Array

Special PageArray for use by repeaters that includes a `getNewItem()` method
for adding new items to the repeater.

Methods:
- [`__construct(Page $parent, Field $field)`](method-__construct.md)
- [`setForPage(Page $forPage)`](method-setforpage.md)
- [`getForPage(): Page`](method-getforpage.md)
- [`setForField(Field $field)`](method-setforfield.md)
- [`getForField(): RepeaterField`](method-getforfield.md)
- [`getNewItem(): RepeaterPage`](method-getnewitem.md)
- [`trackAdd(Wire|mixed $item, int|string $key)`](method-trackadd.md)
- [`trackRemove(Wire|mixed $item, int|string $key)`](method-trackremove.md)
