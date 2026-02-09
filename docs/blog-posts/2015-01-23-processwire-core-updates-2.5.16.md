# ProcessWire core updates (2.5.16)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.16/

## Sections


## ProcessWire core updates (2.5.16)

23 January 2015 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-core-updates-2.5.16/#comments)

Before we jump into core updates for this week, I just wanted to mention the great new [ProcessWire developer directory](http://directory.processwire.com), built by [Pete](https://www.notanotherdotcom.com). Check it out, and please add yourself to it if you aren't already there.

In addition, we're very excited that this week ProcessWire was awarded [Best Free PHP CMS](http://www.cmscritic.com/2014-critics-choice-award-winner-best-free-php-cms/) in the Critic's Choice awards by CMSCritic! Now for the core updates…


### Blank versus zero

This week we fixed something that a few of you have run into over the years. ProcessWire's number types (like FieldtypeInteger) didn't differentiate between the number 0 and the lack of a value. So if you performed a `$pages->find("some_field=0")` you would get all pages that had the value 0 specified, as well as pages that had no value specified. Essentially a `some_field=0` and `some_field=''` were equivalent queries, and there was no way to differentiate between them.

Very often that's exactly what you want (and it can save you a lot of content input). But there are also cases where it is not what you want at all. For example, consider a score or rating value. A rating of 0 is something very different from "not yet rated". That's just one example of many.

With the dev branch updates put in place this week, you can now differentiate between empty (blank) values versus zero (0) values. It is a configurable option with each number field:

If blank and 0 mean different things, then you can query them separately. For instance, if you wanted to find all pages that had no value present for some_field, you could do a `$pages->find("some_field=")`. Or if you wanted all pages that literally had the value 0 present, then you could do a `$pages->find("some_field=0")`.

Yes, it's a small thing, but it's a good thing that you'll be glad to have when the need strikes.


### Configurable URL segments in template settings

If you have used URL segments in ProcessWire, you may have noticed that when enabled, your page will receive and process any valid URL that starts with your page URL (assuming it isn't a URL already handled by a child page). Meaning, if your page lived at /path/to/page/ and you had URL segments enabled, then it would be loaded for any URL that started with /path/to/page/. For example, hitting any one of these URLs would load the same page:

- /path/to/page/
- /path/to/page/photos/
- /path/to/page/something/
- /path/to/page/hello/world/
- /path/to/page/foo/foo/bar/foo/bar/

Now it may have been that you really only wanted to support /path/to/page/ (no URL segments) and /path/to/page/photos/ (1 URL segment). That left the responsibility on your template file to detect invalid segments and throw a 404 when a URL segment other than 'photos' was present. If your template file isn't fulfilling that responsibility, then you've got potential problems:

- Accepting undefined URL segments means the same page content is accessible at multiple (possibly unlimited) URLs, which may be an SEO problem (potential duplicate content, for starters).
- If caching output like with template cache or ProCache, then accepting undefined URL segments means there are no constraints on the cache. A single page has the potential to create an unlimited quantity of cacheable pages–worst case filling up your hard drive.

So how do you prevent that? You have to differentiate when you've received a valid URL segment string and when you've not. Here's one way we've seen it done:

```
if($input->urlSegment1 == 'photos') {
  // valid! display photo gallery

} else if(strlen($input->urlSegment1)) {
  // invalid! throw 404
  throw new Wire404Exception();

} else {
  // no URL segment: render normal page
}
```

Looks good… but wait, there's a problem here. Can you spot it?

The code above only considers URL segment #1. If it gets a valid segment #1 of "photos" then everything else is fair game. Meaning, /path/to/page/photos/kung/pao/chicken/ is still valid, and the two issues we mentioned above have not been solved at all.

Using the `$input->urlSegmentStr` property makes this easier to solve, because it includes *all* URL segments in a slash-separated string. So if we compare it to the string photos then it would not match photos/kung/pao/chicken.

```
if($input->urlSegmentStr == 'photos') {
  // valid! display photo gallery

} else if(strlen($input->urlSegmentStr)) {
  // invalid! throw 404
  throw new Wire404Exception();

} else {
  // no URL segment: render normal page
}
```

So with the above, we've got something safe and relatively easy. But it is still a pain to have to consider and think about this every time we want to use URL segments. What if we could just define ahead of time what's valid rather than having to code around it? Today's commit to the dev branch lets you do that. Now you can optionally specify what are the valid URL segment strings right in your template settings. If you are so inclined, you can even use regular expressions.

So that we can continue with the same example above, please ignore what's configured in the screenshot and pretend it was just configured to handle the single "photos" URL segment. The URL segment could now be safely handled with just this code:

```
if($input->urlSegmentStr == 'photos') {
  // valid! render photo gallery

} else {
  // no URL segment: render normal page
}
```

Furthermore, with the above example, it doesn't matter if we check `$input->urlSegmentStr` or `$input->urlSegment1`, as both are equally safe in this instance since all URL segments other than "photos" are automatically sent to a 404 before the template file even gets to look at it.


### Set page references from title (string)

You can now populate page reference fields simply by populating a title from one of the possible page references.

```
$page->some_page_field = "Trends and Research";
```

That essentially says "find a page with the title 'Trends and Research' and cross reference it with this field." You can also set multiple values:

```
$page->some_page_field = "
  Trends and Research
  Highlights
  Timely Publications
  ";
```

The above example uses a newline separated string, but you can also use pipes "|" to separate values.

In order to use this, the page reference field (some_page_field) must either have a parent or template specified in its settings.

I'm not suggesting you use this as the ideal way to set Page reference values from the API. But where this comes in handy is when it comes to importing from another source. For instance, maybe you are importing from a spreadsheet, and the only thing you've got to use are titles of categories, companies or the like.

That was exactly the case I ran into this week. So I updated the ImportPagesCSV module to support import of Page fields (to be posted soon), used Adrian's [Batch Child Editor](http://modules.processwire.com/modules/batch-child-editor/) module to create all the possible pages that would be referenced, and then imported my spreadsheet. That made for a very easy import job!


### More system notifications updates

There were a few minor updates to the SystemNotifications module this week:

- Now you can separate the runtime notices from the persistent notifications. If using AdminThemeReno, they even display in different locations. Whether this is desirable to you or not will depend on your use case, but it's nice to have the option. This is configurable in the module settings (see the last option).
- You can now specify what order you want notifications to appear in: newest-to-oldest or oldest-to-newest.
- You can now enable or disable notifications with an on/off switch accessible in the module settings. This enables you to temporarily disable notifications if all the ajax activity is interfering with JS debugging or some other activity, without having to uninstall the module (and thus losing your settings).
- The icons are now configurable with the InputfieldIcon we introduced last week. Speaking of which, the icons in AdminThemeReno are now configurable with that as well.
