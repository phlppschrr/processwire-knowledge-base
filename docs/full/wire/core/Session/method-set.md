# $session->set($key, $value, $_value = null): $this

Source: `wire/core/Session.php`

Set a session variable

- You can optionally use a namespace with this method, to avoid collisions with other session variables.
  But if using namespaces we recommended using the dedicated getFor() and setFor() methods instead.
- You can also get or set non-namespaced session values directly (see examples).

~~~~~
// Set value "Bob" to session variable named "firstName"
$session->set('firstName', 'Bob');

// You can retrieve the firstName now, or any later request
$firstName = $session->get('firstName');

// outputs: Hello Bob
echo "Hello $firstName";
~~~~~
~~~~~
// Setting and getting a session value directly
$session->firstName = 'Bob';
$firstName = $session->firstName;
~~~~~

## Arguments

- `$key` `string|object` Name of session variable to set (or object for namespace)
- `$value` `string|mixed` Value to set (or name of variable, if first argument is namespace)
- `$_value` (optional) `mixed` Value to set if first argument is namespace. Omit otherwise.

## Return value

$this
