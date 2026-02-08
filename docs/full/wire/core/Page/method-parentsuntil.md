# $page->parentsUntil($selector = '', $filter = ''): PageArray

Source: `wire/core/Page.php`

Return all parents from current page till the one matched by $selector

This duplicates the jQuery parentsUntil() function in ProcessWire.

## Arguments

- string|Page|array $selector May either be a selector sor Page to stop at. Results will not include this.
- string|array $filter Optional selector to filter matched pages by

## Return value

PageArray
