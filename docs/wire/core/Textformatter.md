# Textformatter

Source: `wire/core/Textformatter.php`

ProcessWire Textformatter

Provides the base class for Textformatting Modules

A simple module type that provides formatting of text fields.
Please see the base `Module` interface for all potential methods that a Textformatter module can have.

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## format()

Return an array of module information

Array is associative with the following fields:
- title: An alternate title, if you don't want to use the class name.
- version: an integer that indicates the version number, 101 = 1.0.1
- summary: a summary of the module (1 paragraph max)

@return array

public static function getModuleInfo() {
// just an example, should be overridden
return array(
'title' => 'Unknown Textformatter',
'version' => 0,
'summary' => '',
);
}

## format()

Format the given text string, outside of specific Page or Field context.

@param string $str String is provided as a reference, so is modified directly (not returned).

## formatValue()

Format the given text string with Page and Field provided.

Module developers may override this function completely when providing your own text formatter. No need to call the parent.

@param Page $page

@param Field $field

@param string|mixed $value Value is provided as a reference, so is modified directly (not returned).
