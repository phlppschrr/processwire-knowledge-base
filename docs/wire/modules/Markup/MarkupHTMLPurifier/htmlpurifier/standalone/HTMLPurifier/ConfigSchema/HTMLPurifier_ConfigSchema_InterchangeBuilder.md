# HTMLPurifier_ConfigSchema_InterchangeBuilder

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/ConfigSchema/InterchangeBuilder.php`


## __construct()

Used for processing DEFAULT, nothing else.
@type HTMLPurifier_VarParser
/
protected $varParser;

/**
@param HTMLPurifier_VarParser $varParser

## buildFromDirectory()

@param string $dir
@return HTMLPurifier_ConfigSchema_Interchange

## buildDir()

@param HTMLPurifier_ConfigSchema_Interchange $interchange
@param string $dir
@return HTMLPurifier_ConfigSchema_Interchange

## buildFile()

@param HTMLPurifier_ConfigSchema_Interchange $interchange
@param string $file

## build()

Builds an interchange object based on a hash.
@param HTMLPurifier_ConfigSchema_Interchange $interchange HTMLPurifier_ConfigSchema_Interchange object to build
@param HTMLPurifier_StringHash $hash source data
@throws HTMLPurifier_ConfigSchema_Exception

## buildDirective()

@param HTMLPurifier_ConfigSchema_Interchange $interchange
@param HTMLPurifier_StringHash $hash
@throws HTMLPurifier_ConfigSchema_Exception

## evalArray()

Evaluates an array PHP code string without array() wrapper
@param string $contents

## lookup()

Converts an array list into a lookup array.
@param array $array
@return array

## id()

Convenience function that creates an HTMLPurifier_ConfigSchema_Interchange_Id
object based on a string Id.
@param string $id
@return HTMLPurifier_ConfigSchema_Interchange_Id

## _findUnused()

Triggers errors for any unused keys passed in the hash; such keys
may indicate typos, missing values, etc.
@param HTMLPurifier_StringHash $hash Hash to check.
