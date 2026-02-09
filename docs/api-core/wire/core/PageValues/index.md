# PageValues

Source: `wire/core/PageValues.php`

Inherits: `Wire`

ProcessWire Page Values

Provides implementation for several Page value get() functions.


@since 3.0.205

Methods:
- [`getDotValue(Page $page, string $key): mixed|null`](method-getdotvalue.md) Given a 'field.subfield' type string traverse properties and return value
- [`getBracketValue(Page $page, string $key, mixed $value = null): array|mixed|Page|PageArray|Wire|WireArray|WireData|string|\Traversable`](method-getbracketvalue.md) Get value that ends with square brackets to get iterable value, filtered value or property value
- [`getMultiple(Page $page, array|string $keys, bool $assoc = false): array`](method-getmultiple.md) Get multiple Page property/field values in an array
- [`getFieldFirstValue(Page $page, string $multiKey, bool $getKey = false): null|mixed`](method-getfieldfirstvalue.md) Given a Multi Key, determine if there are multiple keys requested and return the first non-empty value
- [`getMarkup(Page $page, string $key): string`](method-getmarkup.md) Return the markup value for a given field name or {tag} string
- [`getText(Page $page, string $key, bool $oneLine = false, bool|null $entities = null): string`](method-gettext.md) Same as getMarkup() except returned value is plain text
- [`setStatus(Page $page, $value): Page`](method-setstatus.md) Set the status setting, with some built-in protections
- [`removeStatus(Page $page, int|string $statusFlag): Page`](method-removestatus.md) Remove the specified status from this page
- [`setName(Page $page, string $value, Language|string|int|null $language = null): Page`](method-setname.md) Set the page name, optionally for specific language
- [`getInputfields(Page $page, string|array $fieldName = ''): null|InputfieldWrapper`](method-getinputfields.md) Return all Inputfield objects necessary to edit this page
- [`getInputfield(Page $page, string $fieldName): Inputfield|InputfieldWrapper|null`](method-getinputfield.md) Get a single Inputfield for the given field name
- [`getField(Page $page, string|int|Field $field): Field|null`](method-getfield.md) Get a Field object in context or NULL if not valid for this page
- [`getFields(Page $page): FieldsArray`](method-getfields.md) Returns a FieldsArray of all Field objects in the context of this Page
- [`hasField(Page $page, int|string|Field|array $field): bool|string`](method-hasfield.md) Returns whether or not given $field name, ID or object is valid for this Page
- [`getFieldValue(Page $page, string $key, string $selector = ''): null|mixed`](method-getfieldvalue.md) Get the value for a non-native page field, and call upon Fieldtype to join it if not autojoined
- [`formatFieldValue(Page $page, Field $field, mixed $value): mixed`](method-formatfieldvalue.md) Return a value consistent with the page’s output formatting state
