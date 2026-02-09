# A preview of coming attractions to ProcessWire’s image fields

Source: https://processwire.com/blog/posts/a-preview-of-coming-attractions-to-processwires-image-tools/

## Sections


## A preview of coming attractions to ProcessWire’s image fields

18 December 2015 by Ryan Cramer [ 13 Comments](/blog/posts/a-preview-of-coming-attractions-to-processwires-image-tools/#comments)

This week we have a guest post from Tom Reno ([@renobird](https://twitter.com/renobird)) showing us some excellent redesign work he is doing for our images field in ProcessWire. We hope to bring this to you soon in ProcessWire 3 and perhaps on the 2.x dev branch as well! –Ryan

Hello all, Tom Reno (Renobird) here. We wanted to give a preview of some ideas I'm working on to enhance the images field in ProcessWire — specifically in grid view. We will start by looking at the benefits and drawbacks of the current image field admin interface, and then take a look at some screenshots showing upgrades to it.


### Quick overview of the display options for an image field


### List View

This view shows the image/thumbnail, as well as the description and tags fields. If you are using any modules that add fields or cropping options (such as [Image Extra](https://github.com/justonestep/processwire-imageextra) or [Croppable Image](/talk/topic/8709-croppableimage/)) it displays items added by those modules as well. List view is great, but it has some drawbacks when dealing with a large number of images. Let’s suppose you have a field with 10, 20, 30 images or more. Each image consumes the entire width of the field. If you have custom fields and/or buttons for each image; each entry consumes a lot of vertical space. This makes things like sorting and spotting duplicates a bit time consuming, and with a lot of images, downright tedious.


### Grid View

Grid view addresses some of the issues mentioned above by displaying 100px thumbnails of the images. It also supports drag/drop sorting, and provides access to the new image editor when you hover the thumbnail. The drawback to grid view is that you can’t edit any of the image data, mark an image for deletion, or access any options added by other modules without switching back to list view.


### OK Reno, show me some mockups!

Below are some preliminary mockups I’ve been working on for improving the grid view. These are all just static images without any working code.


### Larger thumbnail size

One of the first things is to increase the thumbnail size from 100px to 130px. That is really just an arbitrary increase. It could end up being a little more or less, but this size worked well for my mockups.

Grid view with larger thumbnails


### Hovering a thumbnail

When hovering the thumbnail, there are several key things that appear.

Thumbnail hover state


### Edit mode

When a thumbnail is clicked, an overlay appears with a preview of the full image, image details, and any fields or buttons associated with the image. Ideally the overlay will work more like a dropdown menu that overlays any images below. Optionally, it could work more like Google image search, where the editor appears in between the rows. Since these are all just mockups; the actual implementation is still open for discussion.

Image editor overlay


### Marking an image for deletion

As mentioned above, when hovering a thumbnail, the trash can icon appears in the top left. When checked the image will be marked for deletion. At that point, the border becomes another color (in this case dark red) and the trash can icon is becomes always visible.

Image marked for deletion

I hope you’ve enjoyed this preview. I want to take a moment to acknowledge the excellent ideas and mockups Peter Knight [posted](/talk/topic/9986-image-field-ui-and-general-tidy-up/). His mockups were a great reference point and inspiration for these changes to the grid view. I’m looking forward to exploring some of his ideas for overall improvements to working with images.
