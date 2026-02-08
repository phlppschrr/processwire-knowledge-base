# $pageComparison->_if(Page $page, $key, $yes = '', $no = ''): mixed|string|bool

Source: `wire/core/PageComparison.php`

If value is available for $key return or call $yes condition (with optional $no condition)

This merges the capabilities of an if() statement, get() and getMarkup() methods in one,
plus some useful PW type-specific logic, providing a useful output shortcut.

See phpdoc in `Page::if()` for full details.

## Arguments

- Page $page
- string|bool|int $key Name of field to check, selector string to evaluate, or boolean/int to evalute
- string|callable|mixed $yes If value for $key is present, return or call this
- string|callable|mixed $no If value for $key is empty, return or call this

## Return value

mixed|string|bool

## Meta

- @since 3.0.126
