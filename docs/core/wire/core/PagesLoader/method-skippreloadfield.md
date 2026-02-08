# $pagesLoader->skipPreloadField(Page $page, Field $field, array $options): string

Source: `wire/core/PagesLoader.php`

Skip preloading of this field or fieldtype?

Returns populated string with reason if yes, or blank string if no.

## Usage

~~~~~
// basic usage
$string = $pagesLoader->skipPreloadField($page, $field, $options);

// usage with all arguments
$string = $pagesLoader->skipPreloadField(Page $page, Field $field, array $options);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$options` `array`

## Return value

- `string`
