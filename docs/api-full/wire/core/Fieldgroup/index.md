# Fieldgroup

Source: `wire/core/Fieldgroup.php`

Inherits: `WireArray`
Implements: `Saveable`, `Exportable`, `HasLookupItems`

## Summary

ProcessWire Fieldgroup

Common methods:
- [`isValidItem()`](method-isvaliditem.md)
- [`isValidKey()`](method-isvalidkey.md)
- [`getItemKey()`](method-getitemkey.md)
- [`makeBlankItem()`](method-makeblankitem.md)
- [`add()`](method-add.md)

Groups:
Group: [other](group-other.md)
Group: [retrieval](group-retrieval.md)

A group of fields that is ultimately attached to a Template.

Fieldgroup is a type of WireArray that holds a group of Field objects for template(s).
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.

The existance of Fieldgroups is hidden at the ProcessWire web admin level
as it appears that fields are attached directly to Templates. However, they
are separated in the API in case want want to have fieldgroups used by
multiple templates in the future (like ProcessWire 1.x).

## Methods
- [`add(Field|string $item): $this`](method-add.md) Add a field to this Fieldgroup
- [`remove(Field|string $key): bool`](method-remove.md) Remove a field from this fieldgroup
- [`softRemove(Field|string|int $field): bool|Fieldgroup|WireArray`](method-softremove.md) Remove a field without queueing it to be removed from database
- [`getField(string|int|Field $key, bool|string $useFieldgroupContext = false): Field|null`](method-getfield.md) Get a field that is part of this fieldgroup
- [`hasFieldContext(int|string|Field $field, string $namespace = ''): bool`](method-hasfieldcontext.md) Does the given Field have context data available in this fieldgroup?
- [`getFieldContext(string|int|Field $key, string $namespace = ''): Field|null`](method-getfieldcontext.md) Get a Field that is part of this Fieldgroup, in the context of this Fieldgroup.
- [`hasField(string|int|Field $key): bool`](method-hasfield.md) Does this fieldgroup have the given field?
- [`get(string|int $key): Field|string|int|null|array`](method-get.md) Get a Fieldgroup property or a Field.
- [`set(string $key, string|int|object $value): Fieldgroup|WireArray`](method-set.md) Set a fieldgroup property
- [`save(): $this`](method-save.md) Save this Fieldgroup to the database
- [`__toString()`](method-__tostring.md) Fieldgroups always return their name when dereferenced as a string
- [`getPageInputfields(Page $page, string|array $contextStr = '', string|array $fieldName = '', string $namespace = '', bool $flat = true): InputfieldWrapper`](method-getpageinputfields.md) Get all of the Inputfields for this Fieldgroup associated with the provided Page and populate them.
- [`getTemplates(): TemplatesArray`](method-gettemplates.md) Get a list of all templates using this Fieldgroup
- [`getNumTemplates(): int`](method-getnumtemplates.md) Get the number of templates using this Fieldgroup
- [`saveContext(): int`](method-savecontext.md) Save field contexts for this fieldgroup

## Constants
- [`contextNamespacePrefix = 'NS_'`](const-contextnamespaceprefix.md)
