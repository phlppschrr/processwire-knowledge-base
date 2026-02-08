# Sanitizer::punyEncodeName()

Source: `wire/core/Sanitizer.php`

Encode a name value to PW-punycode

@param string $value

@param int $version 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

@return string
