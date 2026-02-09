# ProcessWire 3.0.63 adds client-side image resizing

Source: https://processwire.com/blog/posts/processwire-3.0.63-adds-client-side-image-resizing/

## Sections


## ProcessWire 3.0.63 adds client-side image resizing

26 May 2017 by Ryan Cramer [ 19 Comments](/blog/posts/processwire-3.0.63-adds-client-side-image-resizing/#comments)


## ProcessWire 3.0.63

Client-side image resizing has been on our roadmap for awhile, and this week we've got it ready on the dev branch in version 3.0.63. People expressed interest in this feature in the comments to last week's post, and I promised to give it a closer look sooner rather than later. After getting that closer look, and doing some research, I realized we could get in this week's version. After using it now for a couple of days this week, I think people are really going to like this feature, and it works a lot better than I had originally guessed it could.


### Why client-side image resizing?

Just in case you don't know what it is, client-side image resizing is a means by which you can take a really big image/photo file, drag it into a ProcessWire images field, and have it upload a smaller version of it automatically. It's especially ideal for photos coming directly off high-megapixel digital cameras (and phones) that produce giant JPEG files. But it's useful for any case where where you are dealing with large JPG, PNG or GIF files.

ProcessWire has always been able to resize images at the server side, but they have to be uploaded to the server before they can be resized. Meaning, if you had several photos to upload at 10-megabytes each, you'd likely have to take a lunch break while your photos uploaded. (Sometimes they may even be too big to upload at all). Then even after they uploaded, big images can be time consuming to resize at the server side. In some cases, your server may not even have enough memory to complete the resize.

Client-side image resizing bypasses all of that time by letting the web browser resize the image before the upload starts. Web browsers seem particularly well optimized to this task. Chances are you won't ever need those giant 20-megapixel photos displayed in your website, so having the ability to automatically bypass uploading them at that size is a real time saver that benefits pretty much everyone using ProcessWire.

You and I know how to use Photoshop (or some other tool) to resize images to something reasonable before uploading them. It's a pain and it's a hassle, but we've done it when we needed to. Client-side image resizing takes all the pain and hassle out of it for you and me, which is great. But where it's even better is for our clients. So often, people have big photos to upload, but no tools to prep them… and no background on why one would want to. They need to upload a gallery of photos, but it's either taking forever or not working at all, you get a call, and then it becomes your problem.

One time I got a call from a client that was trying to upload images that were press-ready, and magnitudes larger than what could reasonably by uploaded and used on the website. They had no tools to resize the images. I ended up having them drag the images into blank browser windows (letting the browser scale it to fit the screen). Then they'd take a screenshot of the browser window, and upload the screenshot. I'd call that a dumpster fire to toast marshmallows. It worked, but… whew. No longer will such insanity be necessary. What's funny is that this process isn't all that far off from a laymans description of how client-side image resizing actually works – your browser is scaling a large image, saving the scaled version, and uploading it – except that it's all happening automatically.


### How do you use client-side resize?

In order to use client-side image resizing, you have to define the maximum dimensions allowed for your images field(s). You may already be familiar with these settings, since they've been there for a long time. But in 3.0.63, they now default to client-side resize rather than server-side, making it a lot more useful. If you are already using the max width/height settings, then client-side image resizes will already be enabled as soon as you upgrade to ProcessWire 3.0.63.

If you aren't using max width/height settings currently, but want to, then go ahead and enable them. You can do this by editing your images field(s) (Setup > Fields > Edit [field] > Input [tab]), and either populating the “max width/height” settings, OR the new “max megapixels” setting.

To accompany the new client-side resize option, we've also added a couple more settings, which you'll see in the screenshot below:

Screenshot from ProcessWire admin in Setup > Fields > Edit [image field] > Input [tab].


### Developing client-side image resizing

Client-side image resizing involves HTML5-specific browser features, the canvas element, and a lot of Javascript. I found out that basic client-side resizes are fairly simple on the JS side, but resulting quality can be a problem unless the resize is exactly half the scale of the original. When you get into really high quality client-side resizes that are flexible enough to allow resize to any scale, that's where things get pretty complex. It's far beyond my expertise, so I knew we'd have to work with an existing solution.

What I found is that there are not many existing solutions out there. Searching Google for "client side image resize" already has ProcessWire.com as one of the top results… to a thread of users discussing client-side resizing as a potential PW feature.

After some more hunting around, I came across an older project on GitHub called [ImageUploader](https://github.com/rossturner/HTML5-ImageUploader) by Ross Turner. It seemed to put good emphasis on maintaining quality in scaled images, more-so than the others I looked at. It handled auto-rotation on the client side as well. I found the code easy to follow and developed in a manner that we could adapt for use by ProcessWire's InputfieldImage module.

I ended up forking that library into a new library called [PWImageResizer](https://github.com/processwire/processwire/blob/dev/wire/modules/Inputfield/InputfieldImage/PWImageResizer.js). This library isolates the resizing, removes the uploading, adds support for more image types, restructures and fixes a few things, and presents an API that works nicely with InputfieldImage. There's a week worth of work in there adapting it for PW, but it is otherwise identical to ImageUploader when it comes to the actual heavy lifting of client-side image resizes.


### Resize settings and performance

Client image resizing works with JPEGs, PNGs and GIFs. PNGs and GIFs are lossless, but JPEG is lossy and thus has a “quality” setting that you can configure (see earlier screenshot). Our default quality setting is 90, which seems like a good one to use for most cases–it provides a nice balance between quality and file size. However, I'd suggest also trying out 80 (or anything in between) just to observe the difference in file size and quality to see what benefits your needs the most. Just for fun, try out 10% too – just don't leave it there!

We have a new “maximum megapixels” setting, which can be quite useful. It can be used alongside–or instead of–the max width/height settings. It's particularly useful in cases where you want to have a size limitation, but not specific to width or height dimensions. For instance, if you specify that you want to have a max megapixels of 1.7, that means you want to resize images that have more pixels than 1600x1000, 1000x1600 or any combination of dimensions that happens to add up to a quantity greater than that number of pixels.

I've not tested much outside of the current Chrome just yet, so it's possible results may be different in other browsers and versions. We'll migrate this feature to the master branch once we can confirm it works equally well in a broader context too. Please let us know if you run into issues in your own testing.

Within the testing that I've done this week, I've found client-side image resizes are FAST! So fast that you may not even know it's happening in many cases… and may not know, unless you go back and click the image after upload to observe the size and dimensions. I'd set my max width/height to 800x600 for testing, and was uploading 8-megabyte images having dimensions around 4608x3072. On my oldish MacBook Pro in Chrome, the resize takes about 2 seconds, short enough that it's not apparent. Because the resulting image is so much smaller, the upload that follows is likewise very fast. Then I tested with a 27-megabyte “world satellite map” jpeg having dimensions of 21600x10800, and this one was understandably slower, coming in at about 15 seconds to resize (still a lot faster than server-side though, if even possible). It resized that massive jpeg to an 800x400 image consuming just 78 kb.

That's all for this week. Hope that you all have a great weekend, and please let us know how the client-side image resizing works for you. For more ProcessWire news, be sure to check out the [ProcessWire Weekly](http://weekly.pw) this weekend too.
