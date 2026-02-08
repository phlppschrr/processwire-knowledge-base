# $session->removeFor($ns, $key): $this

Source: `wire/core/Session.php`

Unset a session variable within a namespace

## Usage

~~~~~
// basic usage
$result = $session->removeFor($ns, $key);
~~~~~

## Arguments

- `$ns` `string|object` Namespace
- `$key` `string` Provide name of variable to remove, or boolean true to remove all in namespace.

## Return value

- `$this`
