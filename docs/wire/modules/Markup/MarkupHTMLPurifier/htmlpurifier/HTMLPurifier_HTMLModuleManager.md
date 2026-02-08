# HTMLPurifier_HTMLModuleManager

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## registerModule()

@type HTMLPurifier_DoctypeRegistry
/
public $doctypes;

/**
Instance of current doctype.
@type string
/
public $doctype;

/**
@type HTMLPurifier_AttrTypes
/
public $attrTypes;

/**
Active instances of modules for the specified doctype are
indexed, by name, in this array.
@type HTMLPurifier_HTMLModule[]
/
public $modules = array();

/**
Array of recognized HTMLPurifier_HTMLModule instances,
indexed by module's class name. This array is usually lazy loaded, but a
user can overload a module by pre-emptively registering it.
@type HTMLPurifier_HTMLModule[]
/
public $registeredModules = array();

/**
List of extra modules that were added by the user
using addModule(). These get unconditionally merged into the current doctype, whatever
it may be.
@type HTMLPurifier_HTMLModule[]
/
public $userModules = array();

/**
Associative array of element name to list of modules that have
definitions for the element; this array is dynamically filled.
@type array
/
public $elementLookup = array();

/**
List of prefixes we should use for registering small names.
@type array
/
public $prefixes = array('HTMLPurifier_HTMLModule_');

/**
@type HTMLPurifier_ContentSets
/
public $contentSets;

/**
@type HTMLPurifier_AttrCollections
/
public $attrCollections;

/**
If set to true, unsafe elements and attributes will be allowed.
@type bool
/
public $trusted = false;

public function __construct()
{
// editable internal objects
$this->attrTypes = new HTMLPurifier_AttrTypes();
$this->doctypes  = new HTMLPurifier_DoctypeRegistry();

// setup basic modules
$common = array(
'CommonAttributes', 'Text', 'Hypertext', 'List',
'Presentation', 'Edit', 'Bdo', 'Tables', 'Image',
'StyleAttribute',
// Unsafe:
'Scripting', 'Object', 'Forms',
// Sorta legacy, but present in strict:
'Name',
);
$transitional = array('Legacy', 'Target', 'Iframe');
$xml = array('XMLCommonAttributes');
$non_xml = array('NonXMLCommonAttributes');

// setup basic doctypes
$this->doctypes->register(
'HTML 4.01 Transitional',
false,
array_merge($common, $transitional, $non_xml),
array('Tidy_Transitional', 'Tidy_Proprietary'),
array(),
'-//W3C//DTD HTML 4.01 Transitional//EN',
'http://www.w3.org/TR/html4/loose.dtd'
);

$this->doctypes->register(
'HTML 4.01 Strict',
false,
array_merge($common, $non_xml),
array('Tidy_Strict', 'Tidy_Proprietary', 'Tidy_Name'),
array(),
'-//W3C//DTD HTML 4.01//EN',
'http://www.w3.org/TR/html4/strict.dtd'
);

$this->doctypes->register(
'XHTML 1.0 Transitional',
true,
array_merge($common, $transitional, $xml, $non_xml),
array('Tidy_Transitional', 'Tidy_XHTML', 'Tidy_Proprietary', 'Tidy_Name'),
array(),
'-//W3C//DTD XHTML 1.0 Transitional//EN',
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'
);

$this->doctypes->register(
'XHTML 1.0 Strict',
true,
array_merge($common, $xml, $non_xml),
array('Tidy_Strict', 'Tidy_XHTML', 'Tidy_Strict', 'Tidy_Proprietary', 'Tidy_Name'),
array(),
'-//W3C//DTD XHTML 1.0 Strict//EN',
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'
);

$this->doctypes->register(
'XHTML 1.1',
true,
// Iframe is a real XHTML 1.1 module, despite being
// "transitional"!
array_merge($common, $xml, array('Ruby', 'Iframe')),
array('Tidy_Strict', 'Tidy_XHTML', 'Tidy_Proprietary', 'Tidy_Strict', 'Tidy_Name'), // Tidy_XHTML1_1
array(),
'-//W3C//DTD XHTML 1.1//EN',
'http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd'
);

}

/**
Registers a module to the recognized module list, useful for
overloading pre-existing modules.
@param $module Mixed: string module name, with or without
               HTMLPurifier_HTMLModule prefix, or instance of
               subclass of HTMLPurifier_HTMLModule.
@param $overload Boolean whether or not to overload previous modules.
                 If this is not set, and you do overload a module,
                 HTML Purifier will complain with a warning.
@note This function will not call autoload, you must instantiate
      (and thus invoke) autoload outside the method.
@note If a string is passed as a module name, different variants
      will be tested in this order:
         - Check for HTMLPurifier_HTMLModule_$name
         - Check all prefixes with $name in order they were added
         - Check for literal object name
         - Throw fatal error
      If your object name collides with an internal class, specify
      your module manually. All modules must have been included
      externally: registerModule will not perform inclusions for you!

## addModule()

Adds a module to the current doctype by first registering it,
and then tacking it on to the active doctype

## addPrefix()

Adds a class prefix that registerModule() will use to resolve a
string name to a concrete class

## setup()

Performs processing on modules, after being called you may
use getElement() and getElements()
@param HTMLPurifier_Config $config

## processModule()

Takes a module and adds it to the active module collection,
registering it if necessary.

## getElements()

Retrieves merged element definitions.
@return Array of HTMLPurifier_ElementDef

## getElement()

Retrieves a single merged element definition
@param string $name Name of element
@param bool $trusted Boolean trusted overriding parameter: set to true
                if you want the full version of an element
@return HTMLPurifier_ElementDef Merged HTMLPurifier_ElementDef
@note You may notice that modules are getting iterated over twice (once
      in getElements() and once here). This
      is because
