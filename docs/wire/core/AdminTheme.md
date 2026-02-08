# AdminTheme

Source: `wire/core/AdminTheme.php`

ProcessWire Admin Theme Module

An abstract module intended as a base for admin themes.

See the Module interface (Module.php) for details about each method.

This file is licensed under the MIT license.
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property int|string $version Current admin theme version

@property string $url URL to admin theme

@property string $path Disk path to admin theme

@method void install()

@method void uninstall()

@method array getExtraMarkup()

## getModuleInfo()

Per the Module interface, return an array of information about the Module

## __construct()

Construct

## init()

Initialize the admin theme system and determine which admin theme should be used

All admin themes must call this init() method to register themselves.

Note: this should be called after API ready.

## initConfig()

Initialize configuration properties and JS config for when this is current admin theme

@since 3.0.173

## get()

Get property

@param string $key

@return int|mixed|null|string

## url()

Get URL to this admin theme

@return string

@since 3.0.171

## path()

Get disk path to this admin theme

@return string

@since 3.0.171

## getLabel()

Get predefined translated label by key for labels shared among admin themes

@param string $key

@param string $val Value to return if label not available

@return string

@since 3.0.162

## isCurrent()

Returns true if this admin theme is the one that will be used for this request

## setCurrent()

Set this admin theme as the current one

## ___getExtraMarkup()

Enables hooks to append extra markup to various sections of the admin page

@return array Associative array containing the following properties, any of
which may be populated or empty:
	- head
	- body
	- masthead
	- content
	- footer
	- sidebar

## addExtraMarkup()

Add extra markup to a region in the admin theme

@param string $name

@param string $value

## addBodyClass()

Add a <body> class to the admin theme

@param string $className

## getBodyClass()

Get the body[class] attribute string

@return string

## getClass()

Return class for a given named item or blank if none available

Omit the first argument to return all classes in an array.

@param string $name Tag or item name, i.e. “input”, or omit to return all defined [tags=classes]

@param bool $getArray Specify true to return array of class name(s) rather than string (default=false). $name argument required.

@return string|array Returns string or array of class names, or array of all [tags=classes] or $tagName argument is empty.

## ___install()

Install the admin theme

Other admin themes using an install() method must call this install before their own.
