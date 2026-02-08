# $page->path(): string

Source: `wire/core/Page.php`

Returns the Page’s path from the ProcessWire installation root.

The path is always indicated from the ProcessWire installation root. Meaning, if the installation is
running from a subdirectory, then the path does not include that subdirectory, whereas the url does.
Note that path and url are identical if installation is not running from a subdirectory.


~~~~~
// Difference between path and url on site running from subdirectory /my-site/
echo $page->path(); // outputs: /about/contact/
echo $page->url();  // outputs: /my-site/about/contact/
~~~~~

## Return value

string Returns the page path, for example: `/about/contact/`

## See also

- [Page::url()](method-url.md)
- [Page::httpUrl()](method-httpurl.md)
