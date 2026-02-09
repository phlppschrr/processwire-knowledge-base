# $pagesEditor->addStatus(Page $page, $status): bool

Source: `wire/core/PagesEditor.php`

Silently add status flag to a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->addStatus($page, $status);

// usage with all arguments
$bool = $pagesEditor->addStatus(Page $page, $status);
~~~~~

## Arguments

- `$page` `Page`
- `$status` `int` Use Page::status* constants

## Return value

- `bool`

## See Also

- [PagesEditor::setStatus()](index.md)
- [PagesEditor::removeStatus()](method-removestatus.md)

## Since

3.0.146
