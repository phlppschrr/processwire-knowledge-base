# FieldtypeMulti

Source: `wire/core/FieldtypeMulti.php`

Inherits: `Fieldtype`

## Summary

ProcessWire FieldtypeMulti

Common methods:
- [`getDatabaseSchema()`](method-getdatabaseschema.md)
- [`getSelectorInfo()`](method-___getselectorinfo.md)
- [`getCompatibleFieldtypes()`](method-___getcompatiblefieldtypes.md)
- [`getBlankValue()`](method-getblankvalue.md)
- [`sanitizeValue()`](method-sanitizevalue.md)

Groups:
Group: [other](group-other.md)

Interface and some functionality for Fieldtypes that can contain multiple values.




To support automatic “order by” sorting: The `$useOrderByCols` property of this Fieldtype must be set to boolean true,
indicating that the Fieldtype supports sorting. The actual columns to order by are an array of 'col' or '-col' specified
with the Field object in an `$orderByCols` property (array).

To support pagination: Both the `$useOrderByCols` and the `$usePagination` properties of this Fieldtype must be set to
boolean true, indicating the Fieldtype supports pagination (and sorting). When enabled, the wakeupValue() method will receive
pagination information in the value it is given. All other aspects of pagination must be handled by the individual Fieldtype.

## Methods
- [`getDatabaseSchema(Field $field): array`](method-getdatabaseschema.md) Modify the default schema provided by Fieldtype to include a 'sort' field, and integrate that into the primary key.
- [`getSelectorInfo(Field $field, array $data = array()): array`](method-___getselectorinfo.md) (hookable) Return array with information about what properties and operators can be used with this field
- [`getCompatibleFieldtypes(Field $field): Fieldtypes|null`](method-___getcompatiblefieldtypes.md) (hookable) Get an array of Fieldtypes that are compatible with this one (i.e. ones the user may change the type to)
- [`getBlankValue(Page $page, Field $field): WireArray`](method-getblankvalue.md) Per Fieldtype interface, return a blank value of this Fieldtype
- [`sanitizeValue(Page $page, Field $field, mixed $value): WireArray`](method-sanitizevalue.md) Per the Fieldtype interface, sanitize the combined value for use in a Page
- [`wakeupValue(Page $page, Field $field, array $value): WireArray`](method-___wakeupvalue.md) (hookable) Process the value to convert it from array to whatever object it needs to be
- [`sleepValue(Page $page, Field $field, WireArray $value): array`](method-___sleepvalue.md) (hookable) Given an 'awake' value, as set by wakeupValue, convert the value back to a basic type for storage in DB.
- [`savePageField(Page $page, Field $field): bool`](method-___savepagefield.md) (hookable) Per the Fieldtype interface, Save the given Field from the given Page to the database
- [`loadPageField(Page $page, Field $field): array|null`](method-___loadpagefield.md) (hookable) Load the given page field from the database table and return the value.
- [`getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadquery.md) Return the query used for loading all parts of the data from this field.
- [`getLoadQueryWhere(Field $field, DatabaseQuerySelect $query, string $col, string $operator, mixed $value): DatabaseQuery`](method-getloadquerywhere.md) Apply a where condition to a load query (used by getLoadQuery method)
- [`setupPageFieldRows(Page $page, Field $field, $value): WireArray`](method-setuppagefieldrows.md) Prepare rows for save or delete
- [`lockForWriting(Field $field): bool`](method-lockforwriting.md) Lock field table for writing
- [`unlockForWriting(): bool`](method-unlockforwriting.md) Unlock for writing
- [`getMaxColumnValue(Page $page, Field $field, string $column, int|bool $noValue = false): int|bool|mixed`](method-getmaxcolumnvalue.md) Get max value of column for given Page and Field or boolean false (or specified $noValue) if no rows present
- [`getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL`](method-getloadqueryautojoin.md) Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.
- [`getMatchQuery(PageFinderDatabaseQuerySelect $query, string $table, string $subfield, string $operator, mixed $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect`](method-getmatchquery.md) Get the query that matches a Fieldtype table's data with a given value
- [`getConfigInputfields(Field $field): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Get Inputfields for advanced settings of the Field and Fieldtype

## Constants
- [`multiValueSeparator = "\0,"`](const-multivalueseparator.md)
