# LanguagesValueInterface

Source: `wire/core/Interfaces.php`

## Summary

Interface LanguagesValueInterface

Common methods:
- [`setLanguageValue()`](method-setlanguagevalue.md)
- [`getLanguageValue()`](method-getlanguagevalue.md)
- [`setFromInputfield()`](method-setfrominputfield.md)

Interface for multi-language fields

## Methods
- [`setLanguageValue(int|Language $languageID, mixed $value)`](method-setlanguagevalue.md) Sets the value for a given language
- [`getLanguageValue($languageID): string|mixed`](method-getlanguagevalue.md) Given a language, returns the value in that language
- [`setFromInputfield(Inputfield $inputfield)`](method-setfrominputfield.md) Given an Inputfield with multi language values, this grabs and populates the language values from it
