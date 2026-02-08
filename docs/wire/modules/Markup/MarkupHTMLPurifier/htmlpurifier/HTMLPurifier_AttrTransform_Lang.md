# HTMLPurifier_AttrTransform_Lang

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Post-transform that copies lang's value to xml:lang (and vice-versa)
@note Theoretically speaking, this could be a pre-transform, but putting
      post is more efficient.
