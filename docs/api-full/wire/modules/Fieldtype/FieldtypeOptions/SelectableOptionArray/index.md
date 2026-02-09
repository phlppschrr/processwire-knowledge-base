# SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Inherits: `WireArray`

## Summary

ProcessWire Selectable Option Array, for FieldtypeOptions

Common methods:
- [`setPage()`](method-setpage.md)
- [`getPage()`](method-getpage.md)
- [`setField()`](method-setfield.md)
- [`getField()`](method-getfield.md)
- [`of()`](method-of.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`setPage(Page $page)`](method-setpage.md) Set the these options live on
- [`getPage(): NullPage|Page`](method-getpage.md) Returns page these options are for, if applicable (NullPage otherwise)
- [`setField(Field $field)`](method-setfield.md) Set the field these options are for
- [`getField(): null|Field`](method-getfield.md) Returns Field object these options are for
- [`of(bool|null $of = null): bool`](method-of.md) Get or set output formatting mode
- [`render(): string`](method-render.md) Provide a default string rendering of these selectable options
- [`__toString(): string`](method-__tostring.md) Return string value of these options (pipe separated IDs)
- [`getProperty(string $property): mixed|null`](method-getproperty.md) Enables this WireArray to behave like the first item (for getting properties)
- [`setProperty(string $property, mixed $value): SelectableOption|SelectableOptionArray`](method-setproperty.md) Enables this WireArray to behave like the first item (for setting properties)
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md) Is the given WireArray identical to this one?
- [`getByProperty(string $property, string|int $value, bool|null $noValue = false): bool|null|SelectableOption`](method-getbyproperty.md) Get SelectableOption by $property matching $value, or boolean false if not found
- [`getOptionByProperty(string $property, string|int $value): bool|SelectableOption`](method-getoptionbyproperty.md) Alias of getByProperty
- [`addByProperty(string $property, string|int $value): SelectableOption|false`](method-addbyproperty.md) Add option by property (id, name, title)
- [`addByID(int $id): false|SelectableOption`](method-addbyid.md) Add by option ID
- [`addByValue(string $value): false|SelectableOption`](method-addbyvalue.md) Add by option value
- [`addByTitle(string $title): false|SelectableOption`](method-addbytitle.md) Add by option title
- [`getByID(int $id): SelectableOption|null`](method-getbyid.md) Get option by ID
- [`getByValue(string $value): SelectableOption|null`](method-getbyvalue.md) Get option by value
- [`getByTitle(string $title): SelectableOption|null`](method-getbytitle.md) Get option by title
- [`removeByProperty(string $property, string|int $value): bool`](method-removebyproperty.md) Remove item by property (value, title, id)
- [`removeByID(int $id): bool`](method-removebyid.md) Remove option by ID
- [`removeByValue(string $value): bool`](method-removebyvalue.md) Remove option by value
- [`removeByTitle(string $title): bool`](method-removebytitle.md) Remove option by title
- [`hasValue(string $value): SelectableOption|bool`](method-hasvalue.md) Is the given value present in these selectable options?
- [`hasTitle(string $title): SelectableOption|bool`](method-hastitle.md) Is the given title present in these selectable options?
- [`hasID(int $id): SelectableOption|bool`](method-hasid.md) Is the given id present in these selectable options?
