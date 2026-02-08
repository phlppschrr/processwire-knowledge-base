# Sanitizer::filterValidateURL()

Source: `wire/core/Sanitizer.php`

Implementation of PHP's FILTER_VALIDATE_URL with IDN and underscore support (will convert to valid)

Example: http://трикотаж-леко.рф

@param string $url

@param array $options Specify ('allowIDN' => false) to disallow internationalized domain names

@return string
