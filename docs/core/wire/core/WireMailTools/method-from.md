# $wireMailTools->from($email, $name = null): WireMail

Source: `wire/core/WireMailTools.php`

Return new WireMail instance populated with “from” email

## Usage

~~~~~
// basic usage
$wireMail = $wireMailTools->from($email);

// usage with all arguments
$wireMail = $wireMailTools->from($email, $name = null);
~~~~~

## Arguments

- `$email` `string` Must be a single email address or "User Name <user@example.com>" string.
- string|null An optional FROM name

## Return value

- `WireMail`

## Since

3.0.113
