# HTMLPurifier_HTMLModule_Tidy

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Abstract class for a set of proprietary modules that clean up (tidy)
poorly written HTML.
@todo Figure out how to protect some of these methods/properties

## getFixesForLevel()

Retrieves all fixes per a level, returning fixes for that specific
level as well as all levels below it.
@param string $level level identifier, see $levels for valid values
@return array Lookup up table of fixes

## makeFixesForLevel()

Dynamically populates the $fixesForLevel member variable using
the fixes array. It may be custom overloaded, used in conjunction
with $defaultLevel, or not used at all.
@param array $fixes

## populate()

Populates the module with transforms and other special-case code
based on a list of fixes passed to it
@param array $fixes Lookup table of fixes to activate

## getFixType()

Parses a fix name and determines what kind of fix it is, as well
as other information defined by the fix
@param $name String name of fix
@return array(string $fix_type, array $fix_parameters)
@note $fix_parameters is type dependant, see populate() for usage
      of these parameters

## makeFixes()

Defines all fixes the module will perform in a compact
associative array of fix name to fix implementation.
@return array
