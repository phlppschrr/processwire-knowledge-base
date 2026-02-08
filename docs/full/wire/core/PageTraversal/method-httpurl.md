# $pageTraversal->httpUrl(Page $page, $options = array()): string

Source: `wire/core/PageTraversal.php`

Returns the URL to the page, including scheme and hostname

- This method is just like the `$page->url()` method except that it also includes scheme and hostname.

- This method can also be accessed at the property `$page->httpUrl` (without parenthesis).

- It is desirable to use this method when some page templates require https while others don't.
  This ensures local links will always point to pages with the proper scheme. For other cases, it may
  be preferable to use `$page->url()` since it produces shorter output.

~~~~~
// Generating a link to this page using httpUrl
echo "<a href='$page->httpUrl'>$page->title</a>";
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` For details on usage see `Page::url()` options argument.

## Return value

string Returns full URL to page, for example: `https://processwire.com/about/`

## See also

- [Page::url()](../Page/method-url.md)
- [Page::localHttpUrl()](../Page/index.md)
