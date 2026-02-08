# WireAction

Source: `wire/core/WireAction.php`

WireAction

Base class for actions in ProcessWire

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@method bool action($item)

@method int executeMultiple($items)

@method InputfieldWrapper getConfigInputfields()

## __construct()

Define any default values for configuration

## init()

Module initialization

## getItemType()

Return the string type (class name) of items that this action operates upon

@return string

## isValidItem()

Is the given item valid for use by this action?

@param object $item

@return bool True if valid, false if not

## ___action()

Perform the action on the given item

@param Wire $item Item to operate upon

@return bool True if the item was successfully operated upon, false if not.

## execute()

Execute the action for the given item

@param Wire $item Item to operate upon

@return bool True if the item was successfully operated upon, false if not.

## ___executeMultiple()

Execute the action for multiple items at once

@param array|WireArray $items Items to operate upon

@return int Returns quantity of items successfully operated upon

@throws WireException when it receives an unexpected type for $items

## ___getConfigInputfields()

Return any Inputfields needed to configure this action

@return InputfieldWrapper

## setRunner()

Set the object instance that is running this action

If an action knows that it only accepts a certain type of runner, then
it should throw a WireException if the given runner is not valid.

@param Wire $runner

## getRunner()

Get the object instance that is running this action

Actions should not generally depend on a particular runner, but should take advantage
of a specific runner if it benefits the action.

@return Wire|null Returns null if no runner has been set

## summary()

Get or set a text summary of what this action did

@param string|null $text Set the summary or omit to only retrieve the summary

@return string Always returns the current summary text or blank string if not set
