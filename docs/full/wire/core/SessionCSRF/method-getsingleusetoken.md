# SessionCSRF::getSingleUseToken()

Source: `wire/core/SessionCSRF.php`

Get a CSRF Token name and value that can only be used once

Note that a single call to hasValidToken($id) or validate($id) will invalidate the single use token.
So call them once and store your result if you need the result multiple times.


@param int|string $id Optional unique ID/name for this token (of omitted one is generated automatically)

@return array ("id' => "token ID", "name" => "token name", "value" => "token value", "time" => created timestamp)
