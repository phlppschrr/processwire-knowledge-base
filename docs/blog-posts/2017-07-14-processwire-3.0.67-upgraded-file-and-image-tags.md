# ProcessWire 3.0.67 – Upgraded file and image tags

Source: https://processwire.com/blog/posts/processwire-3.0.67-upgraded-file-and-image-tags/

## Sections


## ProcessWire 3.0.67 – Upgraded file and image tags

14 July 2017 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-3.0.67-upgraded-file-and-image-tags/#comments)


## ProcessWire 3.0.67

This week's version includes some helpful UI updates to the tags feature available in our File and Image fields, which we'll be taking a closer look at in this post. Like many versions, this also includes some other updates consistent with submitted GitHub issue reports.


### Upgraded file and image tags

You may already be familiar with this feature, but this week we improved it a lot. With File and Image fields, you've always been able to optionally enable a useful tags feature. This enables you to categorize files or images with tags that can be used to provide more information about the file or image/photo.

As an example, on many sites that I build, every page has an "images" field that can be used for photos placed in CKEditor. But if the client uploads an image and gives it the tag "primary", then my template file knows to display that image at a reserved placement at the top of the page. Likewise, if they give it a tag of "sidebar" then the template file knows to display the image at a reserved place in the sidebar. This simple example just hints towards the usefulness of tagged files/images, but there is so much more you could accomplish. Another example is one we mentioned in a post a couple of weeks ago, where we outlined how to use tags to support a [multi-language file or image field](/blog/posts/processwire-updates-and-new-field-types/) in ProcessWire.


### Upgrading the tags UI

As useful as the file/image tags feature is, the UI for assigning tags has not been as useful. For starters, its appearance was that of just a regular text field… nothing about it really implied tags, so you kind of had to know what you were doing. It's one of the few places in PW where you would have to instruct the client how to use it. Further, it was completely freeform… you would just type tags, and there was no way to choose pre-assigned tags like "primary" or "sidebar", etc. Basically, you had to remember on your own if there were any tags that might be recognized for site layout and such.

This week we've attempted to resolve those issues and make the tags feature both more friendly and useful. The first order of business was to make it actually look like you were working with tags. To do this, we added a slightly modified version of the excellent [Selectize](http://selectize.github.io/selectize.js/) library as an extension to our jQuery UI module. Now you can…

- Type a tag, then hit space or enter, and it gets converted to a tag.
- Select from a list of pre-defined tags.
- Drag and drop tags to the order you prefer.
- Remove a tag without having to backspace over it (though you can also do backspace).
- Have support for freeform tags, predefined tags, or both.

Here's what it looks like before you've entered/selected any tags:

Below is what it looks like when you focus the tags field, giving you a list of predefined tags that you can select from. Or you can enter your own:

This screenshot below demonstrates the tags configuration that you'll see on the Details tab when editing a file or image field:

As someone that has used the file/image tags feature quite a lot in the past, I personally find the ability to use pre-defined tags among the most useful additions here. It means I no longer have to communicate by other means what tags are recognized by the site templates. While I know not everyone uses tags, I hope that at least some of you find the additions this week useful in your projects as well.


### See also:

- [Pagefiles::getTag()](../api-full/wire/core/Pagefiles/method-gettag.md)
- [Pagefiles::findTag()](../api-full/wire/core/Pagefiles/method-findtag.md)
- [Pagefile::tags()](../api-full/wire/core/Pagefile/method-tags.md)
- [Multi-language tags for file/image fields](/blog/posts/processwire-updates-and-new-field-types/)

If you haven't submitted your latest PW sites to our [sites directory](/about/sites/) in awhile, please stop by and [add them](/about/sites/submit/) when you get a chance–we love seeing your work. We'll be back again next week with another new dev version of ProcessWire. Have a great weekend and enjoy the [ProcessWire Weekly](http://weekly.pw).
