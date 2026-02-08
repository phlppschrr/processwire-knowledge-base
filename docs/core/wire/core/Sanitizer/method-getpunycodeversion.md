# Sanitizer::getPunycodeVersion()

Source: `wire/core/Sanitizer.php`

Get internal Punycode version to use

0: Auto-detect from current environment.
1: PHP IDN function used by all PW versions prior to 3.0.244, but buggy PHP 7.4+.
2: Dedicated Punycode PHP library (no known issues at present).
3: PHP IDN function call updated for PHP 7.4+ (default in new installations after January 2025).

@param int $version

@return int 1=PHP DN but buggy after PHP 7.4+, 2=Punycode library, 3=PHP IDN function PHP 7.4+

@since 3.0.244
