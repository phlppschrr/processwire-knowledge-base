# PageComparison::_if()

Source: `wire/core/PageComparison.php`

If value is available for $key return or call $yes condition (with optional $no condition)

This merges the capabilities of an if() statement, get() and getMarkup() methods in one,
plus some useful PW type-specific logic, providing a useful output shortcut.

See phpdoc in `Page::if()` for full details.

@param Page $page

@param string|bool|int $key Name of field to check, selector string to evaluate, or boolean/int to evalute

@param string|callable|mixed $yes If value for $key is present, return or call this

@param string|callable|mixed $no If value for $key is empty, return or call this

@return mixed|string|bool

@since 3.0.126
