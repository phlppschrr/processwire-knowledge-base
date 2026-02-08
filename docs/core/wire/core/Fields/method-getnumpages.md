# $fields->getNumPages(Field $field, array $options = array()): int|array

Source: `wire/core/Fields.php`

Return a count of pages containing populated values for the given field

## Usage

~~~~~
// basic usage
$int = $fields->getNumPages($field);

// usage with all arguments
$int = $fields->getNumPages(Field $field, array $options = array());
~~~~~

## Arguments

- `$field` `Field`
- `$options` (optional) `array` Optionally specify one of the following options: - `template` (template|int|string): Specify a Template object, ID or name to isolate returned rows specific to pages using that template. - `page` (Page|int|string): Specify a Page object, ID or path to isolate returned rows specific to that page. - `getPageIDs` (bool): Specify boolean true to make it return an array of matching Page IDs rather than a count.

## Return value

- `int|array` Returns array only if getPageIDs option set, otherwise returns count of pages.

## Exceptions

- `WireException` If given option for page or template doesn't resolve to actual page/template.
