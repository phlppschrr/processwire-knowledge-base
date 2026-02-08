# $session->getFor($ns, $key): mixed

Source: `wire/core/Session.php`

Get a session variable within a given namespace

~~~~~
// Retrieve namespaced session value
$firstName = $session->getFor($this, 'firstName');
~~~~~

## Arguments

- string|object $ns Namespace string or object
- string $key Specify variable name to retrieve, or blank string to return all variables in the namespace.

## Return value

mixed
