# Language

Source: `wire/modules/LanguageSupport/Language.php`

Inherits: `Page`

## Summary

A type of Page that represents a single Language in ProcessWire

Common methods:
- [`wired()`](method-wired.md)
- [`get()`](method-get.md)
- [`translator()`](method-translator.md)
- [`setIsDefaultLanguage()`](method-setisdefaultlanguage.md)
- [`isDefault()`](method-isdefault.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`__construct(?Template $tpl = null)`](method-__construct.md) Construct a new Language instance
- [`wired()`](method-wired.md) Wired to API
- [`isDefault(): bool`](method-isdefault.md) Returns whether or not this is the default language
- [`isCurrent(): bool`](method-iscurrent.md) Returns whether or not this is the current user’s language
- [`getLocale(int $category = LC_ALL): string|bool`](method-getlocale.md) Get locale for this language
- [`setLocale(int $category = LC_ALL): string|bool`](method-setlocale.md) Set the current locale to use settings defined for this language
