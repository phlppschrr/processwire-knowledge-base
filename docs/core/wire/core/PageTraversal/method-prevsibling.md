# PageTraversal::prevSibling()

Source: `wire/core/PageTraversal.php`

Return the previous sibling page within a provided group of siblings that contains the current page

This method is the old version of the prev() method and is only used if a $siblings argument is provided
to the Page::prev() call. It is much slower than the prev() method.

If given a PageArray of siblings (containing the current) it will return the previous sibling relative to the provided PageArray.

Be careful with this function when the page has a lot of siblings. It has to load them all, so this function is best
avoided at large scale, unless you provide your own already-reduced siblings list (like from pagination)

When using a selector, note that this method operates only on visible children. If you want something like "include=all"
or "include=hidden", they will not work in the selector. Instead, you should provide the siblings already retrieved with
one of those modifiers, and provide those siblings as the second argument to this function.

@param Page $page

@param string|array $selector Optional selector. When specified, will find nearest previous sibling that matches.

@param PageArray|null $siblings Optional siblings to use instead of the default. May also be specified as first argument when no selector needed.

@return Page|NullPage Returns the previous sibling page, or a NullPage if none found.
