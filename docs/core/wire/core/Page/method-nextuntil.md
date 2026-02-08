# $page->nextUntil($selector = '', $filter = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/Page.php`

Return all sibling pages after this one until matching the one specified

## Arguments

- string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.
- string|array $filter Optional selector to filter matched pages by
- PageArray $siblings Optional PageArray of siblings to use instead (avoid).

## Return value

PageArray
