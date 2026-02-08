# WireArray::findRandom()

Source: `wire/core/WireArray.php`

Find a specified quantity of random elements from this WireArray.

Unlike `WireArray::getRandom()` this method always returns a WireArray (or derived type).

~~~~~
// Get 3 random items
$randomItems = $items->findRandom(3);
~~~~~


@param int $num Number of items to return

@return WireArray

@see WireArray::getRandom(), WireArray::findRandomTimed()
