# New image editing features (2.5.19)

Source: https://processwire.com/blog/posts/new-image-editing-features-2.5.19/

## Sections


## New image editing features (2.5.19)

13 February 2015 by Ryan Cramer [ 7 Comments](/blog/posts/new-image-editing-features-2.5.19/#comments)


## Photos, Images, HiDPI and more

If you follow the core updates regularly, you'll see that the focus areas jump around from week to week. It might seem a bit random, but actually it's based largely on what comes up as needs or enhancements with projects powered by ProcessWire that I work on with clients. One area that's been coming up with increasing frequency is the need for better image editing tools, particularly when it comes to images inserted into rich text fields. So this week we've got a major update to the tools available for editing images in these scenarios.


### Highlights of new image editing features

- New built-in image cropping feature (in addition to existing resize features), with ability to re-crop from original source image.
- HiDPI/Retina image support for images inserted into rich text fields (via resolution doubling and increased compression).
- New maximize (all pixels) and minimize (fit-to-window) image tools.
- Simpler image alignment tools with live preview and greeking for context (align left, align right, align center).
- New tool for viewing all variations of an image with ability to delete any or all of them.


### Video/screencast


### Manipulate images directly in your images field

At the end of the video above, you might also notice I clicked on an image filename in the page editor and it opened an image editor, similar to the one we arrived at from the CKEditor field. This part is a work in progress. It works, but not yet fully as intended. By next week it should be fully functional. For now, if you are running the dev branch you might ignore that feature as I've got a little more work to do on it (and that's why it's somewhat hidden at the moment).

Once complete, this feature will enable you to edit files in any image field directly to resize or crop them as you see fit, and then either replace the original or create a new copy to add to your image field.


### More about the HiDPI/Retina option

More and more visitors to our sites are using HiDPI screens. Most smartphones now use HiDPI screens, as do many tablets and notebook computers. Within the last year, HiDPI desktops have become more common (like the iMac 5k), and even Costco is now selling a nice 27-inch HiDPI desktop screen from Samsung, for about the same price that a 27" regular screen was a couple of years ago. That is to say, they are now commonplace and if you aren't already using one, you will be. As you may know, on these screens, regular 72 dpi images pretty much look fuzzy and terrible. But photos and text at HiDPI look absolutely amazing.

One of the most common ways to deliver HiDPI/Retina images is to use an image that's double the size you want to display it at, and then use width/height tags or styles to scale it to 50% original size. You might think that that seems like a horrible waste of bandwidth, but actually you can get away with a lot higher compression when scaling an image to 50%. While you might have kept your original image at 90% quality, you could get away with anywhere from 20-60% quality on the 50% scaled image without any visible quality loss. Because of the increased compression, chances are you've also got a file size that is not that much larger than the non-HiDPI version would have been.

Since ProcessWire doesn't get involved in the front-end output of your site, it likewise doesn't get involved in how you scale images (or don't) for HiDPI screens. But when it comes to the rich text editor (CKEditor) that's an exception, because the images you insert here are inserted by markup that is ultimately output on the front-end of your site.

When you check that "HiDPI/Retina" checkbox in the image editor before inserting an image in your RTE content, what it's actually doing is sizing everything to double the resolution you specified, and then adding a width tag (but not height tag) to the markup, at your specified size. The reason it doesn't add a height tag is because this makes your life a whole lot easier when it comes to handling these images in responsive layouts. Essentially it helps you avoid non-proportional scaling as a result of max-width/min-width styles that are common with responsive images.

I would be really interested in hearing how this works out for those of you using HiDPI/Retina images in responsive layouts. I've had good results here, but of course there are a lot of approaches both to HiDPI images and responsive images out there, so want to make sure we're open-ended enough to accommodate a diversity of environments.


### Screenshots


### Acknowledgements

I want to mention the work that Horst (co-author of Croppable Image) did that made a lot of these new features possible. A few months ago, he added new cropping features to ProcessWire's ImageSizer class (called cropExtra), as well came up with the idea for suffix support for images. The new features added this week make use of a lot of the things Horst contributed to ProcessWire 2.5.

The new cropping features also use a great jQuery plugin by [Fengyuan Chen](https://github.com/fengyuanchen/) called [Cropper](http://fengyuanchen.github.io/cropper/). Thanks to him for his work in creating this.


### More image editing tools for ProcessWire

If you find these new image editing features interesting, be sure to check out some of the other image editing tools available for ProcessWire. These have little crossover with the new image editing features presented here, and may be the perfect fit depending on your situation:

- [Croppable Image](/talk/topic/8709-croppableimage/)
- [Image Focus Area](/talk/topic/8079-imagefocusarea/)
- [Image Extra](http://modules.processwire.com/modules/image-extra/) (just added to modules directory today)
- [More Image/Photo modules for ProcessWire](http://modules.processwire.com/categories/photo-video/)
