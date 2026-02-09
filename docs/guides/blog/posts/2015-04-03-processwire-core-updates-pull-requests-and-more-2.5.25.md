# ProcessWire core updates, pull requests and more (2.5.25)

Source: https://processwire.com/blog/posts/processwire-core-updates-pull-requests-and-more-2.5.25/

## Sections


## ProcessWire core updates, pull requests and more (2.5.25)

3 April 2015 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-core-updates-pull-requests-and-more-2.5.25/#comments)


### New FileValidator module type

Adrian submitted PR [#823](https://github.com/ryancramerdesign/ProcessWire/pull/823) awhile ago, which added SVG sanitization and validation to ProcessWire’s file field. This update (which led to a new module) is discussed in the next section below this one. This is a great thing, well thought out and implemented. But I was reluctant to add this PR for a little while because it got us involved in a new territory of very specific file validations, and it seemed like potentially opening a can of worms. By that I mean getting general purpose, loosely-coupled systems involved in things far more specific than they are meant for.

When someone says “handle this specific type” then we have to look at it as “handle any kind of type.” If we start doing specific actions for one type, then the next request will be to do similar actions for another kind of type, and so on. Suddenly our lean and general purpose InputfieldFile module is a mess of code involved in all kinds of file-format specific details (theoretically). The potential scope is at odds with the lean-and-optimized strategy for the core. It’s simply not practical for the core, or really any single system, to do this… And yet, the need is there, it’s worthwhile, and I can’t argue with the usefulness of what was in the PR. We *should* be able to do this.

What it led to is a new type of core module: FileValidator. Rather than adding SVG validation and sanitization to the core, we added the ability for validation and sanitization of any file type at upload time. If someone has specific file validation needs, as Adrian did, now they can plug them into the core. If you are interested in seeing how it works, see the new [FileValidatorModule](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/FileValidatorModule.php) class (the base for a new module type), which contains instructions on how to implement them. It’s a lot easier than you might imagine. For an example of a FileValidator module, read on…


### Validation and sanitization of SVG files

As mentioned in the previous section, the core now lets you plug-in custom validators and/or sanitizers for any kind of file, by way of FileValidator modules. The first example of such a module is Adrian’s [FileValidatorSvgSanitizer](https://github.com/adrianbj/FileValidatorSvgSanitizer) module, which enables you to validate SVG files against a configurable whitelist, and either sanitize or reject SVGs that don’t match a whitelist.

If you are using SVG images in your site, this is incredibly useful because SVG’s are effectively a text file of XML markup tags that can be manipulated as easily as an HTML document. Unlike other types of images (JPG, GIF, PNG) that can be validated by PHP itself, SVGs are a different animal and an invalid SVG might not be immediately apparent. While PW’s admin is a trusted-user environment, there’s still great benefit to finding and fixing problems at upload time rather than discovering a broken image on the front-end of your site.

If you are using SVG images in your site, we recommend installing the new FileValidatorSvgSanitizer module. Please note however that it requires ProcessWire 2.5.25 or newer, as that is the version FileValidator support was added to the core.


### Module configuration is now even simpler

One of the goals for ProcessWire 2.6 has been to make module configuration (for module authors) simpler and simpler. Back in October we introduced the [ModuleConfig](/blog/posts/new-module-configuration-options/#enter-the-new-moduleconfig-class) class to you, along with an option to specify configuration with an [array in the class](/blog/posts/new-module-configuration-options/#using-an-array-to-define-module-configuration). This week we’ve extended it further to the point where you can now optionally define it with just the array all by itself, no class needed. For example here’s the module configuration file for the new FileValidatorSvgSanitizer module:

FileValidatorSvgSanitizer.config.php

```php
<?php $config = array(
  'allowSanitize' => array(
    'type' => 'checkbox',
    'label' => __('Allow SVG files to be sanitized?'),
    'description' => __('Check box to automatically sanitize.'),
    'value' => 0
  )
);
```

The above is actually an extension of the ModuleConfig class, as ProcessWire automatically converts it to a ModuleConfig class behind the scenes. This example is really simple since it has just one field, but of course you can have as many fields and fieldsets as needed. Also note the text `__('like this')` above simply makes it translatable for multi-language support. Here's another example that we used previously to demonstrate the ModuleConfig class, but converted to the new array-only format:

ModuleName.config.php

```php
<?php $config = array(
  'fullname' => array(
    'label' => 'Full Name',
    'type' => 'text',
    'required' => true,
    'value' => '',
  ),
  'color' => array(
    'type' => 'select',
    'label' => 'Favorite Color',
    'options' => array(
      'red' => 'Red',
      'green' => 'Green',
      'blue' => 'Blue'
    ),
    'value' => 'blue',
  ),
  'age' => array(
    'type' => 'integer',
    'label' => 'Your Age',
    'value' => 40
  )
);
```

Like when using an array in the ModuleConfig class, the `value` attributes define the default and/or unconfigured value for any property. Your module will automatically be populated with any of your defined properties and user configured values. If not yet configured, the provided defaults will be populated.

Note that the `type` attributes above are simply the names of any Inputfield module. You can specify the entire module name (i.e. "InputfieldText") or you can specify it without the "Inputfield" part, which for InputfieldText would just be "text", and InputfieldInteger would just be "integer".

If using an IDE that recognizes phpdoc, you may wish to add `@property` tags above your module class so that your config properties will be easy to keep track of, for you and your IDE, for example:

```
/**
 * @property string $fullname
 * @property string $color
 * @property int $age
 */
class ModuleName extends WireData implements Module { ... }
```


### Clear page cache by matching pages with custom selector

Added Teppo Koivula’s PR [#974](https://github.com/ryancramerdesign/ProcessWire/pull/974) which added a custom selector for clearing the Page cache. This setting is accessible in template settings “Cache” tab (Setup > Templates > [any template] > Cache). Now you can select the option to “Clear this page and other pages matching my selector” when a page is saved. Once chosen, you’ll be able to create a selector to match pages interactively just like in Lister/ListerPro. When a page using your template is saved, that selector is used at runtime to find other pages that should also have their cache cleared.

What if your selector happens to match thousands of pages? That was my main concern with this feature, and reason why we didn’t have something like it before. It simply wouldn’t be practical (if even possible) to match and clear thousands of pages on every save. If the feature is there, sooner or later someone is going to use it in that way. As a result, we updated the approach a bit to bypass the loading of those pages when clearing their caches, to ensure it remains fast. Meaning, it’s now feasible for it to match and clear thousands of page caches if need be. It’s still not ideal to match and clear that many pages on every save (you will likely feel it for a couple seconds), but that’s a lot better than timeouts or running out of memory, and if you have the need to do this, it’s a small price to pay.

The granularity and power offered by this type of cache clearing is incredibly useful. You will likely see this feature make it’s way into ProCache in the near future as well.


### More control of maximum uploaded image dimensions

Added JanRomero’s PR [#1051](https://github.com/ryancramerdesign/ProcessWire/pull/1051) which adds the option to reject uploaded images that exceed a certain dimension. This update is to ProcessWire’s Image inputfield. Previously ProcessWire only provided the option to resize the image to your maximum dimension, rather than refuse it.

Since ProcessWire already has a minimum image size, something else that this enables is the ability to require an uploaded image stay within certain bounds. If the minimum size and the maximum size are identical, then that would effectively require the user to upload the image at an exact predefined dimension. That can be handy in some use cases where you need an image at a certain dimension and don’t want the server performing any resize actions on it. The benefit of avoiding resize actions is that every time an image is resized with lossy formats like JPG, there is a slight reduction in quality (which is just the nature of lossy formats). So if you’ve got a layout that requires an image at an exact size (perhaps from a predefined template or the like), and you don’t want the server resizing or recompressing the image, we think you’ll find this new feature very useful.


### PNG transparency issue fixed

Added phlppschrr’s PR [#846](https://github.com/ryancramerdesign/ProcessWire/pull/846) which corrects a PNG transparency cropping issue. Previously if you cropped a PNG that had a transparent background, that transparent background was lost after the crop. Now the transparent background remains in place as it should.


### Better error output in PageList

Added Teppo Koivula’s PR [#1052](https://github.com/ryancramerdesign/ProcessWire/pull/1052) which upgraded the error handling of ProcessPageList ajax requests. If you’ve ever experienced a never-ending load in in the Page List due to a loss of connectivity, you’ll now get an error message indicating such… rather than spending your day watching the loading icon.


### InputfieldSelector upgrade

The InputfieldSelector module was upgraded to support limiting of what fields are available for selection. While it already does this (by limiting fields to those of selected templates), it was not something that you could narrow down further. The primary use case for this is in ListerPro, so you’ll see this feature making its way into ListerPro in the next week or so.


### Planning for ProcessWire 2.6

There are still a few remaining pull requests left in the queue that we have to cover (like a couple of great additions PagePageHistory module), but we’ve now included the bulk of the pending PRs in the core. As a result, we’re going to shift more of the focus to covering all the GitHub issue reports in the next couple of weeks, as we prepare to release ProcessWire 2.6. That means we’re really trying to limit new features and enhancements for this new version, so focus will be prioritized to the bug issue reports more than feature and enhancement requests.

This isn’t a feature freeze for 2.6 just yet, but it’s close. Not to worry, everything will get covered, but many feature and enhancement requests may have to wait till after the 2.6 release. Nevertheless, if you’ve got ideas now, we always appreciate your participation so please keep posting.

Next week will be a quiet one for the core because it’ll be Spring Break here. From this side, that means the whole family is home, everyone is on vacation, and there won’t be much time for work at the computer. So next week’s blog post is likely to be more of a tips-and-tricks post than it is a core updates post, but I promise it will be worth your time, so stay tuned.

Thanks to Teppo, phlppschrr, and JanRomero for the PRs that were added this week, and thanks to Adrian for his work with SVG sanitization and PR that led to the new FileValidator module type. In addition, thank you to all of you in the ProcessWire community that are participating in and growing ProcessWire.
