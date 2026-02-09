# Fieldtype

Source: `wire/core/Fieldtype.php`

Inherits: `WireData`
Implements: `Module`

ProcessWire Fieldtype Base

Abstract base class from which all Fieldtype modules are descended from.

Fieldtype is a module type used to represent a type of field. All Fieldtype modules descend from this.
Almost all methods in a Fieldtype are primarily of concern to module developers, as Fieldtype modules do not
have a public API (most of the time). Instead, they provide methods used by `Page` and `Field` objects (and related)
to work with the field data. Most Fieldtype modules only need to implement a few methods like
`Fieldtype::sanitizeValue()` (which is required) and `Fieldtype::getDatabaseSchema()`, as the default implementation
of most other methods provided in this Fieldtype class accounts for most situations already.



Methods:
- [`getInputfield(Page $page, Field $field): Inputfield|null`](method-getinputfield.md)
- [`getConfigInputfields(Field $field): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`getConfigArray(Field $field): array`](method-___getconfigarray.md) (hookable)
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md) (hookable)
- [`getConfigAdvancedInputfields(Field $field): InputfieldWrapper`](method-___getconfigadvancedinputfields.md) (hookable)
- [`exportConfigData(Field $field, array $data): array`](method-___exportconfigdata.md) (hookable)
- [`importConfigData(Field $field, array $data): array`](method-___importconfigdata.md) (hookable)
- [`getCompatibleFieldtypes(Field $field): Fieldtypes|null`](method-___getcompatiblefieldtypes.md) (hookable)
- [`sanitizeValue(Page $page, Field $field, string|int|WireArray|object $value): string|int|WireArray|object`](method-sanitizevalue.md)
- [`formatValue(Page $page, Field $field, string|int|object $value): mixed`](method-___formatvalue.md) (hookable)
- [`markupValue(Page $page, Field $field, mixed $value = null, string $property = ''): string|MarkupFieldtype`](method-___markupvalue.md) (hookable)
- [`getBlankValue(Page $page, Field $field): string|int|object|null`](method-getblankvalue.md)
- [`isDeleteValue(Page $page, Field $field, mixed $value): bool`](method-isdeletevalue.md)
- [`isEmptyValue(Field $field, mixed $value): bool`](method-isemptyvalue.md)
- [`wakeupValue(Page $page, Field $field, string|int|array $value): string|int|array|object`](method-___wakeupvalue.md) (hookable)
- [`sleepValue(Page $page, Field $field, string|int|float|array|object $value): string|int|float|array`](method-___sleepvalue.md) (hookable)
- [`exportValue(Page $page, Field $field, string|int|float|array|object|null $value, array $options = array()): string|float|int|array`](method-___exportvalue.md) (hookable)
- [`getMatchQuery(PageFinderDatabaseQuerySelect $query, string $table, string $subfield, string $operator, mixed $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect`](method-getmatchquery.md)
- [`createField(Field $field): bool`](method-___createfield.md) (hookable)
- [`getDatabaseSchema(Field $field): array`](method-getdatabaseschema.md)
- [`getFieldClass(array $a = array()): string`](method-getfieldclass.md)
- [`getSelectorInfo(Field $field, array $data = array()): array`](method-___getselectorinfo.md) (hookable)
- [`loadPageField(Page $page, Field $field): mixed|null`](method-___loadpagefield.md) (hookable)
- [`loadPageFieldFilter(Page $page, Field $field, Selectors|string|array $selector): mixed|null`](method-___loadpagefieldfilter.md) (hookable)
- [`getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadquery.md)
- [`getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL`](method-getloadqueryautojoin.md)
- [`savePageField(Page $page, Field $field): bool`](method-___savepagefield.md) (hookable)
- [`deleteField(Field $field): bool`](method-___deletefield.md) (hookable)
- [`deletePageField(Page $page, Field $field): bool`](method-___deletepagefield.md) (hookable)
- [`emptyPageField(Page $page, Field $field): bool`](method-___emptypagefield.md) (hookable)
- [`emptyPageFieldTable(Page $page, Field $field): bool`](method-emptypagefieldtable.md)
- [`replacePageField(Page $src, Page $dst, Field $field): bool`](method-___replacepagefield.md) (hookable)
- [`deleteTemplateField(Template $template, Field $field): bool`](method-___deletetemplatefield.md) (hookable)
- [`cloneField(Field $field): Field`](method-___clonefield.md) (hookable)
- [`get(string $key): mixed`](method-get.md)
- [`install()`](method-___install.md) (hookable)
- [`uninstall()`](method-___uninstall.md) (hookable)
- [`upgrade($fromVersion, $toVersion)`](method-___upgrade.md) (hookable)
- [`__toString()`](method-__tostring.md)

Hookable methods
================

- [`getConfigInputfields(Field $field): InputfieldWrapper`](method-___getconfiginputfields.md)
- [`getConfigAdvancedInputfields(Field $field): InputfieldWrapper`](method-___getconfigadvancedinputfields.md)
- [`getConfigArray(Field $field): array`](method-___getconfigarray.md)
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md)
- [`exportConfigData(Field $field, array $data): array`](method-___exportconfigdata.md)
- [`importConfigData(Field $field, array $data): array`](method-___importconfigdata.md)
- [`getCompatibleFieldtypes(Field $field): Fieldtypes|null`](method-___getcompatiblefieldtypes.md)
- [`formatValue(Page $page, Field $field, $value): mixed`](method-___formatvalue.md)
- [`markupValue(Page $page, Field $field, $value = null, $property = ''): string|MarkupFieldtype`](method-___markupvalue.md)
- [`wakeupValue(Page $page, Field $field, $value): mixed`](method-___wakeupvalue.md)
- [`sleepValue(Page $page, Field $field, $value): string|int|array`](method-___sleepvalue.md)
- [`exportValue(Page $page, Field $field, $value, array $options = array()): string|float|int|array`](method-___exportvalue.md)
- `importValue(Page $page, Field $field, $value, array $options = array()): string|float|int|array|object`
- [`createField(Field $field): bool`](method-___createfield.md)
- [`getSelectorInfo(Field $field, array $data = array()): array`](method-___getselectorinfo.md)
- [`loadPageField(Page $page, Field $field): mixed|null`](method-___loadpagefield.md)
- [`loadPageFieldFilter(Page $page, Field $field, $selector): mixed|null`](method-___loadpagefieldfilter.md)
- [`savePageField(Page $page, Field $field): bool`](method-___savepagefield.md)
- [`deleteField(Field $field): bool`](method-___deletefield.md)
- [`deletePageField(Page $page, Field $field): bool`](method-___deletepagefield.md)
- [`emptyPageField(Page $page, Field $field): bool`](method-___emptypagefield.md)
- [`replacePageField(Page $src, Page $dst, Field $field): bool`](method-___replacepagefield.md)
- [`deleteTemplateField(Template $template, Field $field): bool`](method-___deletetemplatefield.md)
- [`cloneField(Field $field): Field`](method-___clonefield.md)
- `renamedField(Field $field, $prevName): void`
- `savedField(Field $field): void`
- `saveFieldReady(Field $field): void`
- [`install(): void`](method-___install.md)
- [`uninstall(): void`](method-___uninstall.md)
- `getFieldSetups(): array`
- `$name: string` Name of Fieldtype module.
- `$shortName: string` Short name of Fieldtype, which excludes the "Fieldtype" prefix.
- `$longName: string` Long name of Fieldtype, which is typically the module title.
