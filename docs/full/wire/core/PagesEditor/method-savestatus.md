# $pagesEditor->saveStatus(Page $page): bool

Source: `wire/core/PagesEditor.php`

Silently save whatever the given Page’s status currently is

This action does not update the Page modified date.

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->saveStatus($page);

// usage with all arguments
$bool = $pagesEditor->saveStatus(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `bool`

## Since

3.0.146
