# WireMail::replyTo()

Source: `wire/core/WireMail.php`

Set the 'reply-to' email address and optionally name (where supported)

@param string $email Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional Reply-To name (same as setting/calling replyToName method)

@return $this

@throws WireException if provided email was invalid or in blacklist
