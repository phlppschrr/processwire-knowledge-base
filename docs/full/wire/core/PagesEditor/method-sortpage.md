# PagesEditor::sortPage()

Source: `wire/core/PagesEditor.php`

Set page $sort value and increment siblings having same or greater sort value

- This method is primarily applicable if configured sortfield is manual “sort” (or “none”).
- This is typically used after a move, sort, clone or delete operation.


@param Page $page Page that you want to set the sort value for

@param int|null $sort New sort value for page or null to pull from $page->sort

@param bool $after If another page already has the sort, make $page go after it rather than before it? (default=false)

@throws WireException if given invalid arguments

@return int Number of sibling pages that had to have sort adjusted
