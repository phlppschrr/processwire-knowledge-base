# $sessionCSRF->getTokenName($id = ''): string

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token name, or create one if it doesn't yet exist

## Usage

~~~~~
// basic usage
$string = $sessionCSRF->getTokenName();

// usage with all arguments
$string = $sessionCSRF->getTokenName($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `string`
