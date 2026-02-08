# Sanitizer::bool()

Source: `wire/core/Sanitizer.php`

Convert the given value to a boolean

This differs from regular boolean type conversion in the following ways:

- This method will recognize things like the strings "false" or "0" representing a boolean false.
- If given an object, it will convert the object to a string before determining what boolean value it should represent.
- If given an array, it returns false if the array contains zero items.


@param $value

@return bool
