# Sanitizer::punyDecodeName()

Source: `wire/core/Sanitizer.php`

Decode a PW-punycode'd name value

@param string $value

@param int $version 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

@return string
