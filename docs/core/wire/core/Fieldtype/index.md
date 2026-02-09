# Fieldtype

Source: `wire/core/Fieldtype.php`

ProcessWire Fieldtype Base

Abstract base class from which all Fieldtype modules are descended from.

Fieldtype is a module type used to represent a type of field. All Fieldtype modules descend from this.
Almost all methods in a Fieldtype are primarily of concern to module developers, as Fieldtype modules do not
have a public API (most of the time). Instead, they provide methods used by `Page` and `Field` objects (and related)
to work with the field data. Most Fieldtype modules only need to implement a few methods like
`Fieldtype::sanitizeValue()` (which is required) and `Fieldtype::getDatabaseSchema()`, as the default implementation
of most other methods provided in this Fieldtype class accounts for most situations already.



Hookable methods
================

- [getConfigInputfields(Field $field): InputfieldWrapper](method-___getconfiginputfields.md)

- [getConfigAdvancedInputfields(Field $field): InputfieldWrapper](method-___getconfigadvancedinputfields.md)

- [getConfigArray(Field $field): array](method-___getconfigarray.md)

- [getConfigAllowContext(Field $field): array](method-___getconfigallowcontext.md)

- [exportConfigData(Field $field, array $data): array](method-___exportconfigdata.md)

- [importConfigData(Field $field, array $data): array](method-___importconfigdata.md)

- [getCompatibleFieldtypes(Field $field): Fieldtypes|null](method-___getcompatiblefieldtypes.md)

- [formatValue(Page $page, Field $field, $value): mixed](method-___formatvalue.md)

- [markupValue(Page $page, Field $field, $value = null, $property = ''): string|MarkupFieldtype](method-___markupvalue.md)

- [wakeupValue(Page $page, Field $field, $value): mixed](method-___wakeupvalue.md)

- [sleepValue(Page $page, Field $field, $value): string|int|array](method-___sleepvalue.md)

- [exportValue(Page $page, Field $field, $value, array $options = array(): string|float|int|array](method-___exportvalue.md) )

- importValue(Page $page, Field $field, $value, array $options = array(): string|float|int|array|object )

- [createField(Field $field): bool](method-___createfield.md)

- [getSelectorInfo(Field $field, array $data = array(): array](method-___getselectorinfo.md) )

- [loadPageField(Page $page, Field $field): mixed|null](method-___loadpagefield.md)

- [loadPageFieldFilter(Page $page, Field $field, $selector): mixed|null](method-___loadpagefieldfilter.md)

- [savePageField(Page $page, Field $field): bool](method-___savepagefield.md)

- [deleteField(Field $field): bool](method-___deletefield.md)

- [deletePageField(Page $page, Field $field): bool](method-___deletepagefield.md)

- [emptyPageField(Page $page, Field $field): bool](method-___emptypagefield.md)

- [replacePageField(Page $src, Page $dst, Field $field): bool](method-___replacepagefield.md)

- [deleteTemplateField(Template $template, Field $field): bool](method-___deletetemplatefield.md)

- [cloneField(Field $field): Field](method-___clonefield.md)

- renamedField(Field $field, $prevName): void

- savedField(Field $field): void

- saveFieldReady(Field $field): void

- [install(): void](method-___install.md)

- [uninstall(): void](method-___uninstall.md)

- getFieldSetups(): array

- $name: string Name of Fieldtype module.

- $shortName: string Short name of Fieldtype, which excludes the "Fieldtype" prefix.

- $longName: string Long name of Fieldtype, which is typically the module title.

Methods:
Method: [getInputfield()](method-getinputfield.md)
Method: [getConfigInputfields()](method-___getconfiginputfields.md) (hookable)
Method: [getConfigArray()](method-___getconfigarray.md) (hookable)
Method: [getConfigAllowContext()](method-___getconfigallowcontext.md) (hookable)
Method: [getConfigAdvancedInputfields()](method-___getconfigadvancedinputfields.md) (hookable)
Method: [exportConfigData()](method-___exportconfigdata.md) (hookable)
Method: [importConfigData()](method-___importconfigdata.md) (hookable)
Method: [getCompatibleFieldtypes()](method-___getcompatiblefieldtypes.md) (hookable)
Method: [sanitizeValue()](method-sanitizevalue.md)
Method: [formatValue()](method-___formatvalue.md) (hookable)
Method: [markupValue()](method-___markupvalue.md) (hookable)
Method: [getBlankValue()](method-getblankvalue.md)
Method: [isDeleteValue()](method-isdeletevalue.md)
Method: [isEmptyValue()](method-isemptyvalue.md)
Method: [wakeupValue()](method-___wakeupvalue.md) (hookable)
Method: [sleepValue()](method-___sleepvalue.md) (hookable)
Method: [exportValue()](method-___exportvalue.md) (hookable)
Method: [getMatchQuery()](method-getmatchquery.md)
Method: [createField()](method-___createfield.md) (hookable)
Method: [getDatabaseSchema()](method-getdatabaseschema.md)
Method: [getFieldClass()](method-getfieldclass.md)
Method: [getSelectorInfo()](method-___getselectorinfo.md) (hookable)
Method: [loadPageField()](method-___loadpagefield.md) (hookable)
Method: [loadPageFieldFilter()](method-___loadpagefieldfilter.md) (hookable)
Method: [getLoadQuery()](method-getloadquery.md)
Method: [getLoadQueryAutojoin()](method-getloadqueryautojoin.md)
Method: [savePageField()](method-___savepagefield.md) (hookable)
Method: [deleteField()](method-___deletefield.md) (hookable)
Method: [deletePageField()](method-___deletepagefield.md) (hookable)
Method: [emptyPageField()](method-___emptypagefield.md) (hookable)
Method: [emptyPageFieldTable()](method-emptypagefieldtable.md)
Method: [replacePageField()](method-___replacepagefield.md) (hookable)
Method: [deleteTemplateField()](method-___deletetemplatefield.md) (hookable)
Method: [cloneField()](method-___clonefield.md) (hookable)
Method: [get()](method-get.md)
Method: [install()](method-___install.md) (hookable)
Method: [uninstall()](method-___uninstall.md) (hookable)
Method: [upgrade()](method-___upgrade.md) (hookable)
Method: [__toString()](method-__tostring.md)
