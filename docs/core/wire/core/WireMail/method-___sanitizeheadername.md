# $wireMail->sanitizeHeaderName($name): string

Source: `wire/core/WireMail.php`

Sanitize and normalize a header name

## Usage

~~~~~
// basic usage
$string = $wireMail->sanitizeHeaderName($name);
~~~~~

## Hookable

- Hookable method name: `sanitizeHeaderName`
- Implementation: `___sanitizeHeaderName`
- Hook with: `$wireMail->sanitizeHeaderName()`

## Arguments

- `$name` `string`

## Return value

- `string`

## Since

3.0.132
