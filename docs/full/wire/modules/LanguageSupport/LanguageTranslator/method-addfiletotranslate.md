# $languageTranslator->addFileToTranslate($filename, $filenameIsTextdomain = false, $save = true): string|bool

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Given a source file to translate, create a new textdomain

## Arguments

- string $filename Filename or textdomain that we will be translating, relative to site root.
- bool $filenameIsTextdomain Specify true if $filename is a textdomain instead.
- bool $save Whether to save the language

## Return value

string|bool Returns textdomain string if successful, or false if not.
