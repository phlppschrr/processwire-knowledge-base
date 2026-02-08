# $fieldtypeDoesVersions->restorePageFieldVersion(Page $page, Field $field, $version): bool

Source: `wire/core/Interfaces.php`

Restore version of given page field to live page

## Usage

~~~~~
// basic usage
$bool = $fieldtypeDoesVersions->restorePageFieldVersion($page, $field, $version);

// usage with all arguments
$bool = $fieldtypeDoesVersions->restorePageFieldVersion(Page $page, Field $field, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$version` `int`

## Return value

- `bool`
