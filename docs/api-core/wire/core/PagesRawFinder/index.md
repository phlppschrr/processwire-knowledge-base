# PagesRawFinder

Source: `wire/core/PagesRaw.php`

Inherits: `Wire`

ProcessWire Pages Raw Finder

Methods:
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`init($selector, string|array|Field $field, array $options)`](method-init.md)
- [`find(string|array|Selectors $selector, string|Field|int|array $field = '', array $options = array()): array`](method-find.md) Find pages and return raw data from them in a PHP array
- [`splitFields()`](method-splitfields.md) Split requestFields into native and custom field arrays
- [`findNativeFields()`](method-findnativefields.md) Find raw native fields
- [`findCustom()`](method-findcustom.md) Gateway to finding custom fields whether specific, all or none
- [`findCustomField(Field $field, array $cols)`](method-findcustomfield.md) Find raw custom field
- [`findCustomFieldtypeOptions(Field $field, array $cols, bool $getArray, bool $getAllCols)`](method-findcustomfieldtypeoptions.md) Find custom Options fieldtype columns
- [`findCustomFieldtypePage(Field $field, string $fieldName, array $pageRefCols)`](method-findcustomfieldtypepage.md) Find and apply values for Page reference fields
- [`findCustomAll()`](method-findcustomall.md) Find/populate all custom fields
- [`findParent()`](method-findparent.md) Find and apply values for parent.[field]
- [`findTemplate()`](method-findtemplate.md) Find and apply values for template.[property]
- [`findRuntime()`](method-findruntime.md) Find runtime generated fields
- [`findMeta(array $names)`](method-findmeta.md) Populate 'meta' to (form pages_meta table) to the result values
- [`findReferences(array $colNames)`](method-findreferences.md) Populate a 'references' to the raw results that includes other pages referencing the found ones
- [`findIDs(array|string|Selectors $selector, bool|string $verbose, array $options = array()): array`](method-findids.md) Front-end to pages.findIDs that optionally accepts array of page IDs
- [`objects(array &$values)`](method-objects.md) Convert associative arrays to objects
- [`entities(mixed &$value)`](method-entities.md) Apply entity encoding to all strings in given value, recursively
- [`renames(array &$values)`](method-renames.md) Rename fields on request
- [`ids(bool $csv = false): array|string`](method-ids.md) Get or convert $this->ids to/from CSV
- [`setIds(array $ids)`](method-setids.md) Set the found IDs and init the $this->values array
- [`flattenValues(array $values, string $prefix = '', string $delimiter = '.'): array`](method-flattenvalues.md) Flatten multidimensional values from array['a']['b']['c'] to array['a.b.c']
- [`populateNullValues(&$values)`](method-populatenullvalues.md) Populate null values for requested fields that were not present (the 'nulls' option)
- [`processRequestFieldsArray(array $values, string $prefix = '')`](method-processrequestfieldsarray.md) Process given array of values to populate $this->requestFields and $this->renameFields
