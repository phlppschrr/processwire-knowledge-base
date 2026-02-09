# ProcessWire 3.0.118 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.118-core-updates/

## Sections


## ProcessWire 3.0.118 core updates

2 November 2018 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-3.0.118-core-updates/#comments)


## ProcessWire 3.0.118

This week we've got core updates in ProcessWire version 3.0.118 on the dev branch. This version contains several updates but the most significant is a convenient addition for viewing and editing page redirects.


### New $page API redirect methods

Several weeks back in [3.0.107](/blog/posts/processwire-3.0.107-core-updates/#page-gt-urls) we added the [$page->urls()](/blog/posts/processwire-3.0.107-core-updates/#page-gt-urls) method, which returns an array of all the URLs that will redirect to a Page. These URLs are automatically created by the core *PagePathHistory* module any time you move or rename a page. It ensures that if any links were pointing to the old URL, they will continue to direct the user to the right destination. This week we've added two API methods for managing those URLs:

```
// add a new URL that redirects to $page
$page->addUrl('/some/url/');

// remove an existing URL that redirects to $page
$page->removeUrl('/some/url/');
```

The `$page->addUrl()` method simply adds a new URL to the page. When an added URL is accessed, the URL will redirect to the Page using a 301 permanent redirect. The `$page->removeUrl()` method does the opposite, removing a previously added URL, whether it was one you added, or one that was auto-generated from a previous page move/rename.

These methods are actually just a simpler interface to the core *PagePathHistory* module. In fact, these two methods are added to the Page class via hooks from the *PagePathHistory* module. However, you don't actually need to use the API in order to manage these URLs anymore…


### New redirect URL management in the page editor

Related to the above section on new Page add/remove URL methods, the Page editor now has a new Fieldset that gives information about all the URLs redirecting to a page. You can find this on the *Settings* tab when editing any Page, and it is close to the last field on that tab, labeled “What pages redirect to this one?” Note that it is currently only visible to the Superuser.

The URLs shown in this fieldset represent former locations of the page that were automatically added as a result of page movements or name changes. But what's nice is that now you can manually delete existing URLs AND add new ones from here. So this new section is not just informational, but also quite useful if you need to setup any new redirects.


### More about these redirecting URL features

There have been feature past requests for some kind of UI to manage *PagePathHistory* URLs. Though this solution might be a little different than what was originally requested, since they are managed in the Page editor.

Having this editable at the Page level is something I've had a need for before, and in developing the new ProcessWire.com website, the need arose once again. I figured it was time to go ahead and implement it.

The site structure changes in several ways on the new ProcessWire website, and this means many URLs also change. There are 8-years worth of links coming into the site externally, internally, from the forums, and even from ProcessWire's admin (as contextual help links in the admin).

All these links must keep working, even if they redirect to new locations. Since we're building this as a new website from the ground up, there's no built-in history of URL movements, so many of the redirects need to be added on a page-by-page basis. This new feature in the Page editor makes my job easier, as it will for anyone converting any existing site into ProcessWire (whether running in a different platform or not).

This new feature might also be useful for those wanting to create shorter links to key pages, like for sharing purposes. For instance, I might have some important, but deeply buried page that I want to have an easy-to-remember URL for. Lets say I had a Page at URL /products/scooters/electric/xiaomi/m365/. This is a particularly popular product, so the client wanted to have a URL they could easily recite to their customers over the phone. They could edit that page and add the URL /m365 that automatically redirects to that Page. After that, they'd only have to recite domain.com/m365 to their customers over the phone, which can save a lot of time and reduce transcription errors.


### Limitations on redirects

Currently these redirect features (API and page editor) are very much tailored towards ProcessWire page name format URLs. It doesn't accept things like query strings or fragments. Nor does it let you target alternate URL segments at the destination Page. That's because it's the *PagePathHistory* module that's handling it, and its original purpose is purely to remember past URLs of pages. Now that you can add redirects to it manually as well, we may have to expand upon that and support more, as I'm sure the need will come up sooner or later.

Another limitation is that this feature is very much for individual cases of specific redirect URLs. This is not going to replace setting up rewrite rules in your .htaccess file, where you can use regular expressions to dynamically match and create redirect URLs, capture and replace variables, etc. On the processwire.com site, we'll no doubt be using redirects in the .htaccess file too, especially in cases where we can setup a single rule that will handle lots of URLs in one shot.

Lastly, using .htaccess redirects is also preferable from an efficiency standpoint. Redirects in your .htaccess file happen before PHP or MySQL is loaded and before ProcessWire is booted, so they are pretty much immediate. When there's a redirect that is going to be getting hit all the time, it might still be preferable to put it in your .htaccess file.

For example, maybe you are replacing an old site powered by static html files with a new ProcessWire powered site. Here's how you might setup those redirects in your .htaccess file. This would be somewhere after the `RewriteEngine On` line:

```
RewriteRule ^index.html$ / [R=permanent,L]
RewriteRule ^about.html$ /about/ [R=permanent,L]
RewriteRule ^news.html$ /about/news/ [R=permanent,L]
RewriteRule ^faq.html$ /about/faq/ [R=permanent,L]
```

Or maybe you want to keep some of those old HTML files around, but move them off to an /oldsite/ directory and ensure that their original URLs still work, without redirects

```
RewriteCond %{REQUEST_URI} \.html$
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ oldsite/$1 [L,PT]
```

To conclude, the redirects feature in the page editor (and API) is going to be really useful for a lot of cases, but there may still be cases where you want to stick with handling your redirects from the .htaccess file.


### New $files API var methods and improvements

Among other things, the `$files` API variable replaces a lot of the PHP file functions with more secure and contextual versions, when possible. But there were a couple of things missing. This week, new `$files->unlink()` and `$files->rename()` methods were added to round out the $files toolset. These methods handle deletion and renaming of files, and they accompany the existing related $files methods: copy(), mkdir(), rmdir(), and chmod(),

Relative to the PHP versions of the these file functions, they add another level of security by imposing some additional limits. Specifically, they don't allow you to work with any kind of relative paths, they can block traversal outside of a designated root path, and they can optionally throw Exceptions when a failure occurs (rather than just returning false). Like other $files methods, the new rename() method also adjusts file permissions to be consistent with your $config settings.

```
// examples with only required arguments
$result = $files->unlink($filename);
$result = $files->rename($oldFilename, $newFilename)
```

In places where the core used the PHP versions of these functions, I've switched it to use the new $files API versions. For more information about these methods and the other arguments they support, see the [WireFileTools](https://github.com/processwire/processwire/blob/dev/wire/core/WireFileTools.php) class on GitHub for [unlink](https://github.com/processwire/processwire/blob/dev/wire/core/WireFileTools.php#L285) and [rename](https://github.com/processwire/processwire/blob/dev/wire/core/WireFileTools.php#L326).


### Other updates

This week the version of Uikit used by *AdminThemeUikit* was updated from a beta version to an release candidate version (rc17). They are actually already at rc20, but since I've been testing rc17 here for a couple weeks, that's the one committed to the dev branch for now. I'll likely make an another update to this soon, but it looks like Uikit 3 is getting very close to a final version. In my own usage, Uikit 3 has been very stable for quite a long time.

Work continued on development of the new processwire.com site this week, though it was primarily in writing copy, not in development. I thought I'd make it into the /about/ section, but am still working on writing copy in the /docs/ section. I read in the forums that some of you have found use of videos to be very effective too, so I'll be looking into using more videos on the upcoming site where possible. Though will probably come back to that after all the content is finalized.

That's all I have for the updates this week. If you are in the US, be absolutely certain to [vote on November 6th](https://votesaveamerica.com/ballot) next week. And remember to check in at the [ProcessWire Weekly](http://weekly.pw) this weekend for the latest ProcessWire news and updates! I'm posting to the blog early today because I'm headed out of town this morning and for the weekend—my wife is running a marathon in a different city, so I'll be away from the computer for a bit, but back on Monday. Hope that you have a great weekend!
