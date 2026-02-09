# ProcessWire 3.0.10 expands image resize options

Source: https://processwire.com/blog/posts/processwire-3.0.10-expands-image-resize-options/

## Sections


## ProcessWire 3.0.10 expands image resize options

4 March 2016 by Ryan Cramer [ 8 Comments](/blog/posts/processwire-3.0.10-expands-image-resize-options/#comments)


## ProcessWire 3.0.10

Most of this week and ProcessWire 3.0.10 has been focused on covering issue reports and related tweaks/fixes, which you'll see in the [commit log](https://github.com/ryancramerdesign/ProcessWire/commits/devns). But we've also got a major upgrade to the core in 3.0.10 as well, with the introduction of ImageMagick and a new module type: *ImageSizerEngine*.


### Image Sizer Upgrades

We've got some really nice upgrades to our image resizing engine, thanks to our resident image and photography expert, [Horst](/talk/user/1041-horst/).

ProcessWire's image manipulations have always been handled by the PHP GD library, which does quite a nice job in terms of quality and file size. However, areas where it lacks are in speed and ability to resize really large images.

Sometimes GD simply can't handle really large photos straight off of high-megapixel digital cameras, because manipulating them takes more memory than is available to PHP. And even when it can handle them, you might be waiting a bit for it to generate thumbnails, or perform resizes for large groups of images.

We've been on the lookout for ways to improve the areas mentioned above and Horst found a way to make it happen. He has developed a new image resizing engine for ProcessWire that uses [ImageMagick](https://en.wikipedia.org/wiki/ImageMagick) (PHP's IMagick) library. Relative to GD, ImageMagick has a couple of nice benefits in ProcessWire:


### How to use ImageMagick in the core

ProcessWire 3.0.10 now comes with a new module called *ImageSizerEngineIMagick*. To install, go to Modules > Core > Image and click *Install*.

There's one potential problem though: not all PHP installations have the [ImageMagick library](http://php.net/manual/en/book.imagick.php) available. If the library is not available, installation will fail with an error message indicating that. It may be fairly simple to enable ImageMagick on a PHP installation that doesn't have it, but needs to be installed by someone that has control over the PHP configuration.

Once the *ImageSizerEngineIMagick* module is installed, all image resizes that *can* use ImageMagick *will* use them. You'll notice quicker resizes as soon as you upload new images. You don't have to do anything other than install the module. If there is a situation where ImageMagick can't perform the resize, control will be passed back to the existing GD resizer.

**ImageMagick quality settings aren't exactly the same as quality settings in GD.** I've found that I can use a lower quality setting in IMagick and get the same result as in GD. For instance, my subjective opinion is that a quality setting of 85 in IMagick is equivalent to a quality setting of 90 in GD, and produces similar file sizes. ImageMagick just does it a lot faster.


### New ImageSizerEngine modules

Horst and I collaborated on making *ImageSizerEngine,* a new module type in the ProcessWire core (of which the IMagick one is the first example). This enables one to install new modules to handle image manipulations, much in the same way one can currently install *WireMail* modules to handle email delivery.

You can install multiple *ImageSizerEngine* modules and indicate the order in which they should be tried. If one *ImageSizerEngine* module can't perform a resize of a particular image, it passes it on to the next one in priority order. The last fallback is the existing GD engine, which is available in pretty much all PHP installations, making it the ideal fallback.

The IMagick module mentioned above is the first ImageSizerEngine module available, and it's such an improvement that we thought it belonged in the core. However, there are more *ImageSizerEngine* modules in the works. Horst is currently working on modules that support the CLI versions of ImageMagick and [NetPBM](https://en.wikipedia.org/wiki/Netpbm). I imagine the future will also bring more options, including modules that can compress the hell out of images without visual quality loss, and engines that use external services… the possibilities are numerous.


### GD vs ImageMagick examples

I took a couple of screenshots demonstrating resizes on the same source image between GD and ImageMagick in a ProcessWire installation. The source image is 3 megapixels at 600 kb, resized down to a width of 250 pixels wide. Below are the results with sharpening set to "none".

Something to keep in mind with the examples below is that the source image was a jpeg, resized to 250px jpegs, then sent to a jpeg screenshot (the source PNGs was just far too large to embed in this post). Meaning, if you go pixel-peeping, keep in mind what you are seeing has been through 3 rounds of jpeg compression. The numbers on the left are the quality setting, with 90 being ProcessWire's default.

As you can see IMagick is churning out the resizes a whole lot faster than GD, though with a little bit bigger file size. Both GD and IMagick do quite a nice job in terms of image quality. If you reduce the quality setting by 5 for IMagick (i.e. 85 rather than 90) the file sizes should be similar with little or no difference in quality.

When I go pixel peeping on these images (prior to taking the JPG screenshots), my subjective opinion is that IMagick is doing a better job of retaining the details, but GD is doing a little better job of hiding the jpeg compression, especially around the borders of the flower in the center. It seems that maybe IMagick has a little bit of built-in sharpening, even if set to none.

Speaking of sharpening, here's what the same example looks like with sharpening set to "soft" (ProcessWire's default). Though my comments would be mostly identical to the version with no sharpening. IMagick's sharpening does seem slightly more aggressive than GD's, and that carries through to the medium and strong sharpening settings as well.

Again, keep in mind the above is a jpeg screenshot of resized jpegs from a source jpeg, so not an ideal comparison, but hopefully interesting nonetheless.

A lot of ProcessWire sites really push the boundaries on use of images/photos, and these core upgrades are going to be a major benefit to such sites. The performance of ImageMagick and its ability to handle images of any size makes a big difference! If your system supports PHP's ImageMagick library, I highly recommend installing the core *ImageSizerEngineIMagick* module in PW 3.0.10+. Thanks again to Horst for all of his work in making this happen. Hope to see you all at the [ProcessWire Weekly](http://weekly.pw) this weekend!
