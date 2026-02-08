# $pages->has($selector, $verbose = false): array|int

Source: `wire/core/Pages.php`

Is there any page that matches the given $selector in the system? (with no exclusions)

- This can be used as an “exists” type of method.
- Returns ID of first matching page if any exist, or 0 if none exist (returns array if `$verbose` is true).
- Like with the `get()` method, no pages are excluded, so an `include=all` is not necessary in selector.
- If you need to quickly check if something exists, this method is preferable to using a count() or get().

When `$verbose` option is used, an array is returned instead. Verbose return array includes page `id`,
`parent_id` and `templates_id` indexes.

## Arguments

- `$selector` `string|int|array|Selectors`
- `$verbose` (optional) `bool` Return verbose array with page id, parent_id, templates_id rather than just page id? (default=false)

## Return value

array|int

## See also

- [Pages::count()](method-count.md)
- [Pages::get()](method-get.md)

## Since

3.0.153
