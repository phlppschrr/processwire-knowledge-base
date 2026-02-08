# $pagesVersions->deletePageFieldVersion(Page $page, Field $field, $version): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete a page field version

This should not be called independently of deletePageVersion() as this
method does not delete any files connected to the version.

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$version` `int`

## Return value

bool
