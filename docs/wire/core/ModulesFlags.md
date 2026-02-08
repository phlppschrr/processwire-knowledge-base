# ModulesFlags

Source: `wire/core/ModulesFlags.php`

ProcessWire Modules: Flags

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## moduleFlags()

Get or set flags for module by module ID

Omit all arguments to get flags for all modules indexed by module ID.

Returns null if given module ID not found.

@param int $moduleID This method only accepts module ID

@param int $setValue Flag(s) to set

@return array|mixed|null

## getFlags()

Get flags for the given module

@param int|string|Module $id Module to add flag to

@return int|false Returns integer flags on success, or boolean false on fail

## updateModuleFlags()

Update module flags if any happen to differ from what's in the given moduleInfo

@param int $moduleID

@param array $info
