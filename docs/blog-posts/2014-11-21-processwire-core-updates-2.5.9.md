# ProcessWire core updates (2.5.9)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.9/

## Sections


## ProcessWire core updates (2.5.9)

21 November 2014 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-core-updates-2.5.9/#comments)


### Configurable Admin Thumbnail Images

This week some new configuration settings were added that give you more control over thumbnail images in the admin. Specifically, you can set the dimensions to use for thumbnails, and a scale factor for supporting high DPI/retina output of images in your admin. When used, they affect the output of thumbnail images in all image fields, as well as in the image selection dialog box you see when inserting images into CKEditor or TinyMCE rich text fields.

The default settings are identical to the previously hard-coded settings. Meaning, thumbnail images are 100 pixels tall and a proportional width, uncropped and unscaled at 72 dpi. To change the defaults, you'd copy this section below from /wire/config.php, paste it into your site's /site/config.php, and adjust the settings as you see fit. (This is the same method to you to modify any available configuration setting in ProcessWire).

```
$config->adminThumbOptions = array(
  'width' => 0,
  'height' => 100,
  'scale' => 1.0,
  'imageSizer' => array(
    'upscaling' => false,
    'cropping' => true,
    'autoRotation' => true,
    'sharpening' => 'soft',
    'quality' => 90,
    'suffix' => array(),
  )
);
```

Lets say that you wanted to use 200px tall thumbnail images in the admin (rather than the default 100px). You would adjust the 'height' property to be 200. Or, as another example, lets say that you wanted 150px tall thumbnails, but you wanted them to be double density, high DPI, so that they look good on your Retina screen. You would set the 'height' property to be 300, and then the 'scale' property to be 0.5. That essentially says: create thumbnails at 300px height, but tell the browser to output them at 150px height (so that they look sharp on your high DPI screen). See the [/wire/config.php](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/config.php#L327) file for more information on these properties and all the others mentioned above.

These settings above are used by all of your image fields where you specify that you want thumbnails in the field settings. Your thumbnail size is retained in both list mode and grid mode of the images (though grid mode always crops to keep the images square).

These settings are also used by the image selection dialog box that you see when inserting images into a rich text field. Previously, you had to select from full-size versions of the images here, which wasn't visually ideal, though had the benefit of avoiding creation of new image variations. I prefer the new thumbnail output myself, but if you want to revert to previous the full-size image display, you can disable the thumbnails here via a checkbox in the *ProcessPageEditImageSelect* module settings.


### System Notifications Updates

The core SystemNotifications module continues to be developed and refined. This week major portions of the javascript side of it were re-factored to make a few things simpler. In addition, the notification times that are shown are now live-updated every second. You know exactly how old a notification is, rather than how old it was when the page was last loaded. These live timer updates are also particularly useful with expiring notifications. When a new notification is created that has an expiration time, you now have a live countdown timer that indicates when the notification will be automatically deleted. There were also a few other minor updates and optimizations to SystemNotifications this week.


### New ProcessHello template module for creating Process modules

You may already be familiar with [ProcessHello](http://modules.processwire.com/modules/process-hello/), a module created purely as a starting point for your own Process modules. Well, a lot of improvements have been made to the Process module system that you'd never know about if using the current ProcessHello module. As a result, we've created a [new development version of the ProcessHello module](https://github.com/ryancramerdesign/ProcessHello/tree/dev) that uses most of the new Process module features, and serves as an even better starting point for creating your own Process modules.

Note however that this new ProcessHello requires ProcessWire 2.5.5 or newer, so is primarily of use to those that are using the ProcessWire development branch. Though all of these new Process module features will soon be merged to the master branch, so now's a good time to start experimenting with them. And the new ProcessHello is a great starting point for that.

Here's a summary of the new Process module features you'll see used in the new ProcessHello module:

- Use of a [separate file and class](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.config.php) for module configuration
- Use of an [Inputfield configuration array](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.config.php), rather than programatic Inputfields
- Use of a separate [info file for module information](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.info.php), rather than a getModuleInfo method
- [Automatically installed permissions](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.info.php#L36)
- [Automatic admin page creation](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.info.php#L41)
- [Custom admin navigation](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.info.php#L41) that appears in admin drop-down menus.
- Specification of [custom icon](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.info.php#L27) for your module
- Use of new built-in [headline()](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.module.php#L74) and [breadcrumb()](https://github.com/ryancramerdesign/ProcessHello/blob/dev/ProcessHello.module.php#L78) methods

We encourage you to get on the ProcessWire development branch, install the new [ProcessHello dev version](https://github.com/ryancramerdesign/ProcessHello/tree/dev) and experiment with it. Note that the new ProcessHello doesn't attempt to use ALL available options for Process modules. It's a balance between keeping things simple and demonstrating the features most likely to be used. But there are in fact more new things you can do with Process modules. If you are interested, check out the [/wire/core/Process.php](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/core/Process.php) file that goes more in-depth on the available options.
