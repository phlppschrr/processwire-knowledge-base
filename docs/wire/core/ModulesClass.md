# ModulesClass

Source: `wire/core/ModulesClass.php`

ProcessWire Modules: Class

Base for Modules helper classes.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Modules $modules

## moduleID()

Convert given value to module ID

@param string|int|Module $name

@return int Returns 0 if module not found

## moduleName()

Convert given value to module name

@param int|string|Module $id

@return string Returns blank string if not found

## log()

Save to the modules log

@param string $str Message to log

@param array|string $options Specify module name (string) or options array

@return WireLog
