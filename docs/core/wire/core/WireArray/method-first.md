# WireArray::first()

Source: `wire/core/WireArray.php`

Returns the first item in the WireArray or boolean false if empty.

Note that this resets the internal WireArray pointer, which would affect other active iterations.

~~~~~
$item = $items->first();
~~~~~


@return Wire|mixed|bool
