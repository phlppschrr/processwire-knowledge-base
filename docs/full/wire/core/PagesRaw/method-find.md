# $pagesRaw->find($selector, $field = '', $options = array()): array

Source: `wire/core/PagesRaw.php`

Find pages and return raw data from them in a PHP array

## Arguments

- string|array|Selectors $selector
- string|array|Field $field Name of field/property to get, or array of them, CSV string, or omit to get all (default='') - Optionally use associative array to rename fields in returned value, i.e. `['title' => 'label']` returns 'title' as 'label' in return value. - Specify `parent.field_name` or `parent.parent.field_name`, etc. to return values from parent(s). 3.0.193+ - Specify `references` or `references.field_name`, etc. to also return values from pages referencing found pages. 3.0.193+ - Specify `meta` or `meta.name` to also return values from page meta data. 3.0.193+
- array $options See options for Pages::find - `objects` (bool): Use objects rather than associative arrays? (default=false) - `entities` (bool|array): Entity encode string values? True, or specify array of field names. (default=false) - `nulls` (bool): Populate nulls for field values that are not present, rather than omitting them? (default=false) 3.0.198+ - `indexed` (bool): Index by page ID? (default=true) - `flat` (bool|string): Flatten return value as `["field.subfield" => "value"]` rather than `["field" => ["subfield" => "value"]]`? Optionally specify field delimiter, otherwise a period `.` will be used as the delimiter. (default=false) 3.0.193+ - Note the `objects` and `flat` options are not meant to be used together.

## Return value

array

## Meta

- @since 3.0.172
