# $wireMail->header($key, $value): $this

Source: `wire/core/WireMail.php`

Set any email header

- Multiple calls will append existing headers.
- To remove an existing header, specify NULL as the value.

## Usage

~~~~~
// basic usage
$result = $wireMail->header($key, $value);
~~~~~

## Arguments

- `$key` `string|array` Header name
- `$value` `string` Header value or specify null to unset

## Return value

- `$this`
