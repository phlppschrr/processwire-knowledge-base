# Session::getFor()

Source: `wire/core/Session.php`

Get a session variable within a given namespace

~~~~~
// Retrieve namespaced session value
$firstName = $session->getFor($this, 'firstName');
~~~~~


@param string|object $ns Namespace string or object

@param string $key Specify variable name to retrieve, or blank string to return all variables in the namespace.

@return mixed
