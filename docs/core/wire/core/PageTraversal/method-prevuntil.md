# $pageTraversal->prevUntil(Page $page, $selector = '', $filter = '', array $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one until matching the one specified

## Arguments

- Page $page
- string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.
- string|array $filter Optional selector to filter matched pages by
- array $options Options to pass to the _next() method

## Return value

PageArray
