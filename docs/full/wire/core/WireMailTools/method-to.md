# WireMailTools::to()

Source: `wire/core/WireMailTools.php`

Return new WireMail instance populated with “to” email

@param string|array $email Email to send to–specify any one of the following:
- Single email address
- String like: "John Smith <user@example.com>"
- CSV string of either of the above.
- Regular PHP array of email addresses.
- Associative array of ['user@xample.com' => 'John Smith'].

@param string $name An optional TO name, applies only if your $email argument was just an email address.

@return WireMail

@throws WireException if given invalid email address

@since 3.0.113
