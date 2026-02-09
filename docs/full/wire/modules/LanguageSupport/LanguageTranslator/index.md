# LanguageTranslator

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Inherits: `Wire`

ProcessWire Language Translator

Methods:
- [`__construct(Language $currentLanguage)`](method-__construct.md)
- [`setCurrentLanguage(Language $language): $this`](method-setcurrentlanguage.md)
- [`textdomainTemplate(string $file = '', string $textdomain = '', array $translations = array()): array`](method-textdomaintemplate.md)
- [`objectToTextdomain(Wire|object $o): string`](method-objecttotextdomain.md)
- [`filenameToTextdomain(string $filename): string`](method-filenametotextdomain.md)
- [`textdomainToFilename(string $textdomain): string`](method-textdomaintofilename.md)
- [`textdomainString(string|object $textdomain): string`](method-textdomainstring.md)
- [`getTranslation(string|object $textdomain, string $text, string $context = '', array $options = array()): string|array|false`](method-gettranslation.md)
- [`getTranslation(string|object $textdomain, string $text, string $context = '', array $options = array()): string|array|false`](method-___gettranslation.md) (hookable)
- [`getTranslationInfo(string|object $textdomain, string $text, string $context = '', array $options = array()): array`](method-gettranslationinfo.md)
- [`getTranslationOrFalse(string|object $textdomain, string $text, string $context = '', array $options = array()): string|false`](method-gettranslationorfalse.md)
- [`getTranslations(string|object $textdomain): array`](method-gettranslations.md)
- [`findTranslations(string $text, string|array $context = '', array $options = array()): array`](method-findtranslations.md)
- [`findTranslation(string $text, string|array $context = '', array $options = array()): string|array`](method-findtranslation.md)
- [`setTranslation(string $textdomain, string $text, string $translation, string $context = ''): string`](method-settranslation.md)
- [`setTranslationFromHash(string $textdomain, string $hash, string $translation): string`](method-settranslationfromhash.md)
- [`removeTranslation(string $textdomain, string $hash): $this`](method-removetranslation.md)
- [`getTextHash(string $text): string`](method-gettexthash.md)
- [`getTextdomainTranslationFile(string $textdomain): string`](method-gettextdomaintranslationfile.md)
- [`textdomainFileExists(string $textdomain): bool`](method-textdomainfileexists.md)
- [`loadTextdomain(string $textdomain): $this`](method-loadtextdomain.md)
- [`addFileToTranslate(string $filename, bool $filenameIsTextdomain = false, bool $save = true): string|bool`](method-addfiletotranslate.md)
- [`saveTextdomain(string $textdomain): int|bool`](method-savetextdomain.md)
- [`unloadTextdomain(string $textdomain)`](method-unloadtextdomain.md)
- [`getTextdomain(string $textdomain): array`](method-gettextdomain.md)
- [`encodeJSON(array|string $value): string`](method-encodejson.md)
- [`commonTranslation(string $str): string`](method-commontranslation.md)
