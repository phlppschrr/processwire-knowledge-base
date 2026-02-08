# PagesRaw

Source: `wire/core/PagesRaw.php`

ProcessWire Pages Raw Tools

Pages Raw
$pages->raw
Methods for finding and loading raw page data

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## find()

Find pages and return raw data from them in a PHP array

@param string|array|Selectors $selector

@param string|array|Field $field Name of field/property to get, or array of them, CSV string, or omit to get all (default='')
 - Optionally use associative array to rename fields in returned value, i.e. `['title' => 'label']` returns 'title' as 'label' in return value.
 - Specify `parent.field_name` or `parent.parent.field_name`, etc. to return values from parent(s). 3.0.193+
 - Specify `references` or `references.field_name`, etc. to also return values from pages referencing found pages. 3.0.193+
 - Specify `meta` or `meta.name` to also return values from page meta data. 3.0.193+

@param array $options See options for Pages::find
 - `objects` (bool): Use objects rather than associative arrays? (default=false)
 - `entities` (bool|array): Entity encode string values? True, or specify array of field names. (default=false)
 - `nulls` (bool): Populate nulls for field values that are not present, rather than omitting them? (default=false) 3.0.198+
 - `indexed` (bool): Index by page ID? (default=true)
 - `flat` (bool|string): Flatten return value as `["field.subfield" => "value"]` rather than `["field" => ["subfield" => "value"]]`?
    Optionally specify field delimiter, otherwise a period `.` will be used as the delimiter. (default=false) 3.0.193+
 - Note the `objects` and `flat` options are not meant to be used together.

@return array

@since 3.0.172

## get()

Get page (no exclusions) and return raw data from it in a PHP array

@param string|array|Selectors $selector

@param string|Field|int|array $field Field/property name to get or array of them (or omit to get all)

@param array|bool $options See options for Pages::find
 - `objects` (bool): Use objects rather than associative arrays? (default=false)
 - `entities` (bool|array): Entity encode string values? True, or specify array of field names. (default=false)
 - `indexed` (bool): Index by page ID? (default=false)
 - `flat` (bool|string): Flatten return value as `["field.subfield" => "value"]` rather than `["field" => ["subfield" => "value"]]`?
    Optionally specify field delimiter, otherwise a period `.` will be used as the delimiter. (default=false) 3.0.193+

@return array

@since 3.0.172

## col()

Get native pages table column value for given page ID

This can only be used for native 'pages' table columns,
i.e. id, name, templates_id, status, parent_id, etc.

@param int|array $pageId Page ID or array of page IDs

@param string|array $col Column name you want to get

@return int|string|array|null Returns column value or array of column values if $pageId was an array.
  When array is returned, it is indexed by page ID.

@param array $options
 - `cache` (bool): Allow use of memory cache to retrieve column value when available? (default=true)
    Used only if $pageId is an integer (not used when array of page IDs).

@throws WireException

@since 3.0.190

## cols()

Get native pages table columns (plural) for given page ID

This can only be used for native 'pages' table columns,
i.e. id, name, templates_id, status, parent_id, etc.

@param int|array $pageId Page ID or array of page IDs

@param array|string $cols Names of columns to get or omit to get all columns

@param array $options
 - `cache` (bool): Allow use of memory cache to retrieve column value when available? (default=true)
    Used only if $pageId is an integer (not used when array of page IDs).

@return array Returns associative array on success or empty array if not found
  If $pageId argument was an array then it returns a page ID indexed array of
  associative arrays, one for each page.

@throws WireException

@since 3.0.190
