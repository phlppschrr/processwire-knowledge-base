# Session::setFor()

Source: `wire/core/Session.php`

Set a session variable within a given namespace

To remove a namespace, use `$session->remove($namespace)`.

~~~~~
// Set a session value for a namespace
$session->setFor($this, 'firstName', 'Bob');
~~~~~


@param string|object $ns Namespace string or object.

@param string $key Name of session variable you want to set.

@param mixed $value Value you want to set, or specify null to unset.

@return $this
