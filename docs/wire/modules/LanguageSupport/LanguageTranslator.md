# LanguageTranslator

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

ProcessWire Language Translator

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct the translator and set the current language

@param Language $currentLanguage

## setCurrentLanguage()

Set the current language and reset current stored textdomains

@param Language $language

@return $this

## textdomainTemplate()

Return the array template for a textdomain, optionally populating it with data

@param string $file

@param string $textdomain

@param array $translations

@return array

## objectToTextdomain()

Given an object instance, return the resulting textdomain string

This is accomplished with PHP's ReflectionClass to determine the file where the class lives
and then convert that to a textdomain string. Once determined, we cache it so that we
don't have to do this again.

@param Wire|object $o

@return string

## filenameToTextdomain()

Given a filename, convert it to a textdomain string

@param string $filename

@return string

## textdomainToFilename()

Given a textdomain string, convert it to a filename (relative to site root)

This is determined by loading the textdomain and then grabbing the filename stored in the JSON properties

@param string $textdomain

@return string

## textdomainString()

Normalize a string, filename or object to be a textdomain string

@param string|object $textdomain

@return string

@since 3.0.154 was protected in prior versions

## getTranslation()

Perform a translation in the given $textdomain for $text to the current language

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options 3.0.237+ only
 - `getInfo` (bool): Get verbose array of info about translation? (default=false)
 - `getFalse` (bool): Return false rather than default language value if translation not found? (default=false)

@return string|array|false Translation if available, or original EN version if translation not available.
 - Returns array if options[getInfo] is true.
 - Returns false if translation not found and options[getFalse] is true.

## ___getTranslation()

Implementation for the getTranslation() function - you should call getTranslation() without underscores instead.

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options 3.0.237+ only
 - `getInfo` (bool): Get verbose array of info about translation? (default=false)
 - `getFalse` (bool): Return false rather than default language value if translation not found? (default=false)

@return string|array|false Translation if available, or original EN version if translation not available.
 - Returns array if options[getInfo] is true.
 - Returns false if translation not found and options[getFalse] is true.

## getTranslationInfo()

Get verbose array of information about translation

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options

@return array

@since 3.0.237

## getTranslationOrFalse()

Get translated text or boolean false if not translated (rather than default language value)

@param string|object $textdomain Textdomain string, filename, or object.

@param string $text Text in default language (EN) that needs to be converted to current language.

@param string $context Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.

@param array $options

@return string|false

@since 3.0.237

## getTranslations()

Return ALL translations for the given textdomain

@param string|object $textdomain Textdomain string, filename, or object.

@return array

## findTranslations()

Find all translation(s) for given text

Scans all textdomains to find translations.

@param string $text

@param string|array $context
  - Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
  - If context is not needed you may optionally specify the $options array here.

@param array $options
 - `getInfo` (bool): Return verbose array of information for each found translation? (default=false)
 - `limit` (int): Limit to this many results or 0 for no maximum (default=0)

@return array
 - Returns array of strings containing translations of given text.
 - Returns array of arrays, each with verbose info, if getInfo option requested.

@since 3.0.237

## findTranslation()

Find a translation for given text

Scans all textdomains to find first translation.

@param string $text

@param string|array $context
  - Optional context label for the text, to differentiate from others that may be the same in English, but not other languages.
  - If context is not needed you may optionally specify the $options array here.

@param array $options
 - `getInfo` (bool): Return verbose array of information about found translation? (default=false)

@return string|array
  - Returns string with translated text if found, or blank string if not found.
  - Returns array of info if getInfo option requested. This array is empty if translation was not found.

@since 3.0.237

## setTranslation()

Set a translation

@param string $textdomain

@param string $text

@param string $translation

@param string $context

@return string

## setTranslationFromHash()

Set a translation using an already known hash

@param string $textdomain

@param string $hash

@param string $translation

@return string

## removeTranslation()

Remove a translation

@param string $textdomain

@param string $hash May be the translation hash or the translated text.

@return $this

## getTextHash()

Given original $text, issue a unique MD5 key used to reference it

@param string $text

@return string

## getTextdomainTranslationFile()

Get the JSON filename where the current languages class translations are

@param string $textdomain

@return string

## textdomainFileExists()

Does a json translation file exist for the given textdomain?

@param string $textdomain

@return bool

## loadTextdomain()

Load translation group $textdomain into the current language translations

@param string $textdomain

@return $this

## addFileToTranslate()

Given a source file to translate, create a new textdomain

@param string $filename Filename or textdomain that we will be translating, relative to site root.

@param bool $filenameIsTextdomain Specify true if $filename is a textdomain instead.

@param bool $save Whether to save the language

@return string|bool Returns textdomain string if successful, or false if not.

## saveTextdomain()

Save the translation group given by $textdomain to disk in its translation file

@param string $textdomain

@return int|bool Number of bytes written or false on failure

## unloadTextdomain()

Unload the given textdomain string from memory

@param string $textdomain

## getTextdomain()

Return the data available for the given $textdomain string

@param string $textdomain

@return array

## encodeJSON()

JSON encode language translation data

@param array|string $value

@return string

## commonTranslation()

Get a common translation

These are commonly used translations that can be used as fallbacks.

Returns blank string if given string is not a common phrase.
Returns given $str if given string is common, but not translated here.
Returns translated $str if common and translated.

@param string $str

@return string
