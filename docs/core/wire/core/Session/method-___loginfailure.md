# $session->loginFailure($name, $reason)

Source: `wire/core/Session.php`

Login failure method for hooks

## Usage

~~~~~
// basic usage
$result = $session->loginFailure($name, $reason);
~~~~~

## Hookable

- Hookable method name: `loginFailure`
- Implementation: `___loginFailure`
- Hook with: `$session->loginFailure()`

## Arguments

- `$name` `string` Attempted login name
- `$reason` `string` Reason for login failure
