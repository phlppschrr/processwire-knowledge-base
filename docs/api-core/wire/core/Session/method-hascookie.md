# $session->hasCookie($checkLogin = false): bool

Source: `wire/core/Session.php`

Are session cookie(s) present?

## Usage

~~~~~
// basic usage
$bool = $session->hasCookie();

// usage with all arguments
$bool = $session->hasCookie($checkLogin = false);
~~~~~

## Arguments

- `$checkLogin` (optional) `bool` Specify true to check instead for challenge cookie (which indicates login may be active).

## Return value

- `bool` Returns true if session cookie present, false if not.
