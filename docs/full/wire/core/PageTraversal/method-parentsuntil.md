# PageTraversal::parentsUntil()

Source: `wire/core/PageTraversal.php`

Return all parent from current till the one matched by $selector

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@return PageArray
