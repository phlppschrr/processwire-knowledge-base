# SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Inherits: `WireArray`


Groups:
Group: [other](group-other.md)

ProcessWire Selectable Option Array, for FieldtypeOptions

Methods:
- [`setPage(Page $page)`](method-setpage.md)
- [`getPage(): NullPage|Page`](method-getpage.md)
- [`setField(Field $field)`](method-setfield.md)
- [`getField(): null|Field`](method-getfield.md)
- [`of(bool|null $of = null): bool`](method-of.md)
- [`render(): string`](method-render.md)
- [`__toString(): string`](method-__tostring.md)
- [`getProperty(string $property): mixed|null`](method-getproperty.md)
- [`setProperty(string $property, mixed $value): SelectableOption|SelectableOptionArray`](method-setproperty.md)
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md)
- [`getByProperty(string $property, string|int $value, bool|null $noValue = false): bool|null|SelectableOption`](method-getbyproperty.md)
- [`getOptionByProperty(string $property, string|int $value): bool|SelectableOption`](method-getoptionbyproperty.md)
- [`addByProperty(string $property, string|int $value): SelectableOption|false`](method-addbyproperty.md)
- [`addByID(int $id): false|SelectableOption`](method-addbyid.md)
- [`addByValue(string $value): false|SelectableOption`](method-addbyvalue.md)
- [`addByTitle(string $title): false|SelectableOption`](method-addbytitle.md)
- [`getByID(int $id): SelectableOption|null`](method-getbyid.md)
- [`getByValue(string $value): SelectableOption|null`](method-getbyvalue.md)
- [`getByTitle(string $title): SelectableOption|null`](method-getbytitle.md)
- [`removeByProperty(string $property, string|int $value): bool`](method-removebyproperty.md)
- [`removeByID(int $id): bool`](method-removebyid.md)
- [`removeByValue(string $value): bool`](method-removebyvalue.md)
- [`removeByTitle(string $title): bool`](method-removebytitle.md)
- [`hasValue(string $value): SelectableOption|bool`](method-hasvalue.md)
- [`hasTitle(string $title): SelectableOption|bool`](method-hastitle.md)
- [`hasID(int $id): SelectableOption|bool`](method-hasid.md)
