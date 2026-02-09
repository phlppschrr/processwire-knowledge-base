# $wireInput->requestMethod($method = ''): string|bool

Source: `wire/core/WireInput.php`

Return the current request method (i.e. GET, POST, etc.) or blank if not known

Possible return values are:
- GET
- POST
- HEAD
- PUT
- DELETE
- OPTIONS
- or blank if not known

## Usage

~~~~~
// basic usage
$string = $wireInput->requestMethod();

// usage with all arguments
$string = $wireInput->requestMethod($method = '');
~~~~~

## Arguments

- `$method` (optional) `string` Optionally enter the request method to return bool if current method matches

## Return value

- `string|bool`

## Since

3.0.39
