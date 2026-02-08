# WireMail::extractEmailAndName()

Source: `wire/core/WireMail.php`

Given an email string like "User <user@example.com>" extract and return email and username separately

@param string $email

@return array() Index 0 contains email, index 1 contains username or blank if not set
