# WireArray::add()

Source: `wire/core/WireArray.php`

Add an item to the end of the WireArray.

~~~~~
$items->add($item);
~~~~~


@param int|string|array|object|Wire|WireArray $item Item to add.

@return $this

@throws WireException If given an item that can't be stored by this WireArray.

@see WireArray::prepend(), WireArray::append()
