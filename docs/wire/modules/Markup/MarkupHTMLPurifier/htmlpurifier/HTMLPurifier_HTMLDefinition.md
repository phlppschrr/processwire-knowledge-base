# HTMLPurifier_HTMLDefinition

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition of the purified HTML that describes allowed children,
attributes, and many other things.

Conventions:

All member variables that are prefixed with info
(including the main $info array) are used by HTML Purifier internals
and should not be directly edited when customizing the HTMLDefinition.
They can usually be set via configuration directives or custom
modules.

On the other hand, member variables without the info prefix are used
internally by the HTMLDefinition and MUST NOT be used by other HTML
Purifier internals. Many of them, however, are public, and may be
edited by userspace code to tweak the behavior of HTMLDefinition.

@note This class is inspected by Printer_HTMLDefinition; please
      update that class if things here change.

@warning Directives that change this object's structure must be in
         the HTML or Attr namespace!

## addElement()

Adds a custom element to your HTML definition
@see HTMLPurifier_HTMLModule::addElement() for detailed
      parameter and return value descriptions.

## addBlankElement()

Adds a blank element to your HTML definition, for overriding
existing behavior
@param string $element_name
@return HTMLPurifier_ElementDef
@see HTMLPurifier_HTMLModule::addBlankElement() for detailed
      parameter and return value descriptions.

## getAnonymousModule()

Retrieves a reference to the anonymous module, so you can
bust out advanced features without having to make your own
module.
@return HTMLPurifier_HTMLModule

## __construct()

@type string
/
public $type = 'HTML';

/**
@type HTMLPurifier_HTMLModuleManager
/
public $manager;

/**
Performs low-cost, preliminary initialization.

## doSetup()

@param HTMLPurifier_Config $config

## processModules()

Extract out the information from the manager
@param HTMLPurifier_Config $config

## setupConfigStuff()

Sets up stuff based on config. We need a better way of doing this.
@param HTMLPurifier_Config $config

## parseTinyMCEAllowedList()

Parses a TinyMCE-flavored Allowed Elements and Attributes list into
separate lists for processing. Format is element[attr1|attr2],element2...
@warning Although it's largely drawn from TinyMCE's implementation,
     it is different, and you'll probably have to modify your lists
@param array $list String list to parse
@return array
@todo Give this its own class, probably static interface
