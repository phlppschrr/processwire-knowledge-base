# Functions::wireLen()

Source: `wire/core/Functions.php`

Returns string byte length of any type (string, array, object, bool, int, etc.)

This is identical to the `wireLength()` function except that it does not use
multibyte string lengths on strings, so it returns a byte length when given
a multibyte string rather than a visual character length. So on strings
it uses strlen() rather than mb_strlen().

@param string|array|object|int|bool|null $value

@return int

@since 3.0.192
