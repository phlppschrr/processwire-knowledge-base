# PagesRawFinder

Source: `wire/core/PagesRaw.php`

Inherits: `Wire`

ProcessWire Pages Raw Finder

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`init($selector, string|array|Field $field, array $options)`](method-init.md)
- [`find(string|array|Selectors $selector, string|Field|int|array $field = '', array $options = array()): array`](method-find.md)
- [`splitFields()`](method-splitfields.md)
- [`findNativeFields()`](method-findnativefields.md)
- [`findCustom()`](method-findcustom.md)
- [`findCustomField(Field $field, array $cols)`](method-findcustomfield.md)
- [`findCustomFieldtypeOptions(Field $field, array $cols, bool $getArray, bool $getAllCols)`](method-findcustomfieldtypeoptions.md)
- [`findCustomFieldtypePage(Field $field, string $fieldName, array $pageRefCols)`](method-findcustomfieldtypepage.md)
- [`findCustomAll()`](method-findcustomall.md)
- [`findParent()`](method-findparent.md)
- [`findTemplate()`](method-findtemplate.md)
- [`findRuntime()`](method-findruntime.md)
- [`findMeta(array $names)`](method-findmeta.md)
- [`findReferences(array $colNames)`](method-findreferences.md)
- [`findIDs(array|string|Selectors $selector, bool|string $verbose, array $options = array()): array`](method-findids.md)
- [`objects(array &$values)`](method-objects.md)
- [`entities(mixed &$value)`](method-entities.md)
- [`renames(array &$values)`](method-renames.md)
- [`ids(bool $csv = false): array|string`](method-ids.md)
- [`setIds(array $ids)`](method-setids.md)
- [`flattenValues(array $values, string $prefix = '', string $delimiter = '.'): array`](method-flattenvalues.md)
- [`populateNullValues(&$values)`](method-populatenullvalues.md)
- [`processRequestFieldsArray(array $values, string $prefix = '')`](method-processrequestfieldsarray.md)
