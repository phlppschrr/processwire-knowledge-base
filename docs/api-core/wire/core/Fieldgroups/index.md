# Fieldgroups

Source: `wire/core/Fieldgroups.php`

Inherits: `WireSaveableItemsLookup`

## Summary

ProcessWire Fieldgroups

Common methods:
- [`init()`](method-init.md)
- [`getLoadQuery()`](method-getloadquery.md)
- [`load()`](method-___load.md)
- [`getAll()`](method-getall.md)
- [`getWireArray()`](method-getwirearray.md)

Groups:
Group: [other](group-other.md)

Maintains collections of Fieldgroup object instances and represents the `$fieldgroups` API variable.
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.
`$fieldgroups`

## Methods
- [`init()`](method-init.md) Init
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md) Get the DatabaseQuerySelect to perform the load operation of items
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable) Load all the Fieldgroups from the database
- [`getAll(): FieldgroupsArray`](method-getall.md) Per WireSaveableItems interface, return all available Fieldgroup instances
- [`getWireArray(): WireArray|FieldgroupsArray`](method-getwirearray.md)
- [`makeBlankItem(): Fieldgroup`](method-makeblankitem.md) Per WireSaveableItems interface, create a blank instance of a Fieldgroup
- [`getTable(): string`](method-gettable.md) Per WireSaveableItems interface, return the name of the table that Fieldgroup instances are stored in
- [`getLookupTable(): string`](method-getlookuptable.md) Per WireSaveableItemsLookup interface, return the name of the table that Fields are linked to Fieldgroups
- [`getNumTemplates(Fieldgroup $fieldgroup): int`](method-getnumtemplates.md) Get the number of templates using the given fieldgroup.
- [`getTemplates(Fieldgroup $fieldgroup): TemplatesArray`](method-gettemplates.md) Given a Fieldgroup, return a TemplatesArray of all templates using the Fieldgroup
- [`getFieldNames(string|int|Fieldgroup $fieldgroup): array`](method-getfieldnames.md) Get all field names used by given fieldgroup
- [`save(Saveable $item): bool`](method-___save.md) (hookable) Save the Fieldgroup to DB
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable) Delete the given fieldgroup from the database
- [`deleteField(Field $field): bool`](method-deletefield.md) Delete the entries in fieldgroups_fields for the given Field
- [`clone(Saveable $item, string $name = ''): Fieldgroup|false`](method-___clone.md) (hookable) Create and return a cloned copy of this item
- [`saveContext(Fieldgroup $fieldgroup): int`](method-___savecontext.md) (hookable) Save contexts for all fields in the given fieldgroup
- [`getExportData(Fieldgroup $fieldgroup): array`](method-___getexportdata.md) (hookable) Export config data for the given fieldgroup
- [`setImportData(Fieldgroup $fieldgroup, array $data): array`](method-___setimportdata.md) (hookable) Given an export data array, import it back to the class and return what happened
- [`fieldAdded(Fieldgroup $fieldgroup, Field $field)`](method-___fieldadded.md) (hookable) Hook called when field has been added to fieldgroup
- [`fieldRemoved(Fieldgroup $fieldgroup, Field $field)`](method-___fieldremoved.md) (hookable) Hook called when field has been removed from fieldgroup
