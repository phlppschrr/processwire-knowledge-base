# InputfieldTinyMCEConfigs

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEConfigs.php`

InputfieldTinyMCEConfigHelper

Helper for managing configuration settings in TinyMCE

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## label()

Get shared text label

@param string $name

@return string

## getMceToolbars()

Get TinyMCE toolbar names and details

Returns array of arrays or array of strings

@param bool $splitToArray Specify false to return array of strings

@return array|string[]

## getSkinOptions()

Get skin options (array of name => label)

@return string[]

## getContentCssOptions()

Get content_css options (array of name=label)

@return string[]

## getFeaturesOptions()

Get features options

@return array[]

## getConfigInputfields()

Get field configuration

@param InputfieldWrapper $inputfields

@return InputfieldFieldset

## getModuleConfigInputfields()

Module configuration

@param InputfieldWrapper $inputfields

## getOtherTinyMCEFields()

Get other textarea fields that are using TinyMCE

@return array

## configStyleFormatsCSS()

@return InputfieldTextarea

## addPlugin()

Add an external plugin .js file

@param string $file File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

@throws WireException

## removePlugin()

Remove an external plugin .js file

@param string $file File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

@return bool

## ckeToMceToolbar()

Convert CKE toolbar to MCE (future use)

@param string $value

@return string
