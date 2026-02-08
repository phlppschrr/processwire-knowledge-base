# LanguagesPageFieldValue

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Serves as a multi-language value placeholder for field values that contain a value in more than one language.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## langBlankInheritDefault

Inherit default language value when blank

## langBlankInheritNone

Don't inherit any value when blank

## __construct()

Construct the multi language value

@param Page|null $page

@param Field|null $field

@param array|string $values

## wired()

Wired to API

## setLanguageValue()

Sets the value for a given language

@param int|Language|string $languageID Language object, id, or name

@param mixed $value

@return $this

## setLanguageValues()

Set multiple language values at once

~~~~~
$page->title->setLanguageValues([
 'default' => 'Hello world',
 'es' => 'Hola Mundo',
 'fr' => 'Hei maailma',
]);
~~~~~

@param array $values Associative array of values where keys are language names or IDs.

@param bool $reset Reset any languages not specified to blank? (default=false)

@return self

@since 3.0.236

## setFromInputfield()

Grab language values from Inputfield and populate to this object

@param Inputfield $inputfield

## setToInputfield()

Populate language values from this object to given Inputfield

@param Inputfield $inputfield

@since 3.0.170

## getLanguageValue()

Given a language, returns the value in that language

@param Language|int|string Language object, id, or name

@return string|mixed

## getDefaultValue()

Returns the value in the default language

@return string

## getNonEmptyValue()

Get non-empty value in this order: current lang, default lang, other lang, failValue

@param string $failValue Value to use if we cannot find a non-empty value

@return string

@since 3.0.147

## __toString()

The string value is the value in the current user's language

@return string

## ___getStringValue()

Get string value (for hooks)


@return string

## setField()

Set field that value is for

@param Field $field

## setPage()

Set page that value is for

@param Page $page

## getPage()

Get page that value is for

@return Page|null

## getField()

Get field that value is for

@return Field|null

## __debugInfo()

Debug info

@return array

## getArray()

Get array of language values stored in here

@return array

@since 3.0.188

## getHash()

Get hash of all language values stored in here

@param bool $verbose Specify true for the hash to also include page and field

@return string

@since 3.0.188

## getIterator()

Allows iteration of the languages values

Fulfills \IteratorAggregate interface.

@return \ArrayObject

## languageSupport()

@return null|LanguageSupport

@throws WireException

@throws WirePermissionException

## defaultLanguagePageID()

@return int
