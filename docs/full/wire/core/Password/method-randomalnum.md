# Password::randomAlnum()

Source: `wire/core/Password.php`

Return cryptographically secure random alphanumeric, alpha or numeric string

@param int $length Required length of string, or 0 for random length

@param array $options See WireRandom::alphanumeric() for options

@return string

@throws WireException

@since 3.0.109

@deprecated use WireRandom::alphanumeric() instead
