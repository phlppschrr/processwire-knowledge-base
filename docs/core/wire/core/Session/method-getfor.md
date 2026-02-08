# $session->getFor($ns, $key): mixed

Source: `wire/core/Session.php`

Get a session variable within a given namespace

## Example

~~~~~
// Retrieve namespaced session value
$firstName = $session->getFor($this, 'firstName');
~~~~~

## Usage

~~~~~
// basic usage
$result = $session->getFor($ns, $key);
~~~~~

## Arguments

- `$ns` `string|object` Namespace string or object
- `$key` `string` Specify variable name to retrieve, or blank string to return all variables in the namespace.

## Return value

- `mixed`
