# $wireMail->extractEmailAndName($email): array()

Source: `wire/core/WireMail.php`

Given an email string like "User <user@example.com>" extract and return email and username separately

## Usage

~~~~~
// basic usage
$result = $wireMail->extractEmailAndName($email);
~~~~~

## Arguments

- `$email` `string`

## Return value

- `array()` Index 0 contains email, index 1 contains username or blank if not set
