# $pagesVersionsFiles->useFilesByField(Page $page, array $names = []): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Copy/restore files individually by field for given page?

- Return true if files should be copied/restored individually by field.
- Returns false if entire page directory should be copied/restored at once.

## Arguments

- `$page` `Page`
- `$names` (optional) `Field[]|string[]` Optionally limit check to these fields

## Return value

bool
