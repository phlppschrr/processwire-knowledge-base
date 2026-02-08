# $sanitizer->minArray($data, $allowEmpty = false, $convert = false): array

Source: `wire/core/Sanitizer.php`

Minimize an array to remove empty values

## Arguments

- array $data Array to reduce
- bool|array $allowEmpty Should empty values be allowed in the encoded data? Specify any of the following: - `false` (bool): to exclude all empty values (this is the default if not specified). - `true` (bool): to allow all empty values to be retained (thus no point in calling this function). - Specify array of keys (from data) that should be retained if you want some retained and not others. - Specify array of literal empty value types to retain, i.e. [ 0, '0', array(), false, null ] - Specify the digit `0` to retain values that are 0, but not other types of empty values.
- bool $convert Perform type conversions where appropriate? i.e. convert digit-only string to integer (default=false).

## Return value

array
