# HTMLPurifier_HTMLModule_NonXMLCommonAttributes

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## setup()

@type string
/
public $name = 'NonXMLCommonAttributes';

/**
@type array
/
public $attr_collections = array(
'Lang' => array(
'lang' => 'LanguageCode',
)
);
}





/**
XHTML 1.1 Object Module, defines elements for generic object inclusion
@warning Users will commonly use <embed> to cater to legacy browsers: this
     module does not allow this sort of behavior
/
class HTMLPurifier_HTMLModule_Object extends HTMLPurifier_HTMLModule
{
/**
@type string
/
public $name = 'Object';

/**
@type bool
/
public $safe = false;

/**
@param HTMLPurifier_Config $config
