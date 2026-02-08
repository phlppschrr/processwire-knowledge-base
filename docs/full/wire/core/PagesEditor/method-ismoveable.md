# $pagesEditor->isMoveable(Page $page, Page $oldParent, Page $newParent, &$reason): bool

Source: `wire/core/PagesEditor.php`

Return whether given Page is moveable from $oldParent to $newParent

## Arguments

- Page $page Page to move
- Page $oldParent Current/old parent page
- Page $newParent New requested parent page
- string $reason Populated with reason why page is not moveable, if return value is false.

## Return value

bool
