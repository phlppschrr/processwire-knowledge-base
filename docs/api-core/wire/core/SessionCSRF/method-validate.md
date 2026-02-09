# $sessionCSRF->validate($id = ''): bool

Source: `wire/core/SessionCSRF.php`

Throws an exception if the token is invalid

## Usage

~~~~~
// basic usage
$bool = $sessionCSRF->validate();

// usage with all arguments
$bool = $sessionCSRF->validate($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token

## Return value

- `bool` Always returns true or throws exception

## Exceptions

- `WireCSRFException` if token not valid
