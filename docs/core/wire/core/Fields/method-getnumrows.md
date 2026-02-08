# $fields->getNumRows(Field $field, array $options = array()): int|array

Source: `wire/core/Fields.php`

Return a count of database rows populated the given field

## Arguments

- Field $field
- array $options Optionally specify any of the following options: - `template` (Template|int|string): Specify a Template object, ID or name to isolate returned rows specific to pages using that template. - `page` (Page|int|string): Specify a Page object, ID or path to isolate returned rows specific to that page. - `countPages` (bool): Specify boolean true to make it return a page count rather than a row count (default=false). There will only be potential difference between rows and pages counts with multi-value fields. - `getPageIDs` (bool): Specify boolean true to make it return an array of matching Page IDs rather than a count (overrides countPages).

## Return value

int|array Returns array only if getPageIDs option set, otherwise returns a count of rows.

## Throws

- WireException If given option for page or template doesn't resolve to actual page/template.
