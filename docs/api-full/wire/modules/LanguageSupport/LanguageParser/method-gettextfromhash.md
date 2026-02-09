# $languageParser->getTextFromHash($hash): string|bool

Source: `wire/modules/LanguageSupport/LanguageParser.php`

Given a hash, return the untranslated text associated with it

## Usage

~~~~~
// basic usage
$string = $languageParser->getTextFromHash($hash);
~~~~~

## Arguments

- `$hash` `string`

## Return value

- `string|bool` Returns untranslated text (string) on success or boolean false if not available
