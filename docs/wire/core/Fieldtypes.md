# Fieldtypes

Source: `wire/core/Fieldtypes.php`

ProcessWire Fieldtypes

Maintains a collection of Fieldtype modules.
$fieldtypes

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## other

@property FieldtypeCheckbox $FieldtypeCheckbox

@property FieldtypeCheckbox $checkbox

@property FieldtypeComments|null $FieldtypeComments

@property FieldtypeComments|null $comments

@property FieldtypeDatetime $FieldtypeDatetime

@property FieldtypeDatetime $datetime

@property FieldtypeEmail $FieldtypeEmail

@property FieldtypeEmail $email

@property FieldtypeFile $file

@property FieldtypeFile $FieldtypeFile

@property FieldtypeFloat $FieldtypeFloat

@property FieldtypeFloat $float

@property FieldtypeImage $FieldtypeImage

@property FieldtypeImage $image

@property FieldtypeInteger $FieldtypeInteger

@property FieldtypeInteger $integer

@property FieldtypeModule $FieldtypeModule

@property FieldtypeModule $module

@property FieldtypeOptions|null $FieldtypeOptions

@property FieldtypeOptions|null $options

@property FieldtypePage $FieldtypePage

@property FieldtypePage $page

@property FieldtypePageTable $FieldtypePageTable

@property FieldtypePageTable $pageTable

@property FieldtypePageTitle $FieldtypePageTitle

@property FieldtypePageTitle $pageTitle

@property FieldtypePassword $FieldtypePassword

@property FieldtypePassword $password

@property FieldtypeRepeater|null $FieldtypeRepeater

@property FieldtypeRepeater|null $repeater

@property FieldtypeSelector|null $FieldtypeSelector

@property FieldtypeSelector|null $selector

@property FieldtypeText $FieldtypeText

@property FieldtypeText $text

@property FieldtypeTextarea $FieldtypeTextarea

@property FieldtypeTextarea $textarea

@property FieldtypeToggle|null $FieldtypeToggle

@property FieldtypeToggle|null $toggle

@property FieldtypeURL $FieldtypeURL

@property FieldtypeURL $URL

## __construct()

Construct

## init()

Construct the $fieldtypes API var (load all Fieldtype modules into it)

## preload()

Convert all ModulePlaceholders to Fieldtype modules

## isValidItem()

Per WireArray interface, items added to Fieldtypes must be Fieldtype instances

@param Wire|Fieldtype $item

@return bool

## isValidKey()

Per the WireArray interface, keys must be strings (fieldtype class names)

@param string|int $key

@return bool

## getItemKey()

Per the WireArray interface, Fields are indxed by their name

@param Fieldtype $item

@return string

## makeBlankItem()

Per the WireArray interface, return a blank copy

Since Fieldtype is abstract, there is nothing but NULL to return here

@return null

## get()

Given a Fieldtype name (or class name) return the instantiated Fieldtype module.

If the requested Fieldtype is not already installed, it will be installed here automatically.

@param string $key Fieldtype name or class name, or dynamic property of Fieldtypes

@return Fieldtype|null

## getArray()

Below we account for all get() related functions in WireArray to preload the fieldtypes

This ensures there are no ModulePlaceholders present when results from any of these methods.
