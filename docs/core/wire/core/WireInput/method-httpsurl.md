# WireInput::httpsUrl()

Source: `wire/core/WireInput.php`

Same as httpUrl() method but always uses https scheme, rather than current request scheme

See httpUrl() method for argument and usage details.


@param array|bool $options Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array:
 - `withQueryString` (bool): Include the query string as well? (if present, default=false)
 - `page` (Page): Page object to use, if different from $page (default=$page)

@return string

@see WireInput::httpUrl()
