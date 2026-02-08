# $sessionCSRF->getTokenTime($id = ''): int

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token timestamp

## Usage

~~~~~
// basic usage
$int = $sessionCSRF->getTokenTime();

// usage with all arguments
$int = $sessionCSRF->getTokenTime($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `int`
