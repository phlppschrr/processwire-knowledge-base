# HTMLPurifier_PercentEncoder

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Class that handles operations involving percent-encoding in URIs.

@warning
     Be careful when reusing instances of PercentEncoder. The object
     you use for normalize() SHOULD NOT be used for encode(), or
     vice-versa.

## encode()

Our replacement for urlencode, it encodes all non-reserved characters,
as well as any extra characters that were instructed to be preserved.
@note
     Assumes that the string has already been normalized, making any
     and all percent escape sequences valid. Percents will not be
     re-escaped, regardless of their status in $preserve
@param string $string String to be encoded
@return string Encoded string.

## normalize()

Fix up percent-encoding by decoding unreserved characters and normalizing.
@warning This function is affected by $preserve, even though the
         usual desired behavior is for this not to preserve those
         characters. Be careful when reusing instances of PercentEncoder!
@param string $string String to normalize
@return string
