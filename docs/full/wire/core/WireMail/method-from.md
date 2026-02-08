# $wireMail->from($email, $name = null): $this

Source: `wire/core/WireMail.php`

Set the email 'from' address and optionally name

## Arguments

- string $email Must be a single email address or "User Name <user@example.com>" string.
- string|null An optional FROM name (same as setting/calling fromName)

## Return value

$this

## Throws

- WireException if provided email was invalid or in blacklist
