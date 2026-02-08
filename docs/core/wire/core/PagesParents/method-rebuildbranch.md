# $pagesParents->rebuildBranch($fromParent): int

Source: `wire/core/PagesParents.php`

Rebuild pages_parents branch starting at $fromParent and into all descendents

## Usage

~~~~~
// basic usage
$int = $pagesParents->rebuildBranch($fromParent);
~~~~~

## Arguments

- `$fromParent` `Page|int` From parent Page or ID

## Return value

- `int` Number of rows inserted
