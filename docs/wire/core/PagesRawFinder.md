# PagesRawFinder

Source: `wire/core/PagesRaw.php`

ProcessWire Pages Raw Finder

## __construct()

Construct

@param Pages $pages

## init()

@param string|int|array|Selectors

@param string|array|Field $field

@param array $options

## find()

Find pages and return raw data from them in a PHP array

How to use the `$field` argument:

- If you provide an array for $field then it will return an array for each page, indexed by
  the field names you requested.

- If you provide a string (field name) or Field object, then it will return an array with
  the values of the 'data' column of that field.

- You may request field name(s) like `field.subfield` to retrieve a specific column/subfield.

- You may request field name(s) like `field.*` to return all columns/subfields for `field`,
  in this case, an associative array value will be returned for each page.

- If you specify an associative array for the $field argument, you can optionally rename
  fields in returned value. For example, if you wanted to get the 'title' field but return
  it as a field named 'headline' in the return value, you would specify the array
  `[ 'title' => 'headline' ]` for the $field argument. (3.0.176+)

@param string|array|Selectors $selector

@param string|Field|int|array $field Field/property name or array of of them

@param array $options See options for Pages::find

@return array

@since 3.0.172

## splitFields()

Split requestFields into native and custom field arrays

Populates $this->nativeFields, $this->customFields, $this->customCols

## findNativeFields()

Find raw native fields

## findCustom()

Gateway to finding custom fields whether specific, all or none

## findCustomField()

Find raw custom field

@param Field $field

@param array $cols

@throws WireException

## findCustomFieldtypeOptions()

Find custom Options fieldtype columns

Options field stores its values/titles in separate table.

To use, specify one of the following in the fields to get (where field_name is an options field name):

- `field_name` to just include the IDs of the selected options for each page.
- `field_name.*` to include all available properties for selected options for each page.
- `field_name.title` to include the selected option titles.
- `field_name.value` to include the selected option values.

@param Field $field

@param array $cols

@param bool $getArray

@param bool $getAllCols

@since 3.0.193

## findCustomFieldtypePage()

Find and apply values for Page reference fields

@param Field $field

@param string $fieldName

@param array $pageRefCols

## findCustomAll()

Find/populate all custom fields

## findParent()

Find and apply values for parent.[field]

@since 3.0.193

## findTemplate()

Find and apply values for template.[property]

@since 3.0.206

## findRuntime()

Find runtime generated fields

@since 3.0.193

## findMeta()

Populate 'meta' to (form pages_meta table) to the result values

@param array $names

@since 3.0.193

## findReferences()

Populate a 'references' to the raw results that includes other pages referencing the found ones

To use this specify `references` in the fields to return. Or, to get page references that are
indexed by field name, specify `references.field` instead. To get something more than the id
of page references, specify properties or fields as `references.field_name` replacing `field_name`
with a page property or field name, i.e. `references.title`.

@param array $colNames

@since 3.0.193

## findIDs()

Front-end to pages.findIDs that optionally accepts array of page IDs

@param array|string|Selectors $selector

@param bool|string $verbose One of true, false, or '*'

@param array $options

@return array

@throws WireException

## objects()

Convert associative arrays to objects

@param array $values

## entities()

Apply entity encoding to all strings in given value, recursively

@param mixed $value

## renames()

Rename fields on request

@param array $values

@since 3.0.167

## ids()

Get or convert $this->ids to/from CSV

The point of this is just to minimize the quantity of copies of IDs we are keeping around.
In case the quantity gets to be huge, it'll be more memory friendly.

@param bool $csv

@return array|string

## setIds()

Set the found IDs and init the $this->values array

@param array $ids

@since 3.0.193

## flattenValues()

Flatten multidimensional values from array['a']['b']['c'] to array['a.b.c']

@param array $values

@param string $prefix Prefix for recursive use

@param string $delimiter

@return array

@since 3.0.193

## populateNullValues()

Populate null values for requested fields that were not present (the 'nulls' option)

Applies only if specific fields were requested.

@var array $values

@since 3.0.198

## processRequestFieldsArray()

Process given array of values to populate $this->requestFields and $this->renameFields

@param array $values

@param string $prefix Prefix for recursive use

@since 3.0.194
