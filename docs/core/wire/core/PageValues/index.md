# PageValues

Source: `wire/core/PageValues.php`

Inherits: `Wire`

ProcessWire Page Values

Provides implementation for several Page value get() functions.


@since 3.0.205

Methods:
- [`getDotValue(Page $page, string $key): mixed|null`](method-getdotvalue.md)
- [`getBracketValue(Page $page, string $key, mixed $value = null): array|mixed|Page|PageArray|Wire|WireArray|WireData|string|\Traversable`](method-getbracketvalue.md)
- [`getMultiple(Page $page, array|string $keys, bool $assoc = false): array`](method-getmultiple.md)
- [`getFieldFirstValue(Page $page, string $multiKey, bool $getKey = false): null|mixed`](method-getfieldfirstvalue.md)
- [`getMarkup(Page $page, string $key): string`](method-getmarkup.md)
- [`getText(Page $page, string $key, bool $oneLine = false, bool|null $entities = null): string`](method-gettext.md)
- [`setStatus(Page $page, $value): Page`](method-setstatus.md)
- [`removeStatus(Page $page, int|string $statusFlag): Page`](method-removestatus.md)
- [`setName(Page $page, string $value, Language|string|int|null $language = null): Page`](method-setname.md)
- [`getInputfields(Page $page, string|array $fieldName = ''): null|InputfieldWrapper`](method-getinputfields.md)
- [`getInputfield(Page $page, string $fieldName): Inputfield|InputfieldWrapper|null`](method-getinputfield.md)
- [`getField(Page $page, string|int|Field $field): Field|null`](method-getfield.md)
- [`getFields(Page $page): FieldsArray`](method-getfields.md)
- [`hasField(Page $page, int|string|Field|array $field): bool|string`](method-hasfield.md)
- [`getFieldValue(Page $page, string $key, string $selector = ''): null|mixed`](method-getfieldvalue.md)
- [`formatFieldValue(Page $page, Field $field, mixed $value): mixed`](method-formatfieldvalue.md)
