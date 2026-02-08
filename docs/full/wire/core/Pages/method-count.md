# $pages->count($selector = '', $options = array()): int

Source: `wire/core/Pages.php`

Count and return how many pages will match the given selector.

If no selector provided, it returns count of all pages in site.

~~~~~~~~~
// Return count of how may pages in the site use the blog-post template
$numBlogPosts = $pages->count("template=blog-post");
~~~~~~~~~

## Arguments

- string|array|Selectors $selector Specify selector, or omit to retrieve a site-wide count.
- array|string $options See $options for $pages->find().

## Return value

int

## See also

- [Pages::find()](method-___find.md)
