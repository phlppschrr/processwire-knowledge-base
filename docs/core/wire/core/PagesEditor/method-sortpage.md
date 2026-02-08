# $pagesEditor->sortPage(Page $page, $sort = null, $after = false): int

Source: `wire/core/PagesEditor.php`

Set page $sort value and increment siblings having same or greater sort value

- This method is primarily applicable if configured sortfield is manual “sort” (or “none”).
- This is typically used after a move, sort, clone or delete operation.

## Arguments

- Page $page Page that you want to set the sort value for
- int|null $sort New sort value for page or null to pull from $page->sort
- bool $after If another page already has the sort, make $page go after it rather than before it? (default=false)

## Return value

int Number of sibling pages that had to have sort adjusted

## Throws

- WireException if given invalid arguments
