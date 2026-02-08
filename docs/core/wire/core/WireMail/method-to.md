# $wireMail->to($email = null, $name = null): $this

Source: `wire/core/WireMail.php`

Set the email to address

Each added email addresses appends to any addresses already supplied, unless
you specify NULL as the email address, in which case it clears them all.

## Usage

~~~~~
// basic usage
$result = $wireMail->to();

// usage with all arguments
$result = $wireMail->to($email = null, $name = null);
~~~~~

## Arguments

- `$email` (optional) `string|array|null` Specify any ONE of the following: - Single email address or "User Name <user@example.com>" string. - CSV string of #1. - Non-associative array of #1. - Associative array of (email => name) - NULL (default value, to clear out any previously set values)
- `$name` (optional) `string` Optionally provide a TO name, applicable only when specifying #1 (single email) for the first argument.

## Return value

- `$this`

## Exceptions

- `WireException` if any provided emails were invalid or in blacklist
