# Notices::___renderText()

Source: `wire/core/Notices.php`

Render these Notices as plain text

Note: if this ends up in HTML, such as in a `<pre>`, you should pass the returned text
through `$sanitizer->entities()` or `htmlspecialchars()` before outputting.

@return string

@since 3.0.254
