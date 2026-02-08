# HTMLPurifier_TagTransform_Font

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Transforms FONT tags to the proper form (SPAN with CSS styling)

This transformation takes the three proprietary attributes of FONT and
transforms them into their corresponding CSS attributes.  These are color,
face, and size.

@note Size is an interesting case because it doesn't map cleanly to CSS.
      Thanks to
      http://style.cleverchimp.com/font_size_intervals/altintervals.html
      for reasonable mappings.
@warning This doesn't work completely correctly; specifically, this
         TagTransform operates before well-formedness is enforced, so
         the "active formatting elements" algorithm doesn't get applied.
