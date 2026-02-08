# $wireArray->last(): Wire|mixed|bool

Source: `wire/core/WireArray.php`

Returns the last item in the WireArray or boolean false if empty.

Note that this resets the internal WireArray pointer, which would affect other active iterations.

~~~~~
$item = $items->last();
~~~~~

## Return value

Wire|mixed|bool
