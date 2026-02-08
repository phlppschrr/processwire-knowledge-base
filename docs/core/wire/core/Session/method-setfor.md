# $session->setFor($ns, $key, $value): $this

Source: `wire/core/Session.php`

Set a session variable within a given namespace

To remove a namespace, use `$session->remove($namespace)`.

~~~~~
// Set a session value for a namespace
$session->setFor($this, 'firstName', 'Bob');
~~~~~

## Arguments

- `$ns` `string|object` Namespace string or object.
- `$key` `string` Name of session variable you want to set.
- `$value` `mixed` Value you want to set, or specify null to unset.

## Return value

$this
