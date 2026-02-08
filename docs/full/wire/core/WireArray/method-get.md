# WireArray::get()

Source: `wire/core/WireArray.php`

Returns the value of the item at the given index, or null if not set.

You may also specify a selector, in which case this method will return the same result as
the `WireArray::findOne()` method. See the $key argument description for more details on
what can be provided.


@param int|string|array $key Provide any of the following:
 - Key of item to retrieve.
 - Array of keys, in which case an array of matching items will be returned, indexed by your keys.
 - A selector string or selector array, to return the first item that matches the selector.
 - A string of text with "{var}" tags in it that will be populated with any matching properties from this WireArray.
 - A string like "foobar[]" which returns an array of all "foobar" properties from each item in the WireArray.
 - A string containing the "name" property of any item, and the matching item will be returned.

@return WireData|Page|mixed|array|null Value of item requested, or null if it doesn't exist.

@throws WireException
