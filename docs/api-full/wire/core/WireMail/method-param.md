# $wireMail->param($value): $this

Source: `wire/core/WireMail.php`

Set any email param

See `$additional_parameters` at <http://www.php.net/manual/en/function.mail.php>

- Multiple calls will append existing params.
- To remove an existing param, specify NULL as the value.

This function may only be applicable if you don't have other WireMail modules
installed as email params are only used by PHP's `mail()` function.

## Usage

~~~~~
// basic usage
$result = $wireMail->param($value);
~~~~~

## Arguments

- `$value` `string`

## Return value

- `$this`
