# $wireMailTools->to($email, $name = null): WireMail

Source: `wire/core/WireMailTools.php`

Return new WireMail instance populated with “to” email

## Arguments

- `$email` `string|array` Email to send to–specify any one of the following: - Single email address - String like: "John Smith <user@example.com>" - CSV string of either of the above. - Regular PHP array of email addresses. - Associative array of ['user@xample.com' => 'John Smith'].
- `$name` (optional) `string` An optional TO name, applies only if your $email argument was just an email address.

## Return value

WireMail

## Throws

- WireException if given invalid email address

## Since

3.0.113
