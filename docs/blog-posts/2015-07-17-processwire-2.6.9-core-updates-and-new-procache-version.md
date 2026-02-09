# ProcessWire 2.6.9 core updates, new ProCache version, and more

Source: https://processwire.com/blog/posts/processwire-2.6.9-core-updates-and-new-procache-version/

## Sections


## ProcessWire 2.6.9 core updates, new ProCache version, and more

17 July 2015 by Ryan Cramer [ 7 Comments](/blog/posts/processwire-2.6.9-core-updates-and-new-procache-version/#comments)

This week's core updates include a useful new API method and more configuration options for slash settings in URL segments and paginations, among other tweaks, fixes and details. We've also released a brand new version of ProCache today with some really great enhancements, and we'll cover all of them in this post.


## **ProcessWire core updates for 2.6.9**


### New $page->setAndSave() method

This new method does exactly what it says: sets a value and saves the page. Now of course, that's something you can already do quite easily, but it required a few lines of code or chain of method calls. Now you can do it with just one method call.

```
$page->setAndSave('property', 'value');
```

For comparison, here's what you might do without it:

```
$of = $page->of();
$page->of(false);
$page->set('property', 'value');
$page->save('property');
$page->of($of);
```

Make note of those `$page->of();` calls above. That's what you'd do if you had a $page in an unknown output formatting state, *or* an output formatting ON state (as in the front-end of a site). In order to set a value to be saved to a page, in needs to have output formatting disabled, ensuring that you are working with raw data for saving, and not something like entity encoded text or the like. So the above code remembers the output formatting state ($of), turns output formatting off, sets a value, save the page, and then restores the previous output formatting state. That's a mouthful, but a healthy and important one.

The new `$page->setAndSave()` method does all of that (mouthfull) in a single call. It takes care of remembering and restoring the output formatting state. In return, it's trusting you to provide a value that doesn't have any output formatting applied to it (entity encoding, etc.). So consider this a convenience method for those of you who know what you are doing (i.e. know the difference between formatted and unformatted output) and don't want to fuss with the extra safety provided by the usual way.

As a bonus, this new method also supports setting multiple properties at the same time too. Just give it an array of property => value instead:

```
$page->setAndSave(array(
  'title' => 'It is Friday again',
  'subtitle' => 'Here is another new blog post',
  'body' => 'Hope you all have a great weekend!'
));
```


### Real world example of using setAndSave()

Let's say that you added a `last_login` date/time field to your user template, and you wanted it to update with the current date and time every time they logged in. Here's how you might use the setAndSave() method:

file: /site/ready.php

```
$session->addHookAfter('loginSuccess', function($event) {
  $user = $event->arguments(0);
  $user->setAndSave('last_login', time());
});
```

Pretty simple huh?


### Control of trailing slashes with URL segments and page numbers

ProcessWire has always given you control over the trailing slash setting of pages, enabling you to enforce a trailing slash (or no trailing slash). But that setting has never applied to extra parts of the URL that may get appended from URL segments or pagination numbers. It would simply accept either.

ProcessWire 2.6.9 now gives you independent control over trailing slashes on URL segments and/or paginated URLs. It will enforce them with each request, 301 redirecting to the URL you intend if accessed at one you didn't intend. Of course, if you still prefer the free-form behavior from before, it's still there as an option (and is the default). But now when you check the box to enable URL segments or page numbers (when editing a template), you'll see another box appear to the right of it asking for your trailing slash preference.


## **New version of ProCache (3.1)**

Today we released a new version of ProCache with a lot of great enhancements to HTML minification, cache clearing behaviors, core integration and more. This beta version is available for download now in the ProCache support board.


### Major enhancements to HTML minify capabilities

ProCache uses our own homegrown HTML minify library, and we're constantly optimizing and improving it. The result is in ProCache 3.1. I now believe we have the best HTML minify library available. I've compared it with other popular HTML minify libraries, and have found ours can save more bytes than any other library I've tested with… and often, significantly more so. If you can find an HTML minify library that can minify your HTML better than ours, we'd like to know about it. Here are some of the new features added in ProCache's HTML minification tool:


### Ability to remove unnecessary assumed attributes from HTML tags

Several HTML tags have default values that don't need to be specified. For instance, an `<input>` and an `<input type="text">` are the same thing, so there's no need to have those extra `type="text"` bytes in minified HTML. ProCache strips out unnecessary attributes from all HTML tags where supported. This currently includes specific attributes from `input`, `script`, `style`, `link` and `form` tags.


### Ability to collapse boolean attributes

In HTML5, `selected="selected"` and just `selected` are equivalent, so there's no need to have the longer version in minified HTML. There are in fact **44** different boolean attributes that ProCache will collapse for you automatically in the minified output.


### Removal of specified blank attributes

It is safe to remove certain blank attributes from HTML, as they aren't doing anything but taking up space. ProCache will automatically remove these blank attributes: `class`, `dir`, `for`, `id`, `lang`, `style`, and `title`. Those are just the defaults. You can configure this feature in ProCache to remove any other blank attributes you'd like too.


### Removal of HTML5 closing tags that are considered optional

There are several HTML closing tags that are unnecessary in HTML, and their presence or lack of presence makes no difference to the client browser, or the HTML validator. As a result, there's no need for them to be in minified HTML, as they are just taking up space. ProCache will remove them for you automatically, which can save a significant amount of bytes in many instances.

These optional closing tags are: `</html>`, `</head>`, `</body>`, `</option>`, `</thead>`, `</tbody>`, `</tfoot>`, and `</tr>`. I'll have to admit, growing up on XHTML 1.0, it came as a surprise to me that many of these tags were considered optional in HTML/HTML5. But removal of them can really help with HTML minification, without affecting anything else.


### Ability to specify which HTML tags are allowed to have whitespace collapsed

By default, ProCache will collapse whitespace around adjacent block-level tags, while leaving a single whitespace before or after inline tags (if present in the original markup). In ProCache 3.1, you can now make adjustments to these rules if you want to, making it collapse whitespace around certain elements it didn't before, or having it retain whitespace around certain elements that it doesn't by default. Though 99% of the time, chances are you won't need to make adjustments to ProCache's default rules, as they are quite consistent and reliable. But it's nice to know you can tweak these things when you want to.


### Screenshot showing Minify configuration screen


### New cache clearing behaviors

Several weeks back, we added new cache clearing behaviors to ProcessWire's core template cache. Specifically, we added the ability to clear pages matching a selector that you specify, and/or clear specific pages you select from a tree.

These new cache clearing behaviors are now available in ProCache too. This is in addition to the existing "clear all", "clear self", "clear homepage", "clear parents", and "clear children" behaviors. These are specified on a per-template basis, just like with the template cache. But since ProCache focuses more on site-wide behaviors, how does it do this? Read on to the next section…


### Configuration per-template and integration with ProcessWire core

When ProCache 3.1 is combined with ProcessWire 2.6.9 (or newer) you gain the ability to configure your ProCache settings directly from the template editor (Setup > Templates) just like you can with the core template cache. The new ProCache option appears in the "Cache" tab, right alongside the template cache option.

Not only can you enable ProCache while editing a template, but you can also specify the new behaviors as described in the previous section, and ProCache will use them.


### Automatic injection of canonical link tags

As you may know, search engines aren't always great at telling exactly what URLs map to truly independent pages in a site. They can sometimes confuse the same single page as separate pages due to slight variations in the URL, such as:

- **Hostname:** www.domain.com vs. domain.com
- **GET vars:** presence of query string vs. non-query string
- **Scheme:** http vs. https
- **Slashes:** trailing vs. non-trailing slashes

Given that, it's worthwhile to be really specific with search engines. One way to do that is by 301 redirecting to the proper URL when the improper one is detected. But that's not always possible or realistic, especially in cache situations where everything is static HTML and there's no PHP logic to analyze the situation. As a result, the more reliable way to solve the issue is often with use of canonical link tags in your document <head>. This is your way of specifying to the search engine what the proper access URL is intended to be.

ProCache 3.1 supports automatic injection of a `<link rel="canonical">` tag into your document head, just by checking a box on the Tweaks tab. Though if one is already present, it won't add another.

While ProCache makes this convenient, you also don't need ProCache to do this. It is as simple as adding the following into your document `<head>`:

```
<link rel="canonical" href="http://www.domain.com<?=$input->url?>">
```

Unlike `$page->url`, the `$input->url` property in ProcessWire includes the current page URL, all URL segments and trailing pagination identifiers, if present. As of ProcessWire 2.6.9 (today's new version) you can also configure your URL segment and pagination trailing slash settings, for even more specificity.

Regardless of whether using ProCache to inject them, or placing in your own canonical link tags, always view the source of pages to double check that they are producing the result you expect. Your definition of what represents a unique URL may be different from `$input->url` (especially in multi-language environments), and getting this wrong can really confuse the search engines, so don't assume it is correct until you confirm it to be so yourself.


### Other helpful details added in ProCache

- All minified/merged CSS/JS files are now outlined for you on the Status tab, including filenames, file size, and date last updated. You can also click to view them.
- The Origin tab (where you select which templates are cached) now is in a table format that shows you the lifetime and behaviors of each cached template.
- New "GZIP + More" tab contains recommended modifications to your .htaccess file and provides helpful resources on testing the performance of your site. Previously this information was under the "Tweaks" tab, but now has its own dedicated tab.


## **ProcessWire t-shirts and more**

Netcarver (who you may know from the ProcessWire forums) has setup a new [online shop](http://pwgeeks.spreadshirt.co.uk/) that sells some really great looking ProcessWire shirts and other merchandise like mousepads, phone cases, winter hats, lanyards, coffee mugs, buttons and more. We recommend you check it out and if you see something you like, buy it and help spread the word about ProcessWire! Thanks to Netcarver for setting this up.

*Hope that you all have a great weekend and week, and remember to read the ProcessWire weekly on Saturday morning. If you are busy on the weekends or might forget, you may want to [subscribe to the ProcessWire weekly](/contact/subscribe/) and we'll send it to you by email during the week.*
