# $sessionCSRF->getToken($id = ''): array

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token name and value

## Usage

~~~~~
// basic usage
$array = $sessionCSRF->getToken();

// usage with all arguments
$array = $sessionCSRF->getToken($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `array` ("name" => "token name", "value" => "token value", "time" => created timestamp)
