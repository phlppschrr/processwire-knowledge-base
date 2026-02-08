# $notices->___renderText(): string

Source: `wire/core/Notices.php`

Render these Notices as plain text

Note: if this ends up in HTML, such as in a `<pre>`, you should pass the returned text
through `$sanitizer->entities()` or `htmlspecialchars()` before outputting.

## Return value

string

## Meta

- @since 3.0.254
