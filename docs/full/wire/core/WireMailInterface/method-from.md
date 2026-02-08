# $wireMailInterface->from($email, $name = null): self

Source: `wire/core/WireMailInterface.php`

Set the email from address

## Arguments

- string Must be a single email address or "User Name <user@example.com>" string.
- string|null An optional FROM name (same as setting/calling fromName)

## Return value

self

## Throws

- WireException if provided email was invalid
