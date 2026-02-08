# $sanitizer->filterValidateURL($url, array $options): string

Source: `wire/core/Sanitizer.php`

Implementation of PHP's FILTER_VALIDATE_URL with IDN and underscore support (will convert to valid)

Example: http://трикотаж-леко.рф

## Arguments

- `$url` `string`
- `$options` `array` Specify ('allowIDN' => false) to disallow internationalized domain names

## Return value

string
