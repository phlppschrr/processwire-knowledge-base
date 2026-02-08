# WireRandom::arrayValues()

Source: `wire/core/WireRandom.php`

Return a random version of given array or a quantity of random items

Array keys are retained in return value, unless requested $qty exceeds
the quantity of items in given array.

@param array $a Array to get random items from.

@param int $qty Quantity of items, or 0 to return all (default=0).

@return array
