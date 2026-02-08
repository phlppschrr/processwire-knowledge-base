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

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com


Hookable methods
================

@method InputfieldWrapper getConfigInputfields(Field $field)

@method InputfieldWrapper getConfigAdvancedInputfields(Field $field)

@method array getConfigArray(Field $field)

@method array getConfigAllowContext(Field $field)

@method array exportConfigData(Field $field, array $data)

@method array importConfigData(Field $field, array $data)

@method Fieldtypes|null getCompatibleFieldtypes(Field $field)

@method mixed formatValue(Page $page, Field $field, $value)

@method string|MarkupFieldtype markupValue(Page $page, Field $field, $value = null, $property = '')

@method mixed wakeupValue(Page $page, Field $field, $value)

@method string|int|array sleepValue(Page $page, Field $field, $value)

@method string|float|int|array exportValue(Page $page, Field $field, $value, array $options = array())

@method string|float|int|array|object importValue(Page $page, Field $field, $value, array $options = array())

@method bool createField(Field $field)

@method array getSelectorInfo(Field $field, array $data = array())

@method mixed|null loadPageField(Page $page, Field $field)

@method mixed|null loadPageFieldFilter(Page $page, Field $field, $selector)

@method bool savePageField(Page $page, Field $field)

@method bool deleteField(Field $field)

@method bool deletePageField(Page $page, Field $field)

@method bool emptyPageField(Page $page, Field $field)

@method bool replacePageField(Page $src, Page $dst, Field $field)

@method bool deleteTemplateField(Template $template, Field $field)

@method Field cloneField(Field $field)

@method void renamedField(Field $field, $prevName)

@method void savedField(Field $field)

@method void saveFieldReady(Field $field)

@method void install()

@method void uninstall()

@method array getFieldSetups()

@property string $name Name of Fieldtype module.

@property string $shortName Short name of Fieldtype, which excludes the "Fieldtype" prefix.

@property string $longName Long name of Fieldtype, which is typically the module title.

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
