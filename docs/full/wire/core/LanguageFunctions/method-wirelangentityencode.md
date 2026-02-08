# $languageFunctions->wireLangEntityEncode($value = ''): bool|int|string|null

Source: `wire/core/LanguageFunctions.php`

Set entity encoding state for language translation function calls

The function affects behavior of future `__()`, `_x()` and `_n()` calls.

The following can be used for the `$value` argument:

- `true` (bool): Entity encoding ON
- `false` (bool): Entity encoding OFF
- `1` (int): Entity encode only if not already
- `null` (null): Entity encoding undefined

To get current entity encoding state, call this function with no arguments.

## Arguments

- `$value` (optional) `bool|int|string|null`

## Return value

bool|int|string|null

## Since

3.0.154 Versions 3.0.125 to 3.0.153 can use __(true, 'entityEncode', $value);
