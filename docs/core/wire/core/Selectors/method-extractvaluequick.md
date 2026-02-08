# $selectors->extractValueQuick(&$str, $openingQuote, $closingQuote): false|string|string[]

Source: `wire/core/Selectors.php`

Early-exit optimizations for extractValue

## Arguments

- string $str String to extract value from, $str will be modified if extraction successful
- string $openingQuote Opening quote character, if string has them, blank string otherwise
- string $closingQuote Closing quote character, if string has them, blank string otherwise

## Return value

false|string|string[] Returns found value if successful, boolean false if not
