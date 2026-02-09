# $wireHttp->setCookie($name, $value): self

Source: `wire/core/WireHttp.php`

Set cookie(s) for http GET/POST/etc. request (currently used by curl option only)

## Example

~~~~~
$http->setCookie('PHPSESSID', 'f3943z12339jz93j39iafai3f9393g');
$http->post('http://domain.com', [ 'foo' => 'bar' ], [ 'use' => 'curl' ]);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireHttp->setCookie($name, $value);
~~~~~

## Arguments

- `$name` `string` Name of cookie to set
- `$value` `string|int|null` Specify value to set or null to remove

## Return value

- `self`

## Since

3.0.199
