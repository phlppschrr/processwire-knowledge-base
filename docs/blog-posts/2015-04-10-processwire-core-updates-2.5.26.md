# ProcessWire core updates (2.5.26)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.26/

## Sections


## ProcessWire core updates (2.5.26)

10 April 2015 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-core-updates-2.5.26/#comments)

Happy spring break! Here in Atlanta the weather has been great and my family is off school and work this week, so time at the computer has been more limited than usual. As a result, we don't have as many updates for you this time, but there are still a few updates worth mention in this week's new version, 2.5.26:


### Content-type support added to templates

Templates now let you select a content-type that will be used for output. This is useful if you are using a template file for some kind of output other than HTML. When you select a specific content-type for your template, that content type header will be sent to the client browser before the output of the template is sent.

Previously you could do this, but you had to do it with a PHP `header()` call at the top of your template file. This works fine, except when it comes to caching the page with the built-in Page/Template cache, or with ProCache. If cached output was delivered, then there was no way for your `header()` call to get executed.

By selecting a content-type for your template, now you can be assured the proper content-type header will be delivered to the client regardless of whether the output comes from a cache or is generated at runtime. This of course also saves you from having to code header calls in your template file, which not everyone may be familar with, and now you don't have to be.

To define a content-type for your template, go to Setup > Templates > [your-template] > Files [tab], scroll to the bottom, and you'll see the new Content Type field. The default content types include:

- text/html
- text/plain
- application/json
- application/xml

You can easily add your own content types by specifying the following in your /site/config.php file, or in your admin at Setup > Config (if using the [ProcessWireConfig](https://github.com/ryancramerdesign/ProcessWireConfig) module):

```
/**
 * Allowed content types for output by template files
 *
 * When one of these options is selected for a template, the header will be sent
 * automatically regardless of whether request is live or cached.
 *
 * The keys of the array are file extensions. They are used for identification
 * and storage purposes. In ProCache, they are used as a file extension which
 * connects a configured Apache MIME type to the appropriate content type header.
 *
 * @var array
 *
 */
$config->contentTypes = array(
  'html' => 'text/html',
  'txt' => 'text/plain',
  'json' => 'application/json',
  'xml' => 'application/xml',
);
```

Simply add in your own content types in the same manner as those specified above. The array keys represent the file extension defined by an Apache mime-type. The array values represent the content type header that ProcessWire sends before outputting the page.


### ProCache version 2.0.2 released

Consistent with the content-type support described above, a new version of ProCache was released today that adds support for using these content types. This means you can now use ProCache to cache not just HTML, but any kind of content type. This greatly expands the potential of what you can do with ProCache. For example, perhaps you want to cache several XML sitemaps or a JSON feed. This version of ProCache can do it.

It's worth mentioning that ProcessWire's built in Page/Template cache can now do this too, but of course ProCache will always have the speed advantage, being able to deliver static content without PHP or MySQL.


### PageList now supports hover actions

There have been a couple of requests recently for PageList to support hover actions in the default admin theme. What are hover actions? Well "actions" are the "edit", "view", "move", etc., links that appear when you click on a page in the PageList. And the "hover" part means that those actions appear when you hover the page in the PageList, rather than having to click it. Some prefer this because it enables you to perform these actions without triggering the children to load and render. This is applicable to pages with children only, of course. But should it suit your preference, you might find it to be a nice UI optimization.

If you are using AdminThemeReno, then you are already familiar with this, as AdminThemeReno uses them by default. However, the hover actions supported by AdminThemeDefault are implemented a little bit differently, and they provide a few configuration options that you can tweak to your preference. Should you want to experiment with it, add the following code to your /site/config.php file, and make adjustments to the settings as you see fit. Try out the defaults as a good starting point. If using the [ProcessWireConfig](https://github.com/ryancramerdesign/ProcessWireConfig) module, you don't need to edit your /site/config.php as you'll see these options in Setup > Config, and be able to configure them interactively from there.

```
/**
 * PageList default settings
 *
 * Note that 'limit' and 'speed' can also be overridden in the ProcessPageList module settings.
 * The 'useHoverActions' are currently only known compatible with AdminThemeDefault.
 *
 * #property int limit Number of items to show per pagination (default=50)
 * #property int speed Animation speed in ms for opening/closing lists (default=200)
 * #property bool useHoverActions Show page actions when page is hovered? (default=false)
 * #property int hoverActionDelay Delay in ms between hovering a page and showing the actions (default=250)
 * #property int hoverActionFade Time in ms to spend fading in or out the actions (default=150)
 *
 * @var array
 *
 */
$config->pageList = array(
  'limit' => 50,
  'speed' => 200,
  'useHoverActions' => true,
  'hoverActionDelay' => 250,
  'hoverActionFade' => 150
);
```

There have already been requests for yet more options here to configure, so we'll no doubt be adding more in the near future. If you find something you'd like to tweak with this, and the above options don't let you do it, please let us know.


### What else happened this week and what's coming next week

Beyond the updates mentioned above, most of the commits to the core involved fixes and adjustments consistent with issue reports at GitHub. In preparation for ProcessWire 2.6, we're hoping to cover all of them in the coming weeks. So that's what we did this week, and that's what we're most likely going to be working on next week too.

In addition, there are also new versions of FormBuilder and ListerPro just about ready for release, and they may be posted in the relevant boards next week. Work is also continuing on the ProDrafts module, which I hope to start testing on a few installations in May. Hope that you all have a great weekend and thanks for using ProcessWire!
