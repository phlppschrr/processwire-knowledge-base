# HTMLPurifier_StringHash

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

This is in almost every respect equivalent to an array except
that it keeps track of which keys were accessed.

@warning For the sake of backwards compatibility with early versions
    of PHP 5, you must not use the $hash[$key] syntax; if you do
    our version of offsetGet is never called.

## resetAccessed()

Resets the access array.
