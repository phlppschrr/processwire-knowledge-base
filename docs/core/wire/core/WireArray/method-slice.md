# WireArray::slice()

Source: `wire/core/WireArray.php`

Get a slice of the WireArray.

Given a starting point and a number of items, returns a new WireArray of those items.
If `$limit` is omitted, then it includes everything beyond the starting point.

~~~~~
// Get first 3 items
$myItems = $items->slice(0, 3);
~~~~~


@param int $start Starting index.

@param int $limit Number of items to include. If omitted, includes the rest of the array.

@return WireArray Returns a new WireArray.
