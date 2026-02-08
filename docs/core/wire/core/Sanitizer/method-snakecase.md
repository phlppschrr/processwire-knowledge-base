# Sanitizer::snakeCase()

Source: `wire/core/Sanitizer.php`

Convert string to be all snake_case (lowercase and underscores)

For example, "Hello World" or "hello-world" becomes "hello_world".


@param string $value

@param array $options
 - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-z0-9').
 - `hyphen` (string): Character to use as the hyphen (default='-')

@return string
