# LanguageTranslator

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Inherits: `Wire`

ProcessWire Language Translator

Methods:
- [`__construct(Language $currentLanguage)`](method-__construct.md) Construct the translator and set the current language
- [`setCurrentLanguage(Language $language): $this`](method-setcurrentlanguage.md) Set the current language and reset current stored textdomains
- [`textdomainTemplate(string $file = '', string $textdomain = '', array $translations = array()): array`](method-textdomaintemplate.md) Return the array template for a textdomain, optionally populating it with data
- [`objectToTextdomain(Wire|object $o): string`](method-objecttotextdomain.md) Given an object instance, return the resulting textdomain string
- [`filenameToTextdomain(string $filename): string`](method-filenametotextdomain.md) Given a filename, convert it to a textdomain string
- [`textdomainToFilename(string $textdomain): string`](method-textdomaintofilename.md) Given a textdomain string, convert it to a filename (relative to site root)
- [`textdomainString(string|object $textdomain): string`](method-textdomainstring.md) Normalize a string, filename or object to be a textdomain string
- [`getTranslation(string|object $textdomain, string $text, string $context = '', array $options = array()): string|array|false`](method-gettranslation.md) Perform a translation in the given $textdomain for $text to the current language
- [`getTranslation(string|object $textdomain, string $text, string $context = '', array $options = array()): string|array|false`](method-___gettranslation.md) (hookable) Implementation for the getTranslation() function - you should call getTranslation() without underscores instead.
- [`getTranslationInfo(string|object $textdomain, string $text, string $context = '', array $options = array()): array`](method-gettranslationinfo.md) Get verbose array of information about translation
- [`getTranslationOrFalse(string|object $textdomain, string $text, string $context = '', array $options = array()): string|false`](method-gettranslationorfalse.md) Get translated text or boolean false if not translated (rather than default language value)
- [`getTranslations(string|object $textdomain): array`](method-gettranslations.md) Return ALL translations for the given textdomain
- [`findTranslations(string $text, string|array $context = '', array $options = array()): array`](method-findtranslations.md) Find all translation(s) for given text
- [`findTranslation(string $text, string|array $context = '', array $options = array()): string|array`](method-findtranslation.md) Find a translation for given text
- [`setTranslation(string $textdomain, string $text, string $translation, string $context = ''): string`](method-settranslation.md) Set a translation
- [`setTranslationFromHash(string $textdomain, string $hash, string $translation): string`](method-settranslationfromhash.md) Set a translation using an already known hash
- [`removeTranslation(string $textdomain, string $hash): $this`](method-removetranslation.md) Remove a translation
- [`getTextHash(string $text): string`](method-gettexthash.md) Given original $text, issue a unique MD5 key used to reference it
- [`getTextdomainTranslationFile(string $textdomain): string`](method-gettextdomaintranslationfile.md) Get the JSON filename where the current languages class translations are
- [`textdomainFileExists(string $textdomain): bool`](method-textdomainfileexists.md) Does a json translation file exist for the given textdomain?
- [`loadTextdomain(string $textdomain): $this`](method-loadtextdomain.md) Load translation group $textdomain into the current language translations
- [`addFileToTranslate(string $filename, bool $filenameIsTextdomain = false, bool $save = true): string|bool`](method-addfiletotranslate.md) Given a source file to translate, create a new textdomain
- [`saveTextdomain(string $textdomain): int|bool`](method-savetextdomain.md) Save the translation group given by $textdomain to disk in its translation file
- [`unloadTextdomain(string $textdomain)`](method-unloadtextdomain.md) Unload the given textdomain string from memory
- [`getTextdomain(string $textdomain): array`](method-gettextdomain.md) Return the data available for the given $textdomain string
- [`encodeJSON(array|string $value): string`](method-encodejson.md) JSON encode language translation data
- [`commonTranslation(string $str): string`](method-commontranslation.md) Get a common translation
