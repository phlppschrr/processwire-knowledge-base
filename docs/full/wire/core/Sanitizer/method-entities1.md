# Sanitizer::entities1()

Source: `wire/core/Sanitizer.php`

Entity encode a string and don’t double encode it if already encoded


@param string $str String to entity encode

@param int|bool $flags See PHP htmlentities() function for flags.

@param string $encoding Encoding of string (default="UTF-8").

@return string Entity encoded string

@see Sanitizer::entities(), Sanitizer::unentities()
