# Page::prevUntil()

Source: `wire/core/Page.php`

Return all sibling pages before this one until matching the one specified


@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param PageArray|null $siblings Optional PageArray of siblings to use instead of default.

@return PageArray
