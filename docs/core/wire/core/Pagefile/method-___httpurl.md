# $pagefile->httpUrl(): string

Source: `wire/core/Pagefile.php`

Return the web accessible URL (with scheme and hostname) to this Pagefile.

## Usage

~~~~~
// basic usage
$string = $pagefile->httpUrl();
~~~~~

## Hookable

- Hookable method name: `httpUrl`
- Implementation: `___httpUrl`
- Hook with: `$pagefile->httpUrl()`

## Return value

- `string`

## See Also

- [Pagefile::url()](method-url.md)
