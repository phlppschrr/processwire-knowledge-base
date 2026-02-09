# ProcessWire 3.0.132 adds WEBP image support

Source: https://processwire.com/blog/posts/webp-images-in-pw/

## Sections


## ProcessWire 3.0.132 adds WEBP image support

24 May 2019 by Ryan Cramer [ 6 Comments](/blog/posts/webp-images-in-pw/#comments)

This week I’m happy to report we now have WEBP support in ProcessWire thanks to a GitHub pull request from Horst Nogajski. This enables you to have highly optimized image output in PW and I think you’ll really like the difference it makes. Read on for all the details…

I’ve added that [PR](https://github.com/processwire/processwire/pull/141) to the core this week, and extended it a bit, and it’s now ready for testing on the dev branch. If you aren’t familiar with WEBP, it’s an image format the can make files a whole lot smaller than JPG or PNG, but with no visible loss in quality ([learn more](https://developers.google.com/speed/webp/)). It’s developed by Google and now widely supported by browsers, though it is also a good idea (and typically necessary) to provide a fallback JPEG or PNG when using WEBP.

For cases where WEBP is supported, the difference is rather amazing in many cases. Google claims WEBP is 26% to 34% smaller than equivalent PNG/JPG, but my experience has been: that’s if you are dealing with an already well compressed PNG/JPG. In reality, I’m seeing a bigger difference than that in many or most cases.

For a few examples, take a look in our sites directory. I’ve only implemented WEBP on the individual site landing pages so far, but I’ve added stats about how much space was saved by using the WEBP image relative to the PNG/JPG image (see under lower right corner of images). Here’s an example [showing a savings of 89%](https://processwire.com/sites/list/australian-antarctic-jobs/), though please click around the sites directory to see many more examples. Soon, I will be updating the entire site to use WEBP, but since it was just added to the core in the last 24 hours, so far I've only had time to update that one template file.


### WEBP engine support

ProcessWire supports WEBP with both its GD engine as well as its ImageMagick engine. But that assumes that PHP itself supports WEBP in one of those libraries. I found that on my local dev environment (MAMP) it wasn’t supported in either GD or ImageMagick, though something similar to [Noburu’s instructions](https://processwire.com/talk/topic/14236-webp-support/?do=findComment&comment=185046) worked for me, and I was able to get it working with ImageMagick.

On the other hand, I found that our AWS web server already had WEBP support enabled with PHP’s GD library, so I didn’t have to do anything there. As a result, I've been able to test WEBP with both ImageMagick and GD and both work nicely.

I’m hopeful that most web servers will have WEBP support in either GD or ImageMagick already. Technically, it looks like both engines do a great job with WEBP, but ImageMagick might have a slight edge in this regard, depending on the case.


### WEBP is an output format

WEBP images are fundamentally different from other image formats you have used in ProcessWire. WEBP is purely an output format, not an input format. That’s because you still need a fallback JPG or PNG for any WEBP image that you serve, as not all browsers will be able to consume the WEBP images.

In addition, WEBP images have a type of compression that makes them unsuitable for any further manipulation or transformation, so PNG and/or JPG images should still be the standard for any images you upload to your site. All the WEBP images delivered by ProcessWire are automatically generated from source PNG or JPG images.


### How to tell if your server supports WEBP

A simple way to tell if your PHP has WEBP support is to make a `$page->images->first->webp->url` call and see if it outputs a webp URL or or jpg/png URL. If it outputs a webp URL then all is well. If not, try installing the *ImageSizerEngineIMagick* module (which is already included with the core) and try outputting a webp URL again. If it's still not working, then that means that neither ImageMagick or GD have webp support, and you may need to make some adjustments to your PHP configuration or ask your web host to.

Performing a CMD-F or CTRL-F find in your browser, on the output of `phpinfo()` for "WEBP" is another way to tell if your PHP has support for it.


### How to use WEBP in ProcessWire

The simplest way to output a WEBP image is by using the new “webp” property of our image fields:

```php
<?php foreach($page->images as $image): ?>
<img src='<?= $image->webp->url ?>' alt='<?= $image->description ?>' />
<?php endforeach; ?>
```

Note above how we called `$image->webp->url` rather than `$image->url`. When you call $image->webp->url it will automatically generate a webp image (if it hasn’t already) and return the URL to it. If for some reason it cannot create a WEBP version of the image (like if your server does not support it) then it will simply return the regular $image->url instead.

In many cases you’ll be resizing images before outputting them, so note that you can call the `webp` property/method on any resized image in the same way that you can call it on a non-resized image:

```
$image = $page->images->first();
$thumb = $image->size(300, 300);
echo "<img src='{$thumb->webp->url}'>";
```

If you want to save a couple of characters in typing, the property `$image->webpUrl` is the same as `$image->webp->url`:

```
echo "<img src='$thumb->webpUrl'>";
```

I mentioned earlier that you typically want to provide a fallback JPG/PNG when serving WEBP images, for the browsers that do not support WEBP. To do that, you’d want to use a `<picture>` element with an `<img>` fallback:

```
<picture>
  <source srcset="<?= $image->webp->url ?>" type="image/webp">
  <img src="<?= $image->url ?>" alt="<?= $image->description ?>">
</picture>
```

Browsers that support the WEBP image will ony download the .webp <source> version, while browsers that do not will only download the <img> version.

Next week we’ll get further into this and discuss how you can configure ProcessWire to automatically create WEBP versions of images for all of your resized images (using the `webpAdd` property), as well as some updates you can make to your .htaccess file to let Apache decide what image is best to serve the browser, and more. Though if you want to explore that now, be sure to follow [this post from Horst](https://processwire.com/talk/topic/14236-webp-support/?do=findComment&comment=184583) (and everything that follows) that discusses his WEBP implementation for ProcessWire, as well as the [GitHub WEBP pull request](https://github.com/processwire/processwire/pull/141), both of which are loaded with great info.

Also for anyone interested, the new [PagefileExtra class](../api-full/wire/core/PagefileExtra/index.md) provides the interface for the `$image->webp` object. We’ve only talked about the `url` property/method, but there there are some other methods in there for things like https URLs, file size, cache-busting URLs, etc., that might sometimes be useful too.

That’s all for this week, but we'll have some more on this next week too, so stay tuned. Big thanks to Horst for all his work in bringing WEBP to ProcessWire. For those looking for the GoogleClientAPI module update (and related FormBuilder update), I expect to have that next week—just needed to make a few more tweaks before pushing to GitHub. Hope that you have a great weekend and enjoy reading the [ProcessWire Weekly](https://weekly.pw)!
