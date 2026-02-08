# $wireInput->httpUrl($options = array()): string

Source: `wire/core/WireInput.php`

Get the http URL that initiated the current request, including scheme, URL segments and page numbers

- This should be the same as `$page->httpUrl` except that it includes URL segments and page numbers, when present.

- Note that this does not include query string unless requested (see arguments).

- WARNING: if query string requested, it can contain undefined/unsanitized user input. If you use it for output
  make sure that you entity encode first (by running through `$sanitizer->entities()` for instance).

~~~~~~
$url = $input->httpUrl();
$url = $sanitizer->entities($url); // entity encode for output
echo "You accessed this page at: $url";
~~~~~~

## Arguments

- `$options` (optional) `array|bool` Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array: - `withQueryString` (bool): Include the query string as well? (if present, default=false) - `page` (Page): Page object to use, if different from $page (default=$page)

## Return value

string

## See also

- [WireInput::url()](method-url.md)
- [Page::httpUrl()](../Page/method-httpurl.md)
