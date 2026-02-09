# $languagesPageFieldValue->getHash($verbose = false): string

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Get hash of all language values stored in here

## Usage

~~~~~
// basic usage
$string = $languagesPageFieldValue->getHash();

// usage with all arguments
$string = $languagesPageFieldValue->getHash($verbose = false);
~~~~~

## Arguments

- `$verbose` (optional) `bool` Specify true for the hash to also include page and field

## Return value

- `string`

## Since

3.0.188
