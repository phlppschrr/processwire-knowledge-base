# $wireMailTools->to($email, $name = null): WireMail

Source: `wire/core/WireMailTools.php`

Return new WireMail instance populated with “to” email

## Arguments

- string|array $email Email to send to–specify any one of the following: - Single email address - String like: "John Smith <user@example.com>" - CSV string of either of the above. - Regular PHP array of email addresses. - Associative array of ['user@xample.com' => 'John Smith'].
- string $name An optional TO name, applies only if your $email argument was just an email address.

## Return value

WireMail

## Throws

- WireException if given invalid email address

## Meta

- @since 3.0.113
