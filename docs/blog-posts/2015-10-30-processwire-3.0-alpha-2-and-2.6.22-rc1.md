# ProcessWire 3.0 (alpha 2) and 2.6.22 (rc1)

Source: https://processwire.com/blog/posts/processwire-3.0-alpha-2-and-2.6.22-rc1/

## Sections


## ProcessWire 3.0 (alpha 2) and 2.6.22 (rc1)

30 October 2015 by Ryan Cramer [ 10 Comments](/blog/posts/processwire-3.0-alpha-2-and-2.6.22-rc1/#comments)

This week the updates to the core dev branch were relatively minor, but did include a few small tweaks and fixes. I've bumped the version number to 2.6.22 rc1, so this is our first PW 2.7 release candidate version and may become the 2.7 version next week, unless any major issues arise between now and then (not likely). Thanks to everyone that's been helping to test.


### ProcessWire 3.0 alpha 2

Work has also been continuing on the ProcessWire 3.x side and this week we've released alpha 2. This is a fairly major upgrade from alpha 1 in that this version now supports compiled templates and modules. What that means is that most things (that we've tested) written for ProcessWire 2.x now work in ProcessWire 3.x without changes, and without enabling the compatibility mode I mentioned in a previous post. Actually, I think we can now get rid of compatibility mode all together.

Before we get into the details, here are a few general points about file compilation:


### Compiled modules

Since ProcessWire 3.x now uses namespaces, any modules that it loads also need to recognize that. When ProcessWire 3.x detects a module that's not using a namespace, it knows that it's likely going to cause a fatal error if it attempts to include that file. So what PW does is instead copy the file to another location and automatically modify it to recognize ProcessWire's namespace. Then it uses the modified copy.

Essentially it upgrades the module for PW 3.x. The module itself still runs in the global namespace that it always has, but its references to ProcessWire have been updated to refer to the ProcessWire namespace. Of course, once ProcessWire 3.x is in stable release, hopefully most 3rd party modules will be released as 3.x native, but compiled modules should really ease the transition. If the module continues to work just fine as a compiled module, there really isn't any significant drawback.

I have personally tested numerous modules written for 2.x, and haven't found any yet that aren't working as compiled modules. Though I'm sure there are going to be some, so if you find any please let me know so that I can continue optimizing our compiler. Users of the Pro modules will be glad to know that I've confirmed all Pro modules work as compiled modules, though I'll also be releasing 3.x version of all Pro modules once we get a little further along.

ProcessWire 3.x auto detects when it should compile a module. But if you want to prevent it from compiling any modules, you can set `$config->moduleCompile = false;` in your /site/config.php file. I also want to mention that compiled modules don't add any overhead, except when they are initially compiled. If you've got lots of modules installed, it may take a minute to compile all of them. But it only has to do that once (or whenever the original module file changes). Following that, it adds no overhead, as the compiled version is the exact same PHP but just updated to reference the ProcessWire namespace where appropriate.


### Compiled template files

Like compiled modules, compiled templates enable a template file that might have problems in 3.x to run successfully without changes. Though it's not quite as necessary as with modules, since many 2.x template files are likely run in 3.x natively without changes. But if you are upgrading an existing site to PW 3.x, then chances are you'll want this option enabled, so we've enabled it by default for now.

The template file compiler does the same thing as the module compiler, updating the template file for any references to ProcessWire classes or functions to acknowledge ProcessWire's namespace, where necessary. It also considers any other files included from the template file, as well as any prepend/append files.

Compiled templates are enabled by default to ensure a smooth upgrade process, as well as to limit the namespace verbosity in your templates. Basically, we don't want you to have to see or think about namespaces unless you want to. But compiled templates can be disabled on a template-by-template basis from the "Files" tab of any template editor (Setup > Templates > [any template] > Files). It can be disabled globally by setting `$config->templateCompile = false;` in your /site/config.php file. If you do disable it, you'll likely want to add a `namespace ProcessWire;` to the top of your PHP template files where necessary.


### File Compiler modules

There are other reasons to use compiled template files. A new class of modules is now supported by 3.x, called *FileCompiler* modules. Any installed *FileCompiler* modules get the opportunity to affect the compilation process of template files. Note that *FileCompiler* modules are not applied to module files, only template files.

This has some benefits relative to the existing `Page::render` hook that many modules use to affect output. For one thing, *FileCompiler* modules only run when the original source file has changed, so they can affect output without adding any runtime overhead. For another, it can be more secure, particularly for things like text replacement engines. That's because it's impossible for compiled code to be affected by user input that is later output somewhere (like in comments or similar).


### New module: File Compiler Tags

As an example of one thing that a *FileCompiler* module could do, we've added a new module to the core called *FileCompilerTags*. Though it doesn't come pre installed, so you'll have to install it (Modules > Core > File > Tags File Compiler). But once installed, it enables you to use the existing ProcessWire {tag} syntax to refer to variables within HTML markup (it skips over anything in PHP). This is the same syntax you use elsewhere in the ProcessWire admin, so we thought it would be a good and consistent way to introduce the concept of *FileCompiler* modules. For example, here are a few things you can do once this module is installed:

```
<link rel='stylesheet' href='{config.urls.templates}styles/file.css'>

<a href='{config.urls.root}'>Home</a>

<h1>{title}</h1>
<h1>{page.title}</h1> <!-- same as above -->
<h1>{page.headline|title}</h1> <!-- headline, if populated -->

<h2>Welcome {user.name}</h2>

{body}
```

It's just a very simple tag replacement feature that maybe some will find handy whether as an example, or perhaps for front-end development files you hand off to someone that won't be using PW. This module doesn't actually implement the tag replacement on its own. Instead it hands it off to the existing tag replacement already built in ProcessWire.

While this is just a simple tag replacement, we do think it serves as a good example for those that want to explore the possibilities further. For example, there are already modules like Twig available for ProcessWire, and *FileCompiler* likely provides a much better path for such 3rd party modules.

This particular module is in the core presently, but will likely be moved out of the core once 3.x has representation in the modules directory. But for those interested in implementing their own *FileCompiler* module(s), we'd encourage you to use the *FileCompilerTags* module as a potential Hello World example of implementing this module class.


### How to help test ProcessWire 3.x

While we don't recommend using ProcessWire 3.x in production environments yet, we do encourage early adopters to use it in non-production environments for testing when/if you want to, especially now that 3.x should be mostly compatible with 2.x thanks to module/template compilers. Please let us know when you run into errors so that we can continue making 3.x better and better.


### Upgrading and downgrading from 3.x

It's a fairly simple matter to upgrade or downgrade from ProcessWire 3.x, and I've been doing it continually with my own development sites. ProcessWire 3.x doesn't actually change anything about the database (relative to 2.6 dev), so you can easily switch out the core versions without affecting the database.


### Upgrading 2.6 dev to 3.0

- If you didn't run into any significant errors, you are now successfully running on PW 3.x.


### Downgrading 3.0 to 2.6

1. Reverse the changes you made in the upgrade, removing or renaming the existing index.php and /wire/ directories as a backup, then renaming the ones from 2.x back in place. If you used our example earlier, you'd rename .index.php to index.php and .wire to wire.

2. Your 2.x installation should now be restored. *Optional:* for housekeeping, you can delete the contents of this directory if you want to: /site/assets/cache/FileCompiler/.
