# Page::parent()

Source: `wire/core/Page.php`

Return this page’s parent Page, or–if given a selector–the closest matching parent.

Omit all arguments if you just want to retrieve the parent of this page, which would be the same as the
`$page->parent` property. To retrieve the closest parent matching your selector, specify either a selector
string or array.

~~~~~
// Retrieve the parent
$parent = $page->parent();

// Retrieve the closest parent using template "products"
$parent = $page->parent("template=products");
~~~~~


@param string|array $selector Optional selector. When used, it returns the closest parent matching the selector.

@return Page Returns a Page or a NullPage when there is no parent or the selector string did not match any parents.
