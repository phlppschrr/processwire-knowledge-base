# $pagesTrash->restore(Page $page, $save = true): bool

Source: `wire/core/PagesTrash.php`

Restore a page from the trash back to a non-trash state

Note that this method assumes already have set a new parent, but have not yet saved.
If you do not set a new parent, then it will restore to the original parent, when possible.

## Arguments

- `$page` `Page`
- `$save` (optional) `bool` Set to false if you only want to prep the page for restore (i.e. being saved elsewhere)

## Return value

bool
