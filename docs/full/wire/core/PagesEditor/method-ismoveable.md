# $pagesEditor->isMoveable(Page $page, Page $oldParent, Page $newParent, &$reason): bool

Source: `wire/core/PagesEditor.php`

Return whether given Page is moveable from $oldParent to $newParent

## Arguments

- `$page` `Page` Page to move
- `$oldParent` `Page` Current/old parent page
- `$newParent` `Page` New requested parent page
- `$reason` `string` Populated with reason why page is not moveable, if return value is false.

## Return value

bool
