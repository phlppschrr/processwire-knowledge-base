# $pagesEditor->replace(Page $oldPage, Page $newPage): Page

Source: `wire/core/PagesEditor.php`

Replace one page with another (work in progress)

## Usage

~~~~~
// basic usage
$page = $pagesEditor->replace($oldPage, $newPage);

// usage with all arguments
$page = $pagesEditor->replace(Page $oldPage, Page $newPage);
~~~~~

## Arguments

- `$oldPage` `Page`
- `$newPage` `Page`

## Return value

- `Page`

## Exceptions

- `WireException`

## Since

3.0.189 But not yet available in public API
