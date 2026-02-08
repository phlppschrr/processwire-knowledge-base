# WireMail::from()

Source: `wire/core/WireMail.php`

Set the email 'from' address and optionally name

@param string $email Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional FROM name (same as setting/calling fromName)

@return $this

@throws WireException if provided email was invalid or in blacklist
