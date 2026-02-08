# $languagesPageFieldValue->getNonEmptyValue($failValue = ''): string

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Get non-empty value in this order: current lang, default lang, other lang, failValue

## Usage

~~~~~
// basic usage
$string = $languagesPageFieldValue->getNonEmptyValue();

// usage with all arguments
$string = $languagesPageFieldValue->getNonEmptyValue($failValue = '');
~~~~~

## Arguments

- `$failValue` (optional) `string` Value to use if we cannot find a non-empty value

## Return value

- `string`

## Since

3.0.147
