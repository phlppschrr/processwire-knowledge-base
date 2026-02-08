# HTMLPurifier_ChildDef

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Defines allowed child nodes and validates nodes against it.

## __construct()

Validates nodes according to definition and returns modification.

@param HTMLPurifier_Node[] $children Array of HTMLPurifier_Node
@param HTMLPurifier_Config $config HTMLPurifier_Config object
@param HTMLPurifier_Context $context HTMLPurifier_Context object
@return bool|array true to leave nodes as is, false to remove parent node, array of replacement children
/
abstract public function validateChildren($children, $config, $context);
}





/**
Configuration object that triggers customizable behavior.

@warning This class is strongly defined: that means that the class
         will fail if an undefined directive is retrieved or set.

@note Many classes that could (although many times don't) use the
      configuration object make it a mandatory parameter.  This is
      because a configuration object should always be forwarded,
      otherwise, you run the risk of missing a parameter and then
      being stumped when a configuration directive doesn't work.

@todo Reconsider some of the public member variables
/
class HTMLPurifier_Config
{

/**
HTML Purifier's version
@type string
/
public $version = '4.15.0';

/**
Whether or not to automatically finalize
the object if a read operation is done.
@type bool
/
public $autoFinalize = true;

// protected member variables

/**
Namespace indexed array of serials for specific namespaces.
@see getSerial() for more info.
@type string[]
/
protected $serials = array();

/**
Serial for entire configuration object.
@type string
/
protected $serial;

/**
Parser for variables.
@type HTMLPurifier_VarParser_Flexible
/
protected $parser = null;

/**
Reference HTMLPurifier_ConfigSchema for value checking.
@type HTMLPurifier_ConfigSchema
@note This is public for introspective purposes. Please don't
      abuse!
/
public $def;

/**
Indexed array of definitions.
@type HTMLPurifier_Definition[]
/
protected $definitions;

/**
Whether or not config is finalized.
@type bool
/
protected $finalized = false;

/**
Property list containing configuration directives.
@type array
/
protected $plist;

/**
Whether or not a set is taking place due to an alias lookup.
@type bool
/
private $aliasMode;

/**
Set to false if you do not want line and file numbers in errors.
(useful when unit testing).  This will also compress some errors
and exceptions.
@type bool
/
public $chatty = true;

/**
Current lock; only gets to this namespace are allowed.
@type string
/
private $lock;

/**
Constructor
@param HTMLPurifier_ConfigSchema $definition ConfigSchema that defines
what directives are allowed.
@param HTMLPurifier_PropertyList $parent
