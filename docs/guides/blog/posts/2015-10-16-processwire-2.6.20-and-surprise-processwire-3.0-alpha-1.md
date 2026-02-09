# ProcessWire 2.6.20 and surprise: ProcessWire 3.0 alpha 1

Source: https://processwire.com/blog/posts/processwire-2.6.20-and-surprise-processwire-3.0-alpha-1/

## Sections


## ProcessWire 2.6.20 and surprise: ProcessWire 3.0 alpha 1

16 October 2015 by Ryan Cramer [ 14 Comments](/blog/posts/processwire-2.6.20-and-surprise-processwire-3.0-alpha-1/#comments)


### Two ProcessWire versions this week!


## ProcessWire 2.6.20

This week (and last week) we continued on the path of keeping up-to-date with GitHub issue reports and covering all the issues that come up. There have yet to be any major issues reported, so we're focused on just minor things here, and it seems like we're about ready for release of 2.7. We're aiming to release it at the end of October, 1-2 weeks from now. Since the quantity of issues to cover has been getting smaller, we've taken the opportunity to put some more work into the 3.x branch of ProcessWire, which is also covered in this post.

A couple of improvements were added in 2.6.20 as well. Specifically, the empty-trash and page-clone functions have been updated to support much larger scale operations. Previously some people were running into issues when trying to empty the trash when it had thousands of items in it, or recursively clone a branch of pages that had thousands of pages. Following this week's update, those operations can now be performed on a larger scale. These still can't be performed on an infinite scale though. For instance, if you've got a 100k pages in your trash, it'll probably take several empty operations before they are all cleared out.

If you have a chance, please grab the latest dev branch version 2.6.20 and let us know how it works for you!


## ProcessWire 3.0 alpha 1

We are making progress on ProcessWire 3.0 and have created a new branch on GitHub for it, called the [devns](https://github.com/ryancramerdesign/ProcessWire/tree/devns) branch. This is work in progress, so do not use it in production, as things are still likely to change. However, if you are interested in following it, feel free to give it a try.


### How is this version different from 2.6/2.7?

Currently it's identical in functionality to the current dev branch (2.6.20). Where it differs greatly is on the code side. Here's what's different in ProcessWire 3.0 alpha 1:

The above is how this version is different now, but of course there's a lot more on the way.


### What benefits will using namespaces bring?

It kind of depends on the developer (you). For many it simply won't matter. For others, it'll be a breakthrough. Whether it matters to you personally or not, it's a good thing for the ProcessWire project. It positions ProcessWire well for the future, helps how ProcessWire is perceived relative to other projects, and will help attract new users to ProcessWire. Here's a few more details on the technical benefits:

Using namespaces means that ProcessWire can be integrated with other PHP projects more easily, further strengthening its usability as a PHP framework. As an example, take our old friend WordPress (maybe not the best example, but at least it's one everybody will recognize). You could not easily include ProcessWire from WordPress because the two had name collisions on some classes and functions. Since ProcessWire now runs in its own namespace, it can be included in many situations that it could not have before. So if you want to pull a ProcessWire instance/API into a WordPress site (or any other PHP application or framework) now you can. Granted, you could already do that in a lot of cases, but namespaces open the door to being able to do it just about anywhere.

A traditional benefit of using namespaces in PHP is ease of autoloading classes (like the PSR-4 autoloading standard). ProcessWire itself doesn't use a PSR autoloading standard for its own classes and modules, as it already has something better suited to the core and our module system. But it is fully compatible with PSR-4, and even implements its own PSR-4 autoloader for those that want to define their own namespace roots to autoload their own classes from. You can define your own PSR-4 namespaces and corresponding paths using the new `$classLoader` API variable in ProcessWire 3.0. We'll get into more detail on this in a future post for those that are interested.

In 2010 when the first open source release of ProcessWire came out, namespaces weren't very common among CMS projects, and there wasn't a real compelling case for using them except for dedicated frameworks and other specific needs. Then along came Composer, autoloading standards and more… and today using namespaces is kind of a default assumption and best practice for any PHP project. We're all about best practices, how the project is perceived from outsiders, and how well it adapts to your future needs and scale. Adopting namespaces made a lot of sense for the 3.x major version, even if many of us don't need them immediately.


### Namespace considerations for template files

One reason ProcessWire hasn't used namespaces before is that they run a little counter to our philosophy of keeping the API as absolutely simple as possible. Namespaces add verbosity, and if you don't actually need namespaces, then you may find that verbosity annoying. What do I mean by verbosity? I mean `namespace ProcessWire;` at the top of your PHP files, or an alternate namespace if you so choose. That's really all there is to it. It's not much verbosity granted, but it's there nevertheless. If it's useful to you, you'll love it. But if it's not, then you may perceive it as unnecessary technical jargon.

The good news is that use of namespaces in your template files will be optional in many (or most) cases. But there will be some cases where template files will need the ProcessWire namespace added to them in order to recognize the new context. Though 3.x also comes with a 2.x compatibility mode `$config->compat2x = true;` that lets most sites designed for 2.x continue running normally in 3.x, without overhead.

ProcessWire 3.x will also come with a template compiler that takes care of making sure templates are 3.x compatible at runtime. It does this by automatically updating them with a namespace (when needed) without you having to think about it. Compiled templates will also provide some other benefits, such as the ability to natively support other template engines and have them automatically compiled to PHP every time a change is made. A simple example would be automatically converting markup like `<a href='config.urls.root'>` to `<a href='<?php echo $config->urls->root; ?>'>` which could simplify the appearance of your markup during development. While ProcessWire's core doesn't (and won't) use full template engines by design, compiled templates will open up an interesting new class of 3rd party modules available for ProcessWire installations that wasn't previously possible.

When will using a namespace be necessary in template files? When you use ProcessWire's `wire()` function (or other wire* functions), or if you refer to ProcessWire core class names like `Page` and `PageArray` in your template files. Use of API variables ($page, $pages, $modules, etc.) does not require use of namespaces. In fact, all of ProcessWire's default site profiles were able to run without any changes to them. Nevertheless, we think many will find it to be worthwhile to declare a namespace at the top of your template files when creating new sites in ProcessWire. For those that don't care about namespaces, you can ignore them in your template files unless PHP complains.


### Namespace considerations for 3rd party modules

When it comes to 3rd party module developers, there's a more certain chance that modules will need to be updated for this namespace change. Compatibility mode will enable many 3rd party modules to run without a change. But when a module is made natively for 3.x it will want to either use the ProcessWire namespace, or declare its own. Essentially, a module can be updated for 3.x support simply by adding `namespace ProcessWire;` at the top of the module file.

If a 3rd party module developer wants to go further and declare their own namespace, they can. The ProcessWire core will identify it and call it appropriately. Further, modules that declare their own namespace will automatically receive PW's PSR-4 autoloader for any class/file dependencies the module might have, rather than having to require() or include() them manually. Though unless the module is particularly broad in scope, we suspect that most module authors will simply use the ProcessWire namespace. But for modules that include other classes/files, it might make a lot of sense to take advantage having your own namespace.


### When will ProcessWire 3.x be released?

ProcessWire 3.x likely won't be released in stable form till spring 2016. While we've made a lot of progress already, there's still much more to do. However, we're really happy that we can already bring some of the goods to you today, and we'll have a lot more coverage of 3.x in upcoming blog posts.


### How many more versions will be in the 2.x branch?

After ProcessWire 2.7, we'll continue updating both the 3.x and 2.x branches with the same features, optimizations and fixes. 2.7 may be the last major version on the 2.x branch, but there will likely be several minor versions. If there's a compelling reason for there to be a 2.8 then there will be, but we'll play that by ear. Our plan is to make sure that 3.x is an easy and minor upgrade from 2.x by the time it is released as stable.


### What namespaces does ProcessWire use?

ProcessWire's core uses a single "ProcessWire" namespace, at least from the perspective of the public API. Modules and templates may also use this namespace if they want to, or they may define their own namespaces as they see fit. ProcessWire may also use the root namespace, but only if you enable 2.x compatibility mode with `$config->compat2x = true;` in your /site/config.php file.

ProcessWire 3.x's modules system has full support for whatever namespace the module developer chooses. We will be recommending that module developers use a custom namespace in cases where they may be defining other classes outside of their module, as this limits the possibility of name collisions with other modules that might define similar class names.

The core doesn't use a complex hierarchy of namespaces like some other frameworks because it simply doesn't need them. We also don't want to introduce unnecessary verbosity to our public API. Our autoloading mechanism has no namespace dependency, and our system is based on a bootable API rather than a framework of components that can be used in isolation. ProcessWire's core may however use additional namespaces internally for components that won't be seen on the public API.


### Where to get 3.0 alpha 1?

This version is available as the [devns branch on GitHub](https://github.com/ryancramerdesign/ProcessWire/tree/devns). Go there to download the zip or clone it with git. Just remember this version is an alpha preview and not something you should start upgrading your sites to yet! :)

If you have any questions or comments on the ProcessWire 3.x branch or any of the new things that it brings, we'd enjoy hearing from you! Please comment below. Be sure to read Teppo's [ProcessWire Weekly](http://weekly.pw) this weekend!
