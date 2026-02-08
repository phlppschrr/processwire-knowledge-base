# WireArray::count()

Source: `wire/core/WireArray.php`

Returns the number of items in this WireArray.

Fulfills PHP's Countable interface, meaning it also enables this WireArray to be used with PHP's `count()` function.

~~~~~
// These two are the same
$qty = $items->count();
$qty = count($items);
~~~~~


@return int
