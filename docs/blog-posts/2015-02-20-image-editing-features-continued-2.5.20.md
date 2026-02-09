# Image editing features (continued, 2.5.20)

Source: https://processwire.com/blog/posts/image-editing-features-continued-2.5.20/

## Sections


## Image editing features (continued, 2.5.20)

20 February 2015 by Ryan Cramer [ 0 Comments](/blog/posts/image-editing-features-continued-2.5.20/#comments)

Last week we introduced the new image editing features available from the rich text editor, and told you a little about the editing features yet to come for image fields. This week those features are now ready to use directly from image fields.


### More image editing features

Every image in an image field now has an edit link (represented by an edit/crop icon) that appears when hovering the image. It can also be accessed by clicking on the image filename (useful for touch devices).

When you click the edit link/icon, it opens a modal window showing you the image, along with a few editing controls.

From here you can resize or crop the image as you see fit.*

Once you've adjusted the image to your needs, you have a choice of replacing the original image, or saving to a new copy. Regardless of which option you choose, your image will be processed and immediately updated in your image field underneath. If not in view, it will scroll to it automatically so you can see your work right away.

When using the "Save & Replace" option after cropping an image, this tool will also attempt to re-create size variations that were created from the previous image. This ensures that your thumbnail image, as well as any other sizes you may have generated are updated according to your new crop.

*We will likely be adding a few more editing controls in the future: rotate/flip, quality and sharpening.


### Primary use cases

In ProcessWire, image size variations are typically API-generated for specific dimensions. The image editing tools we've built here are primarily intended to compliment what's already working with images on the API side. It does that by giving the person managing images in the admin more control over where their images will be cropped, and the ability to fix cropping problems without having to upload a new photo.

A common example is when the site editor uploads a tall portrait oriented photo and the API-side is generating a square or landscape oriented photo variation. The result is a photo that technically fits the needed landscape orientation and dimensions, but with potentially important elements cropped out (like people's heads!). With these new image editing features (particularly the cropping feature) the site editor now has a means of correcting such problems on their own by cropping their uploaded photo in a manner that won't cause decapitations on the auto generated variations.

In use cases like this, things like predefined pixel dimensions or aspect ratios don't matter so much, because it's still the API side that's generating the final image sizes. However, there are also cases where you may literally want the site editor defining the exact crop and at the exact pixel dimensions that will be used in the final output of the site. For those cases, you would want predefined crop sizes that the editor can select from, and there is already a module that does a great job of this called [Croppable Image](https://processwire.com/talk/topic/8709-croppableimage/) (and the predecessor Thumbnails/CropImage), so be sure to check it out if you have this particular need.


### Other updates

ProcessWire's modal windows are now consistently generated from the same place, and the settings are configurable in your site configuration. See the [$config->modals](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/config.php#L736) option. Furthermore, the modals now auto-adjust to become larger on smaller screens. At mobile sizes, the modals become full-screen.

We've started work this week on improving some of the touch navigation aspects in the PW admin, and those updates will be continuing in the coming weeks. This week jQuery UI touch support has been added via a library, and this should make a lot of things accessible on touch devices that previously weren't.

There were also significant improvements to the image variations editor that was introduced last week.
