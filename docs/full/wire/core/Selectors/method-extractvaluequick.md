# Selectors::extractValueQuick()

Source: `wire/core/Selectors.php`

Early-exit optimizations for extractValue

@param string $str String to extract value from, $str will be modified if extraction successful

@param string $openingQuote Opening quote character, if string has them, blank string otherwise

@param string $closingQuote Closing quote character, if string has them, blank string otherwise

@return false|string|string[] Returns found value if successful, boolean false if not
