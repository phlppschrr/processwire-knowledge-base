# WireArray::isValidKey()

Source: `wire/core/WireArray.php`

Is the given item key valid for use in this array?

Template method that descendant classes may use to validate the key of items added to this WireArray


@param string|int $key Key to test

@return bool True if key is valid and may be used, false if not
