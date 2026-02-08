# SessionCSRF::getToken()

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token name and value


@param int|string|null $id Optional unique ID for this token

@return array ("name" => "token name", "value" => "token value", "time" => created timestamp)
