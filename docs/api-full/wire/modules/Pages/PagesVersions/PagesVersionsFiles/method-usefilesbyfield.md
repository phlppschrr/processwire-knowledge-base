# $pagesVersionsFiles->useFilesByField(Page $page, array $names = []): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Copy/restore files individually by field for given page?

- Return true if files should be copied/restored individually by field.
- Returns false if entire page directory should be copied/restored at once.

## Usage

~~~~~
// basic usage
$bool = $pagesVersionsFiles->useFilesByField($page);

// usage with all arguments
$bool = $pagesVersionsFiles->useFilesByField(Page $page, array $names = []);
~~~~~

## Arguments

- `$page` `Page`
- `$names` (optional) `Field[]|string[]` Optionally limit check to these fields

## Return value

- `bool`
