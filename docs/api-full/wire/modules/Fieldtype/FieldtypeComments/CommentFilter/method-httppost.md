# $commentFilter->httpPost($request, $host, $path, $port = 80): array|string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFilter.php`

Send an HTTP POST request

## Usage

~~~~~
// basic usage
$array = $commentFilter->httpPost($request, $host, $path);

// usage with all arguments
$array = $commentFilter->httpPost($request, $host, $path, $port = 80);
~~~~~

## Arguments

- $request
- $host
- $path
- `$port` (optional) `int`

## Return value

- `array|string`

## Deprecated

no longer in use (replaced with WireHttp)
