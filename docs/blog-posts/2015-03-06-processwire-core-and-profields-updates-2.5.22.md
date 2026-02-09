# ProcessWire core and ProFields updates (2.5.22)

Source: https://processwire.com/blog/posts/processwire-core-and-profields-updates-2.5.22/

## Sections


## ProcessWire core and ProFields updates (2.5.22)

6 March 2015 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-core-and-profields-updates-2.5.22/#comments)


### Upload support now provided in image selection window

In our ongoing effort to provide you the best editing tools available, we've continued this week with some additional tweaks to the rich text editor. Specifically, we added caption support to CKEditor rich text fields (via HTML5 figure/figcaption), and we've added image upload capability to the image selection modal window.

Before this week, when you went to insert an image in your text (via the rich text editor), you were given an option to select images, but not an option to upload images. Actually, the option to upload to any image field(s) has always been in your page editor (assuming it had an image field), rather than in that modal dialog window. But this has been a recurring point of confusion for users new to ProcessWire. People have come to expect the ability to upload images anywhere that they have the ability to select them. So this week we added that capability.

Now when you click the image icon in CKEditor, your dialog window has an "upload" button in the lower toolbar. The only requirement is that the page being edited has at least one image field on it. If you have multiple image fields, you will get a choice of which image field you want to upload to. The upload works in the same way that it does in your page editor: drag and drop one or more images and they upload automatically.

You might wonder why we didn't have this before? It's actually a lot trickier to implement in ProcessWire than you might think. Because all images are attached to pages (that have image fields), all images are represented by fields in a page, like any other field. That means that if you are uploading images to a modal dialog window sitting on top of your page editor, you've got two copies of the same field open (one in the modal dialog window, and the other in the page editor beneath it). The challenge was always "how do we prevent changes in one from wiping out changes in the other." The solution was Javascript of course. When you upload an image in the modal dialog window and save it, it goes in behind-the-scenes and updates the one in the editor window underneath too.


### Image caption support in the rich text editor

Any time you insert an image into your copy, you now have a "caption" checkbox that you can check. When checked, it inserts an HTML5 `figure` + `figcaption` + `img` rather than just an `img`. The image with caption can be left, right, or center aligned just like images can. After insertion of the image, the caption text becomes editable in your editor. Because we've left the editing of caption text to the RTE, your caption text can contain additional markup elements (like links for example) as needed.

*A note about using this in CKE inline mode:* I've found what appears to be a bug in CKEditor's selection object when in inline mode (only). If you go back and modify an existing image with caption (by opening the image modal dialog) any changes to the alignment (left, right, center) won't be reflected after insertion of the image. A fairly minor thing, and not an issue when inserting an image/caption the first time, but I wanted to mention it. I'm on the hunt for a solution, but this one might be in CKEditor itself.

*A note about CKEditor and browser cache:* When it comes to these upgrades that involve modifications to our own CKEditor plugins, it can be really difficult to get your browser to recognize the new version. If you don't see the new caption support working at first, you may need to quit and restart your browser or clear the cache.


### Major upgrade to ProFields Textareas fieldtype

The [Textareas ProField](/talk/store/product/10-profields/) now supports most Input (Inputfield) types, whether core or 3rd party in the latest beta released to ProFields subscribers this week. You can now have any number of any of the below input types, each with their own name/label/description, and each accessible from the API as the proper type, all within a single Textareas field. I should probably change the name of this Fieldtype, as the name Textareas doesn't make much sense for it anymore! In addition to the previously supported Text, Textarea and CKEditor fields, I have successfully tested it with the following core inputs, which were not previously supported:

- Date fields
- Single checkbox fields
- Page fields (with select, AsmSelect, Checkboxes, Select Multiple, Radios, and Autocomplete)
- Single selection fields: Select and Radios (outside of Page fields, like in FormBuilder)
- Multi-selection fields: Checkboxes, AsmSelect, Select Multiple (outside of Page fields, like in FormBuilder)
- Integer and Float fields

Support is not limited to those mentioned above, and it may well support many 3rd party Inputfield types as well. In addition, multi-language is supported for all inputs.


### Markdown Textformatter module now with Parsedown support

If you are familiar with Markdown, you may have heard of [Parsedown](http://parsedown.org), which is perhaps the best Markdown library out there right now (as far as I know). In addition to being very fast, one of the nice things about it is that it supports [GitHub flavored markdown](https://help.github.com/articles/github-flavored-markdown/). This week we updated our TextformatterMarkdownExtra module to support the Parsedown library. Because I'm not entirely sure if there might be some minor differences in rendering between the existing library and Parsedown, I've also left the existing library in place (as the default). To switch to Parsedown, go to your Modules > Core > Textformatter > Markdown Extra module settings. You'll see an option in there to switch it to use the Parsedown library.


### has_parent selectors now support multi-value

This is a rather minor thing, but may be big to a few people that have needed it in the past. ProcessWire supports a property in selectors called "has_parent". This lets you specify an ID or path of any page in your site, and it then limits the `$pages->find()` to only pages in the family tree beneath the page you have specified. Most properties in selectors support multiple values, where you can specify multiple OR values by separating them with a pipe "|", like this: `a|b|c`. The has_parent property was one of the few that did not support multiple values. As of this week, it now does. Now you can do things like like:

```php
$products = $pages->find("has_parent=/products|/future-products, ...");
```
