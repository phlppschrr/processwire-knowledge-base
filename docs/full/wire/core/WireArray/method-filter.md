# WireArray::filter()

Source: `wire/core/WireArray.php`

Filter this WireArray to only include items that match the given selector (destructive)

~~~~~
// Filter $items to contain only those with "featured" property having value 1
$items->filter("featured=1");
~~~~~


@param string|array|Selectors $selector Selector string or array to use as the filter.

@return $this reference to current instance.

@see filterData
