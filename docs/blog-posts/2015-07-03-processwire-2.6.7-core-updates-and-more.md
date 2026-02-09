# ProcessWire 2.6.7 core updates and more

Source: https://processwire.com/blog/posts/processwire-2.6.7-core-updates-and-more/

## Sections


## ProcessWire 2.6.7 core updates and more

3 July 2015 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-2.6.7-core-updates-and-more/#comments)


## ProcessWire 2.6.7

This weeks new version of ProcessWire includes several minor bug fixes, a few PRs, and some nice new features. A lot of attention this week was put towards getting up-to-date with recent GitHub issue reports and PRs, and that will continue. Last week's version (2.6.6) focused on improvements to many core Inputfields in support of dynamic insertion, and those updates continued into this weeks version as well. If you are tracking the dev branch of PW, we recommend upgrading to 2.6.7 to enjoy the latest features and refinements. Following upgrade, be sure to click Modules > Refresh (as with any version upgrade) so that core module versions are updated. This ensures you that you don't have potentially older versions of PW's CSS and JS files stuck in your browser cache–a lot of them have changed recently.


### New core files for site hooks

The abundance of hooks and ease of hooking nearly any method in PW are widely enjoyed by ProcessWire users. This week we added support for standardized include/hook files so that you can easily attach hooks without having to create a module or make guesses over where is the best place to add your own hook functions.

If using ProcessWire's [$config->prependTemplateFile](https://github.com/ryancramerdesign/ProcessWire/blob/master/site-default/config.php#L41) option, this has always been a decent place to put your own hook functions. But there are also a few problems with this method:

Enter ProcessWire's new standardized include/hook files, which are included on every request (when they exist), and answer all of the issues mentioned above. These include/hook files receive all ProcessWire API variables in local scope, just like template files. The names of hook files correspond to ProcessWire's [runtime states](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/ProcessWire.php#L41). The new standardized hook files include the following:

**/site/init.php** This file is included during ProcessWire's boot initialization, immediately after autoload modules have been loaded and had their `init()` methods called. Anything you do in here will behave the same as an `init()` method on a module. When this file is called, the current `$page` has not yet been determined. This is an excellent place to attach hooks that don't need to know anything about the current page.

**/site/ready.php** This file is included immediately after the API is fully ready. It behaves the same as a `ready()` method in an autoload module. The current `$page` has been determined, but not yet rendered. This is an excellent place to attach hooks that may need to know something about the current page. It's also an excellent place to include additional classes or libraries that will be used on all pages in your site.

**/site/finished.php** This file is included when ProcessWire has finished rendering and delivering a page, and is in the process of shutting down. It is called immediately before the API is disengaged, so you can still access any API variable and update `$session` values as needed. Admittedly, this is probably not the place you would put hooks, but it is an ideal place to perform your own shutdown, should your application call for it.

To start using these include/hook files, all you need to do is upgrade to ProcessWire 2.6.7 (or newer) and create one of the above files. Read on for an example…


### Going beyond hooks

We've introduced these files as standardized include/hook files because that's the most common use case scenario. However, these are just regular PHP files that get included at certain key points in ProcessWire's request handling process. They enable you to get into things that previously would have required a module to accomplish. But you may find them to be useful for much more than just attaching hooks.


### Include/hook file example

I'm currently developing an application for a client where I need to attach hooks, as well as include one or more other helper class files. The ready.php hook turned out to be ideal for this particular application. The ready.php attaches a hook, as well as establishes a `$cart` API variable for all templates in the site, provided via an external *ProductCart* class. Here is an abbreviated example:

/site/ready.php

```php
<?php

$pages->addHookAfter('saved', function($event) {
  $page = $event->object;
  if($page->template == 'product') {
    // update other related pages when 'product' page is saved
  }
});

if($page->template != 'admin') {
  // include an external helper class...
  require('./classes/ProductCart.php');
  // ...and establish it as a new $cart API variable, and
  // populate it with products saved in the user's session:
  $wire->wire('cart', new ProductCart($session->productsInCart));
}
```

There is also a /site/finished.php that obtains the products from the `$cart` and saves them back to the session, ready for the next request:

/site/finished.php

```php
<?php

if($page->template != 'admin') {
  $session->productsInCart = $cart->getArray();
}
```

Granted, you could certainly have found a way to do this all before, but there would have been no way for me to tell you exactly how and where to do it, because the answer would be *"it depends on how you are using your template files."* With these new standardized include/hook files, there is now a universal way to accomplish these sorts of tasks without needing to develop a module for it.


### Continued updates for ListerPro

Last week ListerPro got [editable columns support](/blog/posts/inline-ajax-page-editing-comes-to-listerpro-processwire-2.6.6/), giving you and your clients the ability to edit any field from any page, directly from within your Lister. A few of us have become addicted to editing this way. For me, it's been a big time saver on sites I currently have in development...

For example, I had to upload different company logo images to a dozen different product pages. Rather than going and editing each of those pages individually, I went to Pages > Find (to the generic ListerPro), and matched `template=product, logo.count=0`, and that gave me a Lister with all product pages that didn't yet have a company logo image. On a single page in ListerPro, I was able to drag and drop all of those company logo images in place. Something that might have taken me 10 minutes before instead took under 2 minutes.

In using it extensively to manage content this week, there were opportunities for several tweaks, additions and adjustments to make it even better. As a result, there was a new version of ListerPro (version 1.0.4) released today that expands on what was introduced last week. Registered users can download it now in the ListerPro support board.

In addition to some refinements and bug fixes, this version also improves support for file/image fields, and adds support for changing the *parent* of pages. If a page you are editing has less than 100 possible parents, it will give you a regular select box to choose one from. If there are more than 100 possible parents, then it will give you a PageListSelect input.

This latest version of ListerPro requires the current version of the ProcessWire dev branch (2.6.7). If you are currently running ListerPro 1.0.3, we recommend you upgrade to ListerPro 1.0.4 and ProcessWire 2.6.7. Hope that you enjoy these updates and please let us know how they work for you.


### New version of AdminThemeReno on the way

Yesterday Tom Reno (Renobird) sent over a new version of his core admin theme (AdminThemeReno) to include on the dev branch. I'm very excited to get this new version integrated into the core. There wasn't enough time to include it in this weeks updates (today is a holiday here in the US, so time at the computer has been somewhat limited). But we'll definitely be getting this one in place next week, so stay tuned!

Hope that you all have a great weekend (and week). As always, remember to tune in to Teppo Koivula's fantastic [ProcessWire Weekly](http://www.flamingruby.com) Saturday morning.
