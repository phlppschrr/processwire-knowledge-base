# $pagesEditor->delete(Page $page, $recursive = false, array $options = array()): bool|int

Source: `wire/core/PagesEditor.php`

Permanently delete a page and its fields.

Unlike trash(), pages deleted here are not restorable.

If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then
this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

## Arguments

- Page $page
- bool|array $recursive If set to true, then this will attempt to delete all children too. If you don't need this argument, optionally provide $options array instead.
- array $options Optional settings to change behavior: - `uncacheAll` (bool): Whether to clear memory cache after delete (default=false) - `recursive` (bool): Same as $recursive argument, may be specified in $options array if preferred.

## Return value

bool|int Returns true (success), or integer of quantity deleted if recursive mode requested.

## Throws

- WireException on fatal error
