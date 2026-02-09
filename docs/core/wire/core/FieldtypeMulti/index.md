# FieldtypeMulti

Source: `wire/core/FieldtypeMulti.php`

Inherits: `Fieldtype`


Groups:
Group: [other](group-other.md)

ProcessWire FieldtypeMulti

Interface and some functionality for Fieldtypes that can contain multiple values.




To support automatic “order by” sorting: The `$useOrderByCols` property of this Fieldtype must be set to boolean true,
indicating that the Fieldtype supports sorting. The actual columns to order by are an array of 'col' or '-col' specified
with the Field object in an $orderByCols property (array).

To support pagination: Both the `$useOrderByCols` and the `$usePagination` properties of this Fieldtype must be set to
boolean true, indicating the Fieldtype supports pagination (and sorting). When enabled, the wakeupValue() method will receive
pagination information in the value it is given. All other aspects of pagination must be handled by the individual Fieldtype.

Methods:
- [`getDatabaseSchema(Field $field): array`](method-getdatabaseschema.md)
- [`getSelectorInfo(Field $field, array $data = array()): array`](method-___getselectorinfo.md) (hookable)
- [`getCompatibleFieldtypes(Field $field): Fieldtypes|null`](method-___getcompatiblefieldtypes.md) (hookable)
- [`getBlankValue(Page $page, Field $field): WireArray`](method-getblankvalue.md)
- [`sanitizeValue(Page $page, Field $field, mixed $value): WireArray`](method-sanitizevalue.md)
- [`wakeupValue(Page $page, Field $field, array $value): WireArray`](method-___wakeupvalue.md) (hookable)
- [`sleepValue(Page $page, Field $field, WireArray $value): array`](method-___sleepvalue.md) (hookable)
- [`savePageField(Page $page, Field $field): bool`](method-___savepagefield.md) (hookable)
- [`loadPageField(Page $page, Field $field): array|null`](method-___loadpagefield.md) (hookable)
- [`getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadquery.md)
- [`getLoadQueryWhere(Field $field, DatabaseQuerySelect $query, string $col, string $operator, mixed $value): DatabaseQuery`](method-getloadquerywhere.md)
- [`setupPageFieldRows(Page $page, Field $field, $value): WireArray`](method-setuppagefieldrows.md)
- [`lockForWriting(Field $field): bool`](method-lockforwriting.md)
- [`unlockForWriting(): bool`](method-unlockforwriting.md)
- [`getMaxColumnValue(Page $page, Field $field, string $column, int|bool $noValue = false): int|bool|mixed`](method-getmaxcolumnvalue.md)
- [`getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL`](method-getloadqueryautojoin.md)
- [`getMatchQuery(PageFinderDatabaseQuerySelect $query, string $table, string $subfield, string $operator, mixed $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect`](method-getmatchquery.md)
- [`getConfigInputfields(Field $field): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)

Constants:
- [`multiValueSeparator`](const-multivalueseparator.md)
