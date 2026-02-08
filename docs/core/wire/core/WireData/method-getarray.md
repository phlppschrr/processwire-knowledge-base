# WireData::getArray()

Source: `wire/core/WireData.php`

Returns the full array of properties set to this object

If descending classes also store data in other containers, they may want to
override this method to include that data as well.


@return array Returned array is associative and indexed by property name.
