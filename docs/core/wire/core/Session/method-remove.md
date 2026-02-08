# Session::remove()

Source: `wire/core/Session.php`

Unset a session variable

~~~~~
// Unset a session var
$session->remove('firstName');

// Unset a session var in a namespace
$session->remove($this, 'firstName');

// Unset all session vars in a namespace
$session->remove($this, true);
~~~~~


@param string|object $key Name of session variable you want to remove (or namespace string/object)

@param string|bool|null $_key Omit this argument unless first argument is a namespace. Otherwise specify one of:
 - If first argument is namespace and you want to remove a property from the namespace, provide key here.
	- If first argument is namespace and you want to remove all properties from the namespace, provide boolean TRUE.

@return $this
