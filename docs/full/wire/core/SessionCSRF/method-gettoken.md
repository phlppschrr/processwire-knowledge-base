# $sessionCSRF->getToken($id = ''): array

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token name and value

## Arguments

- int|string|null $id Optional unique ID for this token

## Return value

array ("name" => "token name", "value" => "token value", "time" => created timestamp)
