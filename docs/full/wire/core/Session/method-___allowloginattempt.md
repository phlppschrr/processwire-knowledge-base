# $session->allowLoginAttempt($name): bool

Source: `wire/core/Session.php`

Allow login attempt for given name at all?

This method does nothing and is purely for hooks to modify return value.

## Usage

~~~~~
// basic usage
$bool = $session->allowLoginAttempt($name);
~~~~~

## Hookable

- Hookable method name: `allowLoginAttempt`
- Implementation: `___allowLoginAttempt`
- Hook with: `$session->allowLoginAttempt()`

## Arguments

- `$name` `string`

## Return value

- `bool`
