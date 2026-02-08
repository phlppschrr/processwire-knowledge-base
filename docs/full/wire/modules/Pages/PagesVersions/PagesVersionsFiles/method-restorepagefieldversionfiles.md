# $pagesVersionsFiles->restorePageFieldVersionFiles(Page $page, Field $field, $version): int

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Restore files for given field from version into live $page

## Usage

~~~~~
// basic usage
$int = $pagesVersionsFiles->restorePageFieldVersionFiles($page, $field, $version);

// usage with all arguments
$int = $pagesVersionsFiles->restorePageFieldVersionFiles(Page $page, Field $field, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$version` `int`

## Return value

- `int`
