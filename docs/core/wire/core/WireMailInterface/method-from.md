# WireMailInterface::from()

Source: `wire/core/WireMailInterface.php`

Set the email from address

@param string Must be a single email address or "User Name <user@example.com>" string.

@param string|null An optional FROM name (same as setting/calling fromName)

@return self

@throws WireException if provided email was invalid
