# Language

Source: `wire/modules/LanguageSupport/Language.php`

A type of Page that represents a single Language in ProcessWire

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property LanguageTranslator $translator Get instance of LanguageTranslator for this language

@property bool $isDefault Is this the default language?

@property bool $isCurrent Is this the current language?

@property Pagefiles $language_files Language translation files for /wire/ (language pack)

@property Pagefiles $language_files_site Language translation files for /site/ (custom translations per site)

## __construct()

Construct a new Language instance

@param Template|null $tpl

## wired()

Wired to API

## isDefault()

Returns whether or not this is the default language

@return bool

## isCurrent()

Returns whether or not this is the current user’s language

@return bool

## getLocale()

Get locale for this language

See the `Languages::getLocale()` method for full details.

@param int $category Optional category (default=LC_ALL)

@return string|bool

@see Languages::setLocale()

## setLocale()

Set the current locale to use settings defined for this language

See the `Languages::setLocale()` method for full details.

@param int $category Optional category (default=LC_ALL)

@return string|bool Returns the locale that was set or boolean false if requested locale cannot be set.

@see Languages::setLocale()
