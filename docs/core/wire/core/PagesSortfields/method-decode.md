# PagesSortfields::decode()

Source: `wire/core/PagesSortfields.php`

Decodes a sortfield from a signed integer or string to a field name

The returned fieldname is preceded with a dash if the sortfield is reversed.

@param string|int $sortfield

@param string $default Default sortfield name (default='sort')

@return string
