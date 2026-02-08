# $pagesEditor->isDeleteable(Page $page, $throw = false): bool

Source: `wire/core/PagesEditor.php`

Is the given page deleteable from the API?

Note: this does not account for user permission checking.
It only checks if the page is in a state to be deleteable via the API.

## Arguments

- `$page` `Page`
- `$throw` (optional) `bool` Throw WireException with additional details?

## Return value

bool True if deleteable, False if not

## Throws

- WireException If requested to do so via $throw argument
