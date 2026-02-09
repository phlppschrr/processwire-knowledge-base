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



## Hookable Methods

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

Methods:
- [`getInputfield(Page $page, Field $field): Inputfield|null`](method-getinputfield.md) Return new instance of the Inputfield module associated with this Fieldtype.
- [`getConfigInputfields(Field $field): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Get any Inputfields used for configuration of this Fieldtype.
- [`getConfigArray(Field $field): array`](method-___getconfigarray.md) (hookable) Same as getConfigInputfields but with definition as an array instead
- [`getConfigAllowContext(Field $field): array`](method-___getconfigallowcontext.md) (hookable) Return an array of configuration field names from that are allowed in fieldgroup/template context
- [`getConfigAdvancedInputfields(Field $field): InputfieldWrapper`](method-___getconfigadvancedinputfields.md) (hookable) Get Inputfields for advanced settings of the Field and Fieldtype
- [`exportConfigData(Field $field, array $data): array`](method-___exportconfigdata.md) (hookable) Export configuration values for external consumption
- [`importConfigData(Field $field, array $data): array`](method-___importconfigdata.md) (hookable) Convert an array of exported data to a format that will be understood internally
- [`getCompatibleFieldtypes(Field $field): Fieldtypes|null`](method-___getcompatiblefieldtypes.md) (hookable) Get an array of Fieldtypes that are compatible with this one
- [`sanitizeValue(Page $page, Field $field, string|int|WireArray|object $value): string|int|WireArray|object`](method-sanitizevalue.md) Sanitize the value for runtime storage and return it.
- [`formatValue(Page $page, Field $field, string|int|object $value): mixed`](method-___formatvalue.md) (hookable) Format the given value for output and return a string of the formatted value
- [`markupValue(Page $page, Field $field, mixed $value = null, string $property = ''): string|MarkupFieldtype`](method-___markupvalue.md) (hookable) Render a markup string of the value.
- [`getBlankValue(Page $page, Field $field): string|int|object|null`](method-getblankvalue.md) Return the blank value for this fieldtype, whether that is a blank string, zero value, blank object or array
- [`isDeleteValue(Page $page, Field $field, mixed $value): bool`](method-isdeletevalue.md) Is given value one that should cause the DB row(s) to be deleted rather than saved?
- [`isEmptyValue(Field $field, mixed $value): bool`](method-isemptyvalue.md) Return whether the given value is considered empty or not.
- [`wakeupValue(Page $page, Field $field, string|int|array $value): string|int|array|object`](method-___wakeupvalue.md) (hookable) Given a raw value (value as stored in database), return the value as it would appear in a Page object.
- [`sleepValue(Page $page, Field $field, string|int|float|array|object $value): string|int|float|array`](method-___sleepvalue.md) (hookable) Given an 'awake' value, as set by wakeupValue(), convert the value back to a basic type for storage in database.
- [`exportValue(Page $page, Field $field, string|int|float|array|object|null $value, array $options = array()): string|float|int|array`](method-___exportvalue.md) (hookable) Given a value, return an portable version of it as either a string, int, float or array
- [`getMatchQuery(PageFinderDatabaseQuerySelect $query, string $table, string $subfield, string $operator, mixed $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect`](method-getmatchquery.md) Get the database query that matches a Fieldtype table’s data with a given value.
- [`createField(Field $field): bool`](method-___createfield.md) (hookable) Create a new field table in the database.
- [`getDatabaseSchema(Field $field): array`](method-getdatabaseschema.md) Get the database schema for this field
- [`getFieldClass(array $a = array()): string`](method-getfieldclass.md) Get class name to use Field objects of this type (must be class that extends Field class)
- [`getSelectorInfo(Field $field, array $data = array()): array`](method-___getselectorinfo.md) (hookable) Return array with information about what properties and operators can be used with this field.
- [`loadPageField(Page $page, Field $field): mixed|null`](method-___loadpagefield.md) (hookable) Load the given page field from the database table and return the value.
- [`loadPageFieldFilter(Page $page, Field $field, Selectors|string|array $selector): mixed|null`](method-___loadpagefieldfilter.md) (hookable) Load the given page field from the database table and return a *filtered* value.
- [`getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadquery.md) Return the query used for loading all parts of the data from this field.
- [`getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL`](method-getloadqueryautojoin.md) Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.
- [`savePageField(Page $page, Field $field): bool`](method-___savepagefield.md) (hookable) Save the given field from given page to the database.
- [`deleteField(Field $field): bool`](method-___deletefield.md) (hookable) Delete the given field, which implies: drop the table used by the field.
- [`deletePageField(Page $page, Field $field): bool`](method-___deletepagefield.md) (hookable) Delete the given Field from the given Page.
- [`emptyPageField(Page $page, Field $field): bool`](method-___emptypagefield.md) (hookable) Empty out the DB table data for page field, but leave everything else in tact.
- [`emptyPageFieldTable(Page $page, Field $field): bool`](method-emptypagefieldtable.md) Empty DB table of page field
- [`replacePageField(Page $src, Page $dst, Field $field): bool`](method-___replacepagefield.md) (hookable) Move this field’s data from one page to another.
- [`deleteTemplateField(Template $template, Field $field): bool`](method-___deletetemplatefield.md) (hookable) Delete the given Field from all pages using the given template, without loading those pages.
- [`cloneField(Field $field): Field`](method-___clonefield.md) (hookable) Return a cloned copy of $field
- [`get(string $key): mixed`](method-get.md) Get a property from this Fieldtype’s data
- [`install()`](method-___install.md) (hookable) Install this Fieldtype, consistent with optional Module interface
- [`uninstall()`](method-___uninstall.md) (hookable) Uninstall this Fieldtype, consistent with optional Module interface
- [`upgrade($fromVersion, $toVersion)`](method-___upgrade.md) (hookable) Called when module version changes
- [`__toString()`](method-__tostring.md) The string value of Fieldtype is always the Fieldtype's name.
