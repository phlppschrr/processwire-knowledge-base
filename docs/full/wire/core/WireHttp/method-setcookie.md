# $wireHttp->setCookie($name, $value): self

Source: `wire/core/WireHttp.php`

Set cookie(s) for http GET/POST/etc. request (currently used by curl option only)

~~~~~
$http->setCookie('PHPSESSID', 'f3943z12339jz93j39iafai3f9393g');
$http->post('http://domain.com', [ 'foo' => 'bar' ], [ 'use' => 'curl' ]);
~~~~~

## Arguments

- string $name Name of cookie to set
- string|int|null $value Specify value to set or null to remove

## Return value

self

## Meta

- @since 3.0.199
