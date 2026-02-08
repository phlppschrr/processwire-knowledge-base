# $wireInput->httpsUrl($options = array()): string

Source: `wire/core/WireInput.php`

Same as httpUrl() method but always uses https scheme, rather than current request scheme

See httpUrl() method for argument and usage details.

## Usage

~~~~~
// basic usage
$string = $wireInput->httpsUrl();

// usage with all arguments
$string = $wireInput->httpsUrl($options = array());
~~~~~

## Arguments

- `$options` (optional) `array|bool` Specify `withQueryString` (bool) option, or in 3.0.167+ you can also use an options array: - `withQueryString` (bool): Include the query string as well? (if present, default=false) - `page` (Page): Page object to use, if different from $page (default=$page)

## Return value

- `string`

## See Also

- [WireInput::httpUrl()](method-httpurl.md)
