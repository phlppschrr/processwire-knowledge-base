# HTMLPurifier_HTMLModule_CommonAttributes

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## setup()

@type string
/
public $name = 'CommonAttributes';

/**
@type array
/
public $attr_collections = array(
'Core' => array(
0 => array('Style'),
// 'xml:space' => false,
'class' => 'Class',
'id' => 'ID',
'title' => 'CDATA',
'contenteditable' => 'ContentEditable',
),
'Lang' => array(),
'I18N' => array(
0 => array('Lang'), // proprietary, for xml:lang/lang
),
'Common' => array(
0 => array('Core', 'I18N')
)
);
}





/**
XHTML 1.1 Edit Module, defines editing-related elements. Text Extension
Module.
/
class HTMLPurifier_HTMLModule_Edit extends HTMLPurifier_HTMLModule
{

/**
@type string
/
public $name = 'Edit';

/**
@param HTMLPurifier_Config $config
