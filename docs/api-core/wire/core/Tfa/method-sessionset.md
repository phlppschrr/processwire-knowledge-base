# $tfa->sessionSet($key, $value = null)

Source: `wire/core/Tfa.php`

Set a session variable only for this module

Optionally set several variables at once by specifying just $key as an associative array.

## Usage

~~~~~
// basic usage
$result = $tfa->sessionSet($key);

// usage with all arguments
$result = $tfa->sessionSet($key, $value = null);
~~~~~

## Arguments

- `$key` `string|array`
- `$value` (optional) `mixed`
