# $languageTranslator->addFileToTranslate($filename, $filenameIsTextdomain = false, $save = true): string|bool

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Given a source file to translate, create a new textdomain

## Usage

~~~~~
// basic usage
$string = $languageTranslator->addFileToTranslate($filename);

// usage with all arguments
$string = $languageTranslator->addFileToTranslate($filename, $filenameIsTextdomain = false, $save = true);
~~~~~

## Arguments

- `$filename` `string` Filename or textdomain that we will be translating, relative to site root.
- `$filenameIsTextdomain` (optional) `bool` Specify true if $filename is a textdomain instead.
- `$save` (optional) `bool` Whether to save the language

## Return value

- `string|bool` Returns textdomain string if successful, or false if not.
