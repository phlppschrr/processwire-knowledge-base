# ProcessWire CKEditor Inputfield module

Source: https://processwire.com/docs/fields/ckeditor/

## Summary

CKEditor is the rich text editor used by ProcessWire via the module InputfieldCKEditor. On a default installation of ProcessWire, there is typically a “body” field which uses CKEditor.

## Key Points

- CKEditor is the rich text editor used by ProcessWire via the module InputfieldCKEditor. On a default installation of ProcessWire, there is typically a “body” field which uses CKEditor.
- The InputfieldCKEditor module is paired with and relies upon the FieldtypeTextarea module to manage its content.
- This module is tested and confirmed compatible with both repeaters and multi-language support.

## Sections


### Changing a field to use CKEditor

This module is tested and confirmed compatible with both repeaters and multi-language support.


### Inline Mode vs. Regular Mode

When configuring your CKEditor fields, you may notice the option of either Regular Mode or Inline Mode.


### When you should use regular mode

If you only have one or two instances of CKEditor on a page, you may prefer to use Regular Mode because it has been around longer and tends to be more reliable. Regular Mode runs in a separate frame, making it more isolated and thus less prone to any other CSS or Javascript interference. Regular mode editors are also more obviously rich text editors, as their interface and buttons are always visible. We recommend using Regular Mode in these instances:


## Advanced Tips

This section contains contextual instructions that are linked to from within the module. These cover specific needs during field configuration and you do not need to read this section in order to use CKEditor.


### Custom Editor JS Styles Set

This is an option that appears in your CKEditor field settings when editing a textarea field in the ProcessWire field editor. Use this option if you want to have a Styles dropdown that contains your own custom styles that users can choose from your editor.


### Instructions

Edit your CKEditor field in Setup > Fields, and click to the Input tab.


### Custom Editor CSS File

This option enables you to modify the way that text and other elements appear in your editor. This covers how they look in the administrative environment only, and has nothing to do with the front-end of your site. Typically you would use this option if you wanted to modify the default look-and-feel in the editor to something that is more stylistically similar to the front-end of your site.


### Important Note About Inline Mode (contents-inline.css)

If using more than one CKEditor inline mode editor on your page, and not using the same contents-inline.css file on all of them, then you will end up having them compete with each other or fall back to the default contents-inline.css. In order to avoid this, you would need to make your CSS selectors more specific to the field they apply to.
