# ModulesDuplicates

Source: `wire/core/ModulesDuplicates.php`

ProcessWire Modules Duplicates

Provides functions for managing sitautions where more than one
copy of the same module is intalled. This is a helper for the Modules class.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## numNewDuplicates()

Return quantity of new duplicates found while loading modules

@return int

## getCurrent()

Get the current duplicate in use (string) or null if not specified

@param $className

@return string|null Pathname or null

## hasDuplicate()

Does the given module class have a duplicate?

@param string $className

@param string $pathname Optionally specify the duplicate to check

@return bool

## addDuplicate()

Add a duplicate to the list

@param $className

@param $pathname

@param bool $current Is this the current one in use?

## addDuplicates()

Add multiple duplicates

@param $className

@param array $files

## addFromConfigData()

Add duplicates from module config data

@param $className

@param array $data

## getDuplicates()

Return a list of duplicate modules that were found

If given a module className, the following is returned:

Array(
   'files' => array(file1, file2, ...)
   'using' => '/path/to/file/from/pw/root/ModuleName.module' or blank if not defined
)

If no className is specivied, the following is returned:

Array(
   'ModuleName' => array(file1, file2, ...),
   'ModuleName' => array(file1, file2, ...),
   ...and so on...
)

@param string|Module|int $className Optionally return only duplicates for given module name

@return array

## setUseDuplicate()

For a module that has duplicates, tell it which file to use

@param string $className

@param string $pathname Full path and filename to module file

@throws WireException if given information that can't be resolved

## updateDuplicates()

Update the database so that modules have information on their duplicates

## recordDuplicate()

Record a duplicate at runtime

@param string $basename Name of module

@param string $pathname Path of module

@param string $pathname2 Second path of module

@param array $installed Installed module info array

## getDuplicatesConfigData()

Populate duplicates info into config data, when applicable

@param $className

@param array $configData

@return array Updated configData
