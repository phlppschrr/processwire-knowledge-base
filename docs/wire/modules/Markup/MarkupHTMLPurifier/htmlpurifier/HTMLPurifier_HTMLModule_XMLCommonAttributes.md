# HTMLPurifier_HTMLModule_XMLCommonAttributes

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## makeFixes()

@type string
/
public $name = 'XMLCommonAttributes';

/**
@type array
/
public $attr_collections = array(
'Lang' => array(
'xml:lang' => 'LanguageCode',
)
);
}





/**
Name is deprecated, but allowed in strict doctypes, so onl
/
class HTMLPurifier_HTMLModule_Tidy_Name extends HTMLPurifier_HTMLModule_Tidy
{
/**
@type string
/
public $name = 'Tidy_Name';

/**
@type string
/
public $defaultLevel = 'heavy';

/**
@return array
