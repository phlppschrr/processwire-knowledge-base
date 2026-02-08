# SelectableOption

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOption.php`

ProcessWire Selectable Option class, for FieldtypeOptions

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property int $id

@property int $sort

@property string $title

@property string $value

## of()

Turn output formatting on or off, or get current value

@param null|bool $of Omit to return current value, or specify true|false to set

@return bool

## values()

Return all values stored in this SelectableOption

@param bool $returnHash Makes it return a string hash of all values

@return string|array

## getProperty()

Get the language-aware property

@param string $property Either 'title' or 'value'

@return string

## getValue()

Get the language-aware value

@return string

## getTitle()

Get the language-aware title

@return string
