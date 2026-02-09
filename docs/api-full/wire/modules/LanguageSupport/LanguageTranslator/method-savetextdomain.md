# $languageTranslator->saveTextdomain($textdomain): int|bool

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Save the translation group given by $textdomain to disk in its translation file

## Usage

~~~~~
// basic usage
$int = $languageTranslator->saveTextdomain($textdomain);
~~~~~

## Arguments

- `$textdomain` `string`

## Return value

- `int|bool` Number of bytes written or false on failure
