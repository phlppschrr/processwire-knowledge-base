# $sessionCSRF->getTokenValue($id = ''): string

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token value as stored in the session, or create one if it doesn't yet exist

## Usage

~~~~~
// basic usage
$string = $sessionCSRF->getTokenValue();

// usage with all arguments
$string = $sessionCSRF->getTokenValue($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `string`
