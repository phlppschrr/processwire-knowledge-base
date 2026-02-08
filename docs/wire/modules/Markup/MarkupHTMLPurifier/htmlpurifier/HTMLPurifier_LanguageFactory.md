# HTMLPurifier_LanguageFactory

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Class responsible for generating HTMLPurifier_Language objects, managing
caching and fallbacks.
@note Thanks to MediaWiki for the general logic, although this version
      has been entirely rewritten
@todo Serialized cache for languages

## setup()

Sets up the singleton, much like a constructor
@note Prevents people from getting this outside of the singleton

## create()

Creates a language object, handles class fallbacks
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@param bool|string $code Code to override configuration with. Private parameter.
@return HTMLPurifier_Language

## getFallbackFor()

Returns the fallback language for language
@note Loads the original language into cache
@param string $code language code
@return string|bool

## loadLanguage()

Loads language into the cache, handles message file and fallbacks
@param string $code language code
