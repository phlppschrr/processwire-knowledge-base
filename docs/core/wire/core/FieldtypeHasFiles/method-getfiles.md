# $fieldtypeHasFiles->getFiles(Page $page, Field $field): array

Source: `wire/core/Interfaces.php`

Get array of full path/file for all files managed by given page and field

## Usage

~~~~~
// basic usage
$array = $fieldtypeHasFiles->getFiles($page, $field);

// usage with all arguments
$array = $fieldtypeHasFiles->getFiles(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Return value

- `array`
