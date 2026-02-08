# $modulesDuplicates->getDuplicates($className = ''): array

Source: `wire/core/ModulesDuplicates.php`

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

## Arguments

- string|Module|int $className Optionally return only duplicates for given module name

## Return value

array
