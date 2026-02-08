# PagesEditor::isMoveable()

Source: `wire/core/PagesEditor.php`

Return whether given Page is moveable from $oldParent to $newParent


@param Page $page Page to move

@param Page $oldParent Current/old parent page

@param Page $newParent New requested parent page

@param string $reason Populated with reason why page is not moveable, if return value is false.

@return bool
