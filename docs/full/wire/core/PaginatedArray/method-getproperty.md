# $paginatedArray->getProperty($property): mixed

Source: `wire/core/PaginatedArray.php`

Get a property of the PageArray

These map to functions from the array and are here for convenience.
Properties include count, total, start, limit, last, first, keys, values,
These can also be accessed by direct reference, i.e. `$items->limit`.

Please see the `WireArray::getProperty()` method for full details on
non-pagination related properties that can be retrieved through this.

## Arguments

- `$property` `string` Name of property you want to retrieve, can be any of the following: - `count` (int): Count of items currently present. - `total` (int): Total quantity of items across all paginations. - `start` (int): Current start index for pagination. - `limit` (int): Current limit used for pagination. - `last` (mixed): Last item in the WireArray. - `first` (mixed): First item in the WireArray.

## Return value

mixed Value of requested property.
