# $wireMail->replyTo($email, $name = null): $this

Source: `wire/core/WireMail.php`

Set the 'reply-to' email address and optionally name (where supported)

## Arguments

- string $email Must be a single email address or "User Name <user@example.com>" string.
- string|null An optional Reply-To name (same as setting/calling replyToName method)

## Return value

$this

## Throws

- WireException if provided email was invalid or in blacklist
