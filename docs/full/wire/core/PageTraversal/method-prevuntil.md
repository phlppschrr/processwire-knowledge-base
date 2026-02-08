# PageTraversal::prevUntil()

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one until matching the one specified

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param array $options Options to pass to the _next() method

@return PageArray
