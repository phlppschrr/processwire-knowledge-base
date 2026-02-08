# PageTraversal::siblings()

Source: `wire/core/PageTraversal.php`

Return this Page's sibling pages, optionally filtered by a selector.

Note that the siblings include the current page. To exclude the current page, specify "id!=$page".

@param Page $page

@param string $selector Optional selector to filter siblings by.

@return PageArray
