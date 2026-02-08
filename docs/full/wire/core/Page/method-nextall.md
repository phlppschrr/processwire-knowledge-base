# Page::nextAll()

Source: `wire/core/Page.php`

Return all sibling pages after this one, optionally matching a selector


@param string|array|bool $selector Optional selector. When specified, will filter the found siblings.

@param bool|PageArray $getQty Return a count instead of PageArray? (boolean)
  - If no $selector argument is needed, this may be specified as the first argument.
  - Legacy support: You may specify a PageArray of siblings to use instead of the default (deprecated, avoid it).

@param bool $getPrev For internal use, makes this method implement the prevAll() behavior instead.

@return PageArray|int Returns all matching pages after this one, or integer if $count option specified.
