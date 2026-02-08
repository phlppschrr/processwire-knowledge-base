# $pagesVersionsFiles->copyPageFieldVersionFiles(Page $page, Field $field, $version): int

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Copy files for given $page and field into version directory

## Usage

~~~~~
// basic usage
$int = $pagesVersionsFiles->copyPageFieldVersionFiles($page, $field, $version);

// usage with all arguments
$int = $pagesVersionsFiles->copyPageFieldVersionFiles(Page $page, Field $field, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$version` `int`

## Return value

- `int`
