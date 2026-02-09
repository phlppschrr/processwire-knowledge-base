# ProcessWire 3.0.17 brings major upgrade to images field

Source: https://processwire.com/blog/posts/major-images-field-upgrade/

## Sections


## ProcessWire 3.0.17 brings major upgrade to images field

6 May 2016 by Ryan Cramer [ 11 Comments](/blog/posts/major-images-field-upgrade/#comments)


## ProcessWire 3.0.17

A few months back Tom Reno wrote a blog post here about a [redesign of our images field](/blog/posts/a-preview-of-coming-attractions-to-processwires-image-tools/) (in the admin). Today, I'm glad to report that this new images field is now available in ProcessWire 3.0.17. And it's got a few new tricks you haven't heard about yet too. We've got all the details here in this post. There's also a screencast at the end that shows you the new images field in action.


### Credits

The new images field was designed by Tom Reno ([Renobird](/talk/user/474-renobird/)) and the end result looks almost exactly like the original design mockups. Most of the implementation was done by Benjamin Milde ([LostKobrakai](/talk/user/874-lostkobrakai/)). A huge thanks to both Tom and Benjamin for a job well done. This is a really great upgrade to our images field.


### Overview

The most obvious improvement is that the new images field is nicer to look at, nicer to use, and uses available space a lot better. Renobird's design here really gives it a nice feel.

In terms of use, image editing functions are somewhat influenced by Google Images. Clicking an image loads an edit panel below it, within the grid of images. In the edit panel, you can see a larger preview of the image. Click the preview to view it in a lightbox, click buttons to crop the image, view/manage variations, or enter description text and/or tags.

Images can be sorted by drag and drop, just like in the previous iteration. But the sorting is a lot nicer to work with here, you'll see what I mean. If you hover an image for a second, you'll get a helpful tooltip with additional details about the image.

To mark an image for deletion, you just hover it and click the trash icon. To mark all images for deletion, double click any trash icon.


### Uploading

The new images field can also do a few cool things with regard to uploading that the previous images field couldn't.


### Immediate previews

When you start uploading images, you'll see a preview of them immediately in the grid, before they've really even started uploading them. LostKobrakai worked a little magic here. The progress bar will appear on top of that thumbnail preview as the image uploads.


### Drag-and-drop in place

Not only can you drag and drop image(s) directly into the images field, but you can drag and drop them exactly where you want them to go in the grid of images. Previously, any images you added just went to the end of the list. Now you can drag them to the beginning, the end, or anywhere in between. Note that this "drag in place" function is disabled when an image "edit" panel is open, you'll see why below. As a result, you'll want to close the image edit panel when you want to drag images directly into the grid of images.


### Replace an image by dropping a new one on top of it

When the "edit" panel is open, you have a larger preview of the image. You can replace that image simply by dragging a new image from your computer right on top of that preview image. It doesn't get any simpler than that!


### Thumbnails

Admin thumbnails in the previous images field were 100 pixels in the smaller dimension. In the new images field, they are now 260 pixels in the smaller dimension, scaled to 130 pixels (for HiDPI/retina support). The actual size and HiDPI support can be adjusted in config.php settings in `$config->adminThumbOptions`, though we think most will likely want to keep the default settings.

We've established that the new images field uses larger and nicer looking thumbnails, but went back and forth a bit over the best way to handle existing sites that already had potentially thousands of image thumbnails already created and in use. We certainly didn't want to re-create them all, making everyone wait several seconds to edit a page that has many images. Given that, here's what it does:


### Easter egg

Don't mind waiting for it to re-create your legacy thumbnails at the new size? There's a little secret for that. Click the label in the bottom right corner of the images field that says *“drag and drop in new images above.”* When you click it, it changes to *“legacy thumbnails will be re-created on save.”* Click the save button, and it'll re-create the thumbnail images on that page. Now most probably don't need this, but wanted to let you know it's there just in case you wanted it.


### Screencast

Here's a quick screencast that demonstates some of the things mentioned above.


### ProcessWire 3.x API reference continues to grow

While we're on the subject to images (and files), our [3.x API reference](../api-full/index.md) continues to grow! These new classes have been documented in detail and added to our 3.x API reference this week:

- [Pagefile](../api-full/wire/core/Pagefile/index.md)
- [Pagefiles](../api-full/wire/core/Pagefiles/index.md)
- [Pageimage](../api-full/wire/core/Pageimage/index.md)
- [Pageimages](../api-full/wire/core/Pageimages/index.md)
- [PagefilesManager](../api-full/wire/core/PagefilesManager/index.md)


### Wrapping up

Note that other modules that extend the old images field (like those that provide additional crop functions) may not work with the new one. If that turns out to be the case, we'll likely move the old images field to a 3rd party module so that it can continue to be used for these cases.

A big thanks again to LostKobrakai and Renobird for their great work with ProcessWire's new images field. Please let us know if you run into any issues with it. Have a great weekend and remember to read the [ProcessWire Weekly](http://weekly.pw)!
