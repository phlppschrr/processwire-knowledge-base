# $pagesEditor->removeStatus(Page $page, $status): bool

Source: `wire/core/PagesEditor.php`

Silently remove status flag from a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.

## Arguments

- `$page` `Page`
- `$status` `int` Use Page::status* constants

## Return value

bool

## See also

- [PagesEditor::setStatus()](index.md)
- [PagesEditor::addStatus()](method-addstatus.md)
- [PagesEditor::saveStatus()](method-savestatus.md)

## Since

3.0.146
