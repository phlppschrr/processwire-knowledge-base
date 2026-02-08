# $pageTraversal->prevUntilSiblings(Page $page, $selector = '', $filter = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages before this one until matching the one specified

## Arguments

- Page $page
- string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.
- string|array $filter Optional selector string to filter matched pages by
- PageArray|null $siblings Optional PageArray of siblings to use instead of all from the page.

## Return value

PageArray
