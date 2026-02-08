# FieldsArray

Source: `wire/core/FieldsArray.php`

ProcessWire Fields Array

WireArray of Field instances, as used by Fields class

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## isValidItem()

Per WireArray interface, only Field instances may be added

@param Wire $item

@return bool

## isValidKey()

Per WireArray interface, Field keys have to be integers

@param int $key

@return bool

## getItemKey()

Per WireArray interface, Field instances are keyed by their ID

@param Field $item

@return int

## makeBlankItem()

Per WireArray interface, return a blank Field

@return Field
