# $wireMail->header($key, $value): $this

Source: `wire/core/WireMail.php`

Set any email header

- Multiple calls will append existing headers.
- To remove an existing header, specify NULL as the value.

## Arguments

- string|array $key Header name
- string $value Header value or specify null to unset

## Return value

$this
