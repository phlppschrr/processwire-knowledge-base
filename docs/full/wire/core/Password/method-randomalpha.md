# Password::randomAlpha()

Source: `wire/core/Password.php`

Return a pseudo-random alpha or alphanumeric character

This method may be deprecated at some point, so it is preferable to use the
`randomLetters()` or `randomAlnum()` methods instead, when you can count on
the PW version being 3.0.109 or higher.

@param int $qty Number of random characters requested

@param bool $alphanumeric Specify true to allow digits in return value

@param array $disallow Characters that may not be used in return value

@return string

@deprecated use WireRandom::alpha() instead
