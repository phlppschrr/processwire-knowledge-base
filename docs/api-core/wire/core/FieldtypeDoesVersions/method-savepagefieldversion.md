# $fieldtypeDoesVersions->savePageFieldVersion(Page $page, Field $field, $version): bool

Source: `wire/core/Interfaces.php`

Save version of given page field

## Usage

~~~~~
// basic usage
$bool = $fieldtypeDoesVersions->savePageFieldVersion($page, $field, $version);

// usage with all arguments
$bool = $fieldtypeDoesVersions->savePageFieldVersion(Page $page, Field $field, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$version` `int`

## Return value

- `bool`
