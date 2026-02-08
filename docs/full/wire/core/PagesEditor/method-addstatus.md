# $pagesEditor->addStatus(Page $page, $status): bool

Source: `wire/core/PagesEditor.php`

Silently add status flag to a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.

## Arguments

- Page $page
- int $status Use Page::status* constants

## Return value

bool

## See also

- [PagesEditor::setStatus()](index.md)
- [PagesEditor::removeStatus()](method-removestatus.md)

## Meta

- @since 3.0.146
