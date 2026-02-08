# $pagesTrash->trash(Page $page, $save = true): bool

Source: `wire/core/PagesTrash.php`

Move a page to the trash

If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.

## Arguments

- Page $page
- bool $save Set to false if you will perform the save() call, as is the case when called from the Pages::save() method.

## Return value

bool

## Throws

- WireException
