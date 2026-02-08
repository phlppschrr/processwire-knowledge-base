# $wireInput->url($options = array()): string

Source: `wire/core/WireInput.php`

Get the URL that initiated the current request, including URL segments and page numbers

- This should be the same as `$page->url` except that it includes URL segments and page numbers, when present.

- Note that this does not include query string unless requested (see arguments).

- WARNING: if query string requested, it can contain undefined/unsanitized user input. If you use it for output
  make sure that you entity encode first (by running through `$sanitizer->entities()` for instance).

~~~~~~
$url = $input->url();
$url = $sanitizer->entities($url); // entity encode for output
echo "You accessed this page at: $url";
~~~~~~

## Arguments

- array|bool $options Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array: - `withQueryString` (bool): Include the query string as well? (if present, default=false) - `page` (Page): Page object to use, if different from $page (default=$page) - `pageNum` (int): Override current pagination number with this one, 1 to exclude pageNum, 0 for no override (default=0). 3.0.169+

## Return value

string

## See also

- [WireInput::httpUrl()](method-httpurl.md)
- [Page::url()](../Page/method-url.md)
