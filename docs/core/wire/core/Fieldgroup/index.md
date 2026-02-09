# Fieldgroup

Source: `wire/core/Fieldgroup.php`

Inherits: `WireArray`
Implements: `Saveable`, `Exportable`, `HasLookupItems`


Groups:
Group: [other](group-other.md)
Group: [retrieval](group-retrieval.md)

ProcessWire Fieldgroup

A group of fields that is ultimately attached to a Template.

Fieldgroup is a type of WireArray that holds a group of Field objects for template(s).
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.

The existance of Fieldgroups is hidden at the ProcessWire web admin level
as it appears that fields are attached directly to Templates. However, they
are separated in the API in case want want to have fieldgroups used by
multiple templates in the future (like ProcessWire 1.x).

Methods:
- [`add(Field|string $item): $this`](method-add.md)
- [`remove(Field|string $key): bool`](method-remove.md)
- [`softRemove(Field|string|int $field): bool|Fieldgroup|WireArray`](method-softremove.md)
- [`getField(string|int|Field $key, bool|string $useFieldgroupContext = false): Field|null`](method-getfield.md)
- [`hasFieldContext(int|string|Field $field, string $namespace = ''): bool`](method-hasfieldcontext.md)
- [`getFieldContext(string|int|Field $key, string $namespace = ''): Field|null`](method-getfieldcontext.md)
- [`hasField(string|int|Field $key): bool`](method-hasfield.md)
- [`get(string|int $key): Field|string|int|null|array`](method-get.md)
- [`set(string $key, string|int|object $value): Fieldgroup|WireArray`](method-set.md)
- [`save(): $this`](method-save.md)
- [`__toString()`](method-__tostring.md)
- [`getPageInputfields(Page $page, string|array $contextStr = '', string|array $fieldName = '', string $namespace = '', bool $flat = true): InputfieldWrapper`](method-getpageinputfields.md)
- [`getTemplates(): TemplatesArray`](method-gettemplates.md)
- [`getNumTemplates(): int`](method-getnumtemplates.md)
- [`saveContext(): int`](method-savecontext.md)

Constants:
- [`contextNamespacePrefix`](const-contextnamespaceprefix.md)
