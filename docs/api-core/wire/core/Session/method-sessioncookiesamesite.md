# $session->sessionCookieSameSite($value = null): string

Source: `wire/core/Session.php`

Get 'SameSite' value for session cookie

## Usage

~~~~~
// basic usage
$string = $session->sessionCookieSameSite();

// usage with all arguments
$string = $session->sessionCookieSameSite($value = null);
~~~~~

## Arguments

- `$value` (optional) `string|null`

## Return value

- `string`

## Since

3.0.178
