# $pagesType->__construct(ProcessWire $wire, $templates = array(), $parents = array())

Source: `wire/core/PagesType.php`

Construct this PagesType manager for the given parent and template

## Usage

~~~~~
// basic usage
$result = $pagesType->__construct($wire);

// usage with all arguments
$result = $pagesType->__construct(ProcessWire $wire, $templates = array(), $parents = array());
~~~~~

## Arguments

- `$wire` `ProcessWire`
- `$templates` (optional) `Template|int|string|array` Template object or array of template objects, names or IDs
- `$parents` (optional) `int|Page|array` Parent ID or array of parent IDs (may also be Page or array of Page objects)
