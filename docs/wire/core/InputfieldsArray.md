# InputfieldsArray

Source: `wire/core/InputfieldsArray.php`

A WireArray of Inputfield instances, as used by InputfieldWrapper.

The default numeric indexing of a WireArray is not overridden.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## isValidItem()

Per WireArray interface, only Inputfield instances are accepted.

@param Wire $item

@return bool

## find()

Extends the find capability of WireArray to descend into the Inputfield children

@param string $selector

@return WireArray|InputfieldsArray
