# WireArray::getValues()

Source: `wire/core/WireArray.php`

Returns a regular PHP array of all values used in this WireArray.

Unlike the `WireArray::getArray()` method, this does not attempt to maintain original
keys of the items. The returned array is reindexed from 0.


@return array|Wire[] Values used in the WireArray.

@see WireArray::getArray()
