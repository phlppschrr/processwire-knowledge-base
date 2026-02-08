# HTMLPurifier_Printer_HTMLDefinition

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/Printer/HTMLDefinition.php`


## render()

@type HTMLPurifier_HTMLDefinition, for easy access
/
protected $def;

/**
@param HTMLPurifier_Config $config
@return string

## renderDoctype()

Renders the Doctype table
@return string

## renderEnvironment()

Renders environment table, which is miscellaneous info
@return string

## renderContentSets()

Renders the Content Sets table
@return string

## renderInfo()

Renders the Elements ($info) table
@return string

## renderChildren()

Renders a row describing the allowed children of an element
@param HTMLPurifier_ChildDef $def HTMLPurifier_ChildDef of pertinent element
@return string

## listifyTagLookup()

Listifies a tag lookup table.
@param array $array Tag lookup array in form of array('tagname' => true)
@return string

## listifyObjectList()

Listifies a list of objects by retrieving class names and internal state
@param array $array List of objects
@return string
@todo Also add information about internal state

## listifyAttr()

Listifies a hash of attributes to AttrDef classes
@param array $array Array hash in form of array('attrname' => HTMLPurifier_AttrDef)
@return string

## heavyHeader()

Creates a heavy header row
@param string $text
@param int $num
@return string
