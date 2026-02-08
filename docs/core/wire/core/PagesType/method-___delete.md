# $pagesType->delete(Page $page, $recursive = false): bool

Source: `wire/core/PagesType.php`

Permanently delete a page and its fields.

Unlike `$pages->trash()`, pages deleted here are not restorable.

If you attempt to delete a page with children, and don’t specifically set the `$recursive` argument to `true`, then
this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

Hook note:
If you want to hook this method, please hook the `deleteReady`, `deleted`, or `Pages::delete` method
instead, as hooking this method will not hook relevant pages deleted directly through $pages->delete().

## Usage

~~~~~
// basic usage
$bool = $pagesType->delete($page);

// usage with all arguments
$bool = $pagesType->delete(Page $page, $recursive = false);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$pagesType->delete()`

## Arguments

- `$page` `Page`
- `$recursive` (optional) `bool` If set to true, then this will attempt to delete all children too.

## Return value

- `bool`

## Exceptions

- `WireException`
