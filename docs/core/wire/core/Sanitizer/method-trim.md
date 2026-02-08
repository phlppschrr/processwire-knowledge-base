# $sanitizer->trim($str, $chars = '', $method = 'trim'): string

Source: `wire/core/Sanitizer.php`

Trim off all known UTF-8 whitespace types (or given chars) from beginning and ending of string

Like PHP’s trim() but works with multibyte strings and recognizes all types of UTF-8 whitespace
as well as HTML whitespace entities. This method also optionally accepts an array for $chars argument
which enables you to trim out string sequences greater than one character long.

If you do not need an extensive multibyte trim, use PHP’s trim() instead because this takes more overhead.
PHP multibyte support (mb_string) is strongly recommended if using this function.

## Arguments

- string $str
- string|array $chars Array or string of chars to trim, or omit (blank string) for all whitespace (includes UTF-8 and HTML-entity whitespace too).
- string $method Trim method, one of "trim" (both), "rtrim" (right-only) or "ltrim" (left-only). Or just "t", "r", "l" is also fine. 3.0.168+

## Return value

string

## Meta

- @since 3.0.124
