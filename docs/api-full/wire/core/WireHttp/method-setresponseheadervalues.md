# $wireHttp->setResponseHeaderValues(array $responseHeader)

Source: `wire/core/WireHttp.php`

Set response headers where they are provided as an associative array and values can be strings or arrays

## Usage

~~~~~
// basic usage
$result = $wireHttp->setResponseHeaderValues($responseHeader);

// usage with all arguments
$result = $wireHttp->setResponseHeaderValues(array $responseHeader);
~~~~~

## Arguments

- `$responseHeader` `array` headers in an associative array
