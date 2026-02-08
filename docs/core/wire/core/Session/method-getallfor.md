# $session->getAllFor($ns): array

Source: `wire/core/Session.php`

Get all session variables for given namespace and return associative array

## Arguments

- `$ns` `string|Wire`

## Return value

array

## Since

3.0.141 Method added for consistency, but any version can do this with $session->getFor($ns, '');
