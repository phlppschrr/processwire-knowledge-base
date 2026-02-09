# $session->getNamespace($ns): string

Source: `wire/core/Session.php`

Given a namespace object or string, return the namespace string

## Usage

~~~~~
// basic usage
$string = $session->getNamespace($ns);
~~~~~

## Arguments

- `$ns` `object|string`

## Return value

- `string`

## Exceptions

- `WireException` if given invalid namespace type
