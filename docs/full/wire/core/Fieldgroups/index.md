# Fieldgroups

Source: `wire/core/Fieldgroups.php`

Inherits: `WireSaveableItemsLookup`


Groups:
Group: [other](group-other.md)

ProcessWire Fieldgroups

Maintains collections of Fieldgroup object instances and represents the `$fieldgroups` API variable.
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.
$fieldgroups

Methods:
- [`init()`](method-init.md)
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md)
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable)
- [`getAll(): FieldgroupsArray`](method-getall.md)
- [`getWireArray(): WireArray|FieldgroupsArray`](method-getwirearray.md)
- [`makeBlankItem(): Fieldgroup`](method-makeblankitem.md)
- [`getTable(): string`](method-gettable.md)
- [`getLookupTable(): string`](method-getlookuptable.md)
- [`getNumTemplates(Fieldgroup $fieldgroup): int`](method-getnumtemplates.md)
- [`getTemplates(Fieldgroup $fieldgroup): TemplatesArray`](method-gettemplates.md)
- [`getFieldNames(string|int|Fieldgroup $fieldgroup): array`](method-getfieldnames.md)
- [`save(Saveable $item): bool`](method-___save.md) (hookable)
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable)
- [`deleteField(Field $field): bool`](method-deletefield.md)
- [`clone(Saveable $item, string $name = ''): Fieldgroup|false`](method-___clone.md) (hookable)
- [`saveContext(Fieldgroup $fieldgroup): int`](method-___savecontext.md) (hookable)
- [`getExportData(Fieldgroup $fieldgroup): array`](method-___getexportdata.md) (hookable)
- [`setImportData(Fieldgroup $fieldgroup, array $data): array`](method-___setimportdata.md) (hookable)
- [`fieldAdded(Fieldgroup $fieldgroup, Field $field)`](method-___fieldadded.md) (hookable)
- [`fieldRemoved(Fieldgroup $fieldgroup, Field $field)`](method-___fieldremoved.md) (hookable)
