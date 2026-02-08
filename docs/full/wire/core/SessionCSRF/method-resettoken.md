# $sessionCSRF->resetToken($id = '')

Source: `wire/core/SessionCSRF.php`

Clear out token value

## Usage

~~~~~
// basic usage
$result = $sessionCSRF->resetToken();

// usage with all arguments
$result = $sessionCSRF->resetToken($id = '');
~~~~~

## Arguments

- `$id` (optional) `int|string|null` Optional unique ID for this token
