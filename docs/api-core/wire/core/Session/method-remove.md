# $session->remove($key, $_key = null): $this

Source: `wire/core/Session.php`

Unset a session variable

## Example

~~~~~
// Unset a session var
$session->remove('firstName');

// Unset a session var in a namespace
$session->remove($this, 'firstName');

// Unset all session vars in a namespace
$session->remove($this, true);
~~~~~

## Usage

~~~~~
// basic usage
$result = $session->remove($key);

// usage with all arguments
$result = $session->remove($key, $_key = null);
~~~~~

## Arguments

- `$key` `string|object` Name of session variable you want to remove (or namespace string/object)
- `$_key` (optional) `string|bool|null` Omit this argument unless first argument is a namespace. Otherwise specify one of: - If first argument is namespace and you want to remove a property from the namespace, provide key here. - If first argument is namespace and you want to remove all properties from the namespace, provide boolean TRUE.

## Return value

- `$this`
