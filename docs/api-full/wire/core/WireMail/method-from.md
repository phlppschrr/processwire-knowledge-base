# $wireMail->from($email, $name = null): $this

Source: `wire/core/WireMail.php`

Set the email 'from' address and optionally name

## Usage

~~~~~
// basic usage
$result = $wireMail->from($email);

// usage with all arguments
$result = $wireMail->from($email, $name = null);
~~~~~

## Arguments

- `$email` `string` Must be a single email address or "User Name <user@example.com>" string.
- string|null An optional FROM name (same as setting/calling fromName)

## Return value

- `$this`

## Exceptions

- `WireException` if provided email was invalid or in blacklist
