# $wireMailInterface->to($email = null, $name = null): self

Source: `wire/core/WireMailInterface.php`

Set the email to address

Each added email addresses appends to any addresses already supplied, unless
you specify NULL as the email address, in which case it clears them all.

## Arguments

- string|array|null $email Specify any ONE of the following: 1. Single email address or "User Name <user@example.com>" string. 2. CSV string of #1. 3. Non-associative array of #1. 4. Associative array of (email => name) 5. NULL (default value, to clear out any previously set values)
- string $name Optionally provide a FROM name, applicable only when specifying #1 (single email) for the first argument.

## Return value

self

## Throws

- WireException if any provided emails were invalid
