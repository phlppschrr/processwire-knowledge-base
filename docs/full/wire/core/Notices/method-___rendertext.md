# $notices->renderText(): string

Source: `wire/core/Notices.php`

Render these Notices as plain text

Note: if this ends up in HTML, such as in a `<pre>`, you should pass the returned text
through `$sanitizer->entities()` or `htmlspecialchars()` before outputting.

## Usage

~~~~~
// basic usage
$string = $notices->renderText();
~~~~~

## Hookable

- Hookable method name: `renderText`
- Implementation: `___renderText`
- Hook with: `$notices->renderText()`

## Return value

- `string`

## Since

3.0.254
