# HTMLPurifier_AttrDef_HTML_ID

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates the HTML attribute ID.
@warning Even though this is the id processor, it
         will ignore the directive Attr:IDBlacklist, since it will only
         go according to the ID accumulator. Since the accumulator is
         automatically generated, it will have already absorbed the
         blacklist. If you're hacking around, make sure you use load()!

## validate()

@param string $id
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
