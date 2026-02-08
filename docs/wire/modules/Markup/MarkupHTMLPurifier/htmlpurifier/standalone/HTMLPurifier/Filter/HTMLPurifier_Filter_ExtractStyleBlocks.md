# HTMLPurifier_Filter_ExtractStyleBlocks

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/Filter/ExtractStyleBlocks.php`

This filter extracts <style> blocks from input HTML, cleans them up
using CSSTidy, and then places them in $purifier->context->get('StyleBlocks')
so they can be used elsewhere in the document.

@note
     See tests/HTMLPurifier/Filter/ExtractStyleBlocksTest.php for
     sample usage.

@note
     This filter can also be used on stylesheets not included in the
     document--something purists would probably prefer. Just directly
     call HTMLPurifier_Filter_ExtractStyleBlocks->cleanCSS()

## preFilter()

Removes inline <style> tags from HTML, saves them for later use
@param string $html
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return string
@todo Extend to indicate non-text/css style blocks

## cleanCSS()

Takes CSS (the stuff found in <style>) and cleans it.
@warning Requires CSSTidy <http://csstidy.sourceforge.net/>
@param string $css CSS styling to clean
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@throws HTMLPurifier_Exception
@return string Cleaned CSS
