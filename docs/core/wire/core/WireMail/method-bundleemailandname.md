# $wireMail->bundleEmailAndName($email, $name): string

Source: `wire/core/WireMail.php`

Given an email and name, bundle it to an RFC 2822 string

If name is blank, then just the email will be returned

## Usage

~~~~~
// basic usage
$string = $wireMail->bundleEmailAndName($email, $name);
~~~~~

## Arguments

- `$email` `string`
- `$name` `string`

## Return value

- `string`
