# $pageTraversal->parentsUntil(Page $page, $selector = '', $filter = ''): PageArray

Source: `wire/core/PageTraversal.php`

Return all parent from current till the one matched by $selector

## Arguments

- Page $page
- string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.
- string|array $filter Optional selector to filter matched pages by

## Return value

PageArray
