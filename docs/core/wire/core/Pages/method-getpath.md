# $pages->getPath($id, $options = array()): string

Source: `wire/core/Pages.php`

Given an ID, return a path to a page, without loading the actual page

1. Always returns path in default language, unless a language argument/option is specified.
2. Path may be different from 'url' as it doesn't include the root URL at the beginning.
3. In most cases, it's preferable to use `$page->path()` rather than this method. This method is
   here just for cases where a path is needed without loading the page.
4. It's possible for there to be `Page::path()` hooks, and this method completely bypasses them,
   which is another reason not to use it unless you know such hooks aren't applicable to you.

~~~~~
// Get the path for page having ID 1234
$path = $pages->getPath(1234);
echo "Path for page 1234 is: $path";
~~~~~

## Arguments

- `$id` `int|Page` ID of the page you want the path to
- `$options` (optional) `null|array|Language|int|string` Specify $options array or Language object, id or name. Allowed options include: - `language` (int|string|anguage): To retrieve in non-default language, specify language object, ID or name (default=null) - `useCache` (bool): Allow pulling paths from already loaded pages? (default=true) - `usePagePaths` (bool): Allow pulling paths from PagePaths module, if installed? (default=true)

## Return value

string Path to page or blank on error/not-found.

## See also

- [Page::path()](../Page/method-path.md)

## Since

3.0.6
