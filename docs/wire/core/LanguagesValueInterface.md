# LanguagesValueInterface

Source: `wire/core/Interfaces.php`

Interface LanguagesValueInterface

Interface for multi-language fields

## setLanguageValue()

Sets the value for a given language

@param int|Language $languageID

@param mixed $value

## getLanguageValue()

Given a language, returns the value in that language

@param Language|int

@return string|mixed

## setFromInputfield()

Given an Inputfield with multi language values, this grabs and populates the language values from it

@param Inputfield $inputfield
