# WireHttp::getResponseHeaderValues()

Source: `wire/core/WireHttp.php`

Get last HTTP response headers with multi-value headers as arrays

Use this method when you want to retrieve headers that can potentially contain multiple-values.
Note that any code that iterates these values should be able to handle them being either a string or
an array.

This method always returns an associative array of strings and arrays, unless you specify the
`$key` option in which case it can return an array, string, or NULL if the header is not present.


@param string $key Optional header name you want to get (if you only need a specific header)

@param bool $forceArrays If even single-value headers should be arrays, specify true (default=false).

@return array|string|null
