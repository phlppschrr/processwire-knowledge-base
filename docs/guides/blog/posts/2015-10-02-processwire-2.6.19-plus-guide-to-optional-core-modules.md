# ProcessWire 2.6.19 plus guide to optional core modules

Source: https://processwire.com/blog/posts/processwire-2.6.19-plus-guide-to-optional-core-modules/

## Sections


## ProcessWire 2.6.19 plus guide to optional core modules

2 October 2015 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-2.6.19-plus-guide-to-optional-core-modules/#comments)


## ProcessWire 2.6.19

Usually our blog posts focus on what's new in the ProcessWire dev branch. Like last week, there was a LOT of activity on the dev branch this week. But that activity was focused on fixes, tweaks and mostly not stuff you want to read a blog post about. Though we do have a few things to say about that, but not enough to fill an entire blog post. That's likely to continue for the next couple of weeks as we work towards 2.7.

The main content of our posts here over the next couple weeks will instead focus on other subjects, like best practices, introducing more coverage of things we already have, and guest posts. Note that much of this week's post and last week's post will eventually be migrated to new documentation sections in this site.

This week we are focused on covering all the optional modules included with the core that are not installed by default. Many have not been covered in much detail before, and should be. So that is our feature of the week, hope that you enjoy!


### On the path to ProcessWire 2.7 with dev 2.6.19

This week we continued working towards ProcessWire 2.7 by focusing exclusively on GitHub issue reports and pending pull requests. At the time of writing this (at least this minute) we are now up-to-date with GitHub issues and this week's version 2.6.19 contains a ton of small tweaks and fixes. See the [dev branch commit log](https://github.com/ryancramerdesign/ProcessWire/commits/dev) for full details.

Thus far there have been no major bugs reported in the 2.6 dev branch so the focus has been primarily on the smaller details, fixes and optimizations that you'll see in the commit log. This is good news, as it means our dev branch is stepping closer and closer to PW 2.7. A huge thanks to all that have been reporting issues and testing on the ProcessWire dev branch. ProcessWire 2.7 is going to be incredibly optimized and stable thanks to all of your help.

There were no new features added this week, and that's intentional and good. We are now in a soft feature freeze for 2.7, meaning we're trying not to introduce new code that needs significant testing at this point. That's not to say there won't be any new things added to the dev branch before 2.7 final, but that we're going to be very shy and cautious about adding new stuff at this point to ensure an October release date for PW 2.7.


## A guide to optional (uninstalled) core modules

ProcessWire comes with many modules as part of the core that are not installed by default. Yet many don't know they are there, or don't know what they are for. In this article, we'll cover all of them in more detail. You may find a few modules that you want to install and use!


## Admin

The Admin category of modules currently focuses on Admin Theme modules which control the look and feel of your admin UI. ProcessWire core comes with AdminThemeDefault and AdminThemeReno. The AdminThemeDefault is installed already, but AdminThemeReno might not be. Read on to learn more about AdminThemeReno.


### Reno (AdminThemeReno)

This is the great Reno admin theme designed by [Tom Reno](https://twitter.com/renobird) (aka [renobird](/talk/user/474-renobird/) in the forums). This admin theme takes a different approach to the interface than the default admin theme, and is preferred by many ProcessWire users. Once installed, every users' profile screen includes an Admin Theme selection, enabling them switch to the Reno admin theme.

After installing the Reno admin theme, be sure to review the settings on the module configuration screen, as there are a lot of options you can configure. You may want to connect the Reno admin theme with a user profile image, which is something quite nice that the default admin theme does not support. Be sure to click "submit" to save the module settings, even if you didn't change anything, as this commits all the default settings.

Reno admin theme tips:

- Double click the "Pages" navigation as a shortcut to the page tree.
- Use the left and right arrows on your keyboard to open or close the sidebar.
- Hover the lightning-bolt icon that accompanies any navigation item to reveal a flyout of additional options.
- The Reno admin theme has better support for mobile and touch devices than the default admin theme.
- Listen to Tom Reno's band [The Mercury Program](https://www.facebook.com/themercuryprogram) (especially when using the Reno admin theme).


## Fieldtype

Fieldtype modules are literally "field types". They represent different types of content fields in ProcessWire and provide the schema, logic and methods for managing data for each type. Fieldtype modules are what enable ProcessWire to manage and support any kind of content. The core includes a few Fieldtype modules that are not installed by default and we cover these below. Like all modules, you can also create your own Fieldtype modules or install 3rd party ones.


### Cache (FieldtypeCache)

Few know about this Fieldtype that has been in the core since the beginning. This Fieldtype enables you to combine the values from any number of other fields into one single, searchable text field. This is primarily beneficial for creating search engines that need to quickly search the contents of numerous fields at once (like a site text-search engine). If you find yourself creating long page finding selectors like…

```php
$pages->find("title|body|sidebar|summary|intro|keywords%=something");
```

…consider bundling all those fields into a single "cache" field. Then you can search it faster and more efficiently like this:

```php
$pages->find("your_cache_field%=something");
```

The cost is of course storage space, and duplication of content in the database (it's a cache after all). But these days storage space is a lot cheaper than CPU cycles and your users' time, so FieldtypeCache may be just the right fit for some cases.


### Comments (FieldtypeComments)

This is the primary module behind ProcessWire's built-in comments system. Installing it will enable you to create one or more comments fields. It will also install an Inputfield (InputfieldCommentsAdmin) for managing comments as a field on your page. For more about creating comments fields and using the comments Fieldtype, please see the [comments documentation](/api/fieldtypes/comments/).


### Select Options (FieldtypeOptions)

A relatively recent addition, the Select Options Fieldtype enables you to create selectable options using single and multiple select boxes, checkboxes, radio buttons, AsmSelect and more, without using Page references.

In ProcessWire, these types of inputs are usually connected to pages selections (using the Page fieldtype). The Select Options Fieldtype provides an alternative to that approach, enabling you to manually configure your selectable options without using pages to hold the selectable values. The Select Options Fieldtype supports the ability to specify your options in multiple languages, separate name, value and label attributes, default values, and more.

While using the Page Fieldtype generally gives you more long-term flexibility, the Select Options Fieldtype can be quicker to setup, and is quite flexible in its own right. Read more in the [Select Options Fieldtype documentation](/api/modules/select-options-fieldtype/).


### Page Table (FieldtypePageTable)

The Page Table Fieldtype is an alternative to the Repeater Fieldtype, enabling you to create repeating elements that contain their own fields. It's called Page Table because the elements are themselves pages, and they are presented to you in a customizable Table in your page editor. Clicking a row in the table opens a modal window enabling you to edit all the fields for that item. The editable fields may go beyond those shown in your table row. The rows in the Page Table are also drag-n-drop sortable.

Page Table has a few benefits over Repeater:

- It scales better in the admin interface because you only edit one row at a time (rather than all at once). If you need a lot of editable rows, Page Table will handle it more quickly and efficiently than Repeater.
- It lets you support table rows that use different templates. It's a good solution for creating a flexible content model where you might need to create rows with different types of content and fields.
- It gives you more control over where the resulting pages will live.
- It can support more complex Inputfields that may not work in Repeaters.
- There is no need for pre-rendered "ready items" like in Repeater, as Page Table items are edited in their own modal window.

PageTable also has a couple drawbacks relative to Repeater:

- Repeaters are generally faster to setup and get going, because Repeater manage all the details of where the individual page items will live. You can create and use a Repeater more quickly than a PageTable.
- For small lists of items that contain few fields, Repeaters may be more editor friendly. All items can be edited directly in the page edit screen without separate modal windows.

Interesting facts about Page Table:

- Page Table was envisioned and sponsored by [Avoine](http://www.avoine.fi/).
- Page Table was developed alongside the [ProFields](/api/modules/profields/) package, and thus historically carries the ProFields prefix even though it is free and in the core.


### Repeater (FieldtypeRepeater)

Repeaters enable you to define a content type consisting of a group of fields, and make it repeatable. For instance, you might create a homepage slider that consists of a headline, background image, summary text and link URL. Add the repeater field to your homepage, and then you can maintain any number of slides, each containing that group of fields.

Behind the scenes, repeaters are actually creating pages for each of your repeatable items. Though it's not apparent because those items are hidden deep in the page tree within the admin. This makes them particularly easy to configure and use. ProcessWire also provides the Page Table Fieldtype which has some benefits and drawbacks relative to Repeater. Be sure to read the section above on Page Table if you haven't already.


### Text Language (FieldtypeTextLanguage)

*Also includes FieldtypeTextareaLanguage and FieldtypePageTitleLanguage.* These are multi-language versions of the Text, Textarea and PageTitle fields. They are installed by the LanguageSupportFields module. When using multi-language support, you can selectively convert the type of your "title" field, and any other text fields to these multi-language Fieldtypes. They work exactly the same as the non-multi language versions except that they support their text values in each language. When using multi-language text fields, we recommend also installing the core LanguageSupportTabs module, also discussed in this article.


### Selector (FieldtypeSelector)

The Selector Fieldtype is a very powerful page selection field. It collaborates with the Selector Inputfield module to enable you to select pages using your own custom criteria. For an example, go to Pages > Find in your admin, and look at the "Filters" fieldset – that is an example of a Selector field. Now imagine having something like those Filters as a means for selecting pages to store in a field as content, and you've got the Selector Fieldtype.


## Inputfield

Inputfield modules provide the markup and methodology for collecting and processing input from a user. Inputfield modules commonly accompany Fieldtype modules, as they collect, validate and prepare input that will be handled off to a Fieldtype for storage. Most Inputfield modules can also be used on their own, without a Fieldtype. For example, all of forms in ProcessWire's admin are powered by forms built from Inputfield modules. In addition, tools like FormBuilder use Inputfield modules to render and process forms.

Most of ProcessWire's core Inputfield modules are already installed, ready for you to use. But here are a couple that are not installed by default:


### Page Auto Complete (InputfieldPageAutocomplete)

This module collaborates with the FieldtypePage module to enable selection of pages via autocompletion rather than pre-loaded page selection (checkboxes, radios, select boxes and such). This has significant benefits over other page selection methods when it comes to dealing with large groups of potential pages. It wouldn't be feasible to have thousands of checkboxes, whereas it's perfectly feasible to make thousands of pages available for selection when using autocompletion. This module is highly recommended for any input scenario dealing with large numbers of selectable pages/options.

The Page Auto Complete module supports both single and multiple page selection. When used for multiple page selection, it also supports the ability for the options to be sortable.


### Comments Admin (InputfieldCommentsAdmin)

This Inputfield module accompanies the FieldtypeComments module to provide management of comments attached to a page. With this module you can edit existing comments, change their status (approve, spam, delete), change authorship information, and manage parent/child relationships of comments. This module will be installed automatically when using FieldtypeComments, so there is nothing you have to do to install this module.


## Language

Language modules provide the basis of ProcessWire's multiple language support. They are not installed by default since not all sites need multi-language support. But if you do need multi-language support, you will likely want to install all of them. Also be sure to see our [multi-language documentation](../../docs/multi-language-support.md). Please thank [Avoine](http://www.avoine.fi) for sponsoring multi-language support in ProcessWire.


### Language Support (LanguageSupport)

This module provides the basis for language support in ProcessWire. You will want to install this if you intend to develop a multi-language site or application. We also recommend installing all the other "Language" modules that accompany it, described below.


### Language Fields (LanguageSupportFields)

This module provides support for multi-language fields and multi-language alternate fields. See the [documentation for multi-language fields](../../docs/multi-language-support/multi-language-fields.md). The LanguageSupportFields module also installs the 3 core multi-language text types: FieldtypeTextLanguage, FieldtypeTextareaLanguage, and FieldtypePageTitleLanguage.


### Language Page Names (LanguageSupportPageNames)

If your multi-language strategy involves use of multi-language fields, chances are you'll also want your pages to themselves be multi-language. This implies having a single page that can be accessed at different URLs specific to each language. When accessed at the URL for a particular language, the system will output all multi-language fields in that language. For more about multi-language page names, please see the [multi-language URLs documentation](../../docs/multi-language-support/multi-language-urls.md).


### Language Field Tabs (LanguageSupportTabs)

By default, multi-language fields display as a vertical stack of inputs separated by language. Installing this module will instead make them display in a tabbed interface, which is preferred by most. Though the stacked layout is better for translating from one language to another because you can see both languages at the same time. As a result, this module also supports the ability to switch between tabbed and stacked layout for any field, at any time. The icon toggle appears in the top right corner of each field in the page editor. This module was originally envisioned by [@adamspruijt](/talk/user/778-adamspruijt/).


## Markup

Markup modules are focused purely on generating or managing markup. Most can be thought of as helpers for you and your development needs.


### Cache (MarkupCache)

The MarkupCache module provides an easy-to-use API for caching rendered markup from your template files. This module has since been replaced by the [$cache API variable](/blog/posts/processwire-core-updates-2.5.28/#wirecache-upgrades), but the MarkupCache remains in the core for backwards compatibility. In addition, it uses a different storage method for the cache (files rather than database) which is preferred by some.

For more about MarkupCache see this post [introducing MarkupCache](/talk/topic/7-new-markupcache-module/) and the [ProcessWire Caching Explained](http://www.flamingruby.com/blog/processwire-caching-explained/) article by Teppo Koivula.


### Page Fields (MarkupPageFields)

This module adds `$page->renderFields()` and `$page->images->render()` methods that return basic markup representing the field values. This is particularly useful for quick prototyping, testing and debugging.


### RSS Feed (MarkupRSS)

Given a list of pages (PageArray) this module will take those pages and render an RSS feed from them. This module is typically called from the API side by one of your template files designed for outputting RSS feeds. For more about MarkupRSS, see the [MarkupRSS module page](http://modules.processwire.com/modules/markup-rss/). While there, you might also want to check out the [enhanced fork](http://modules.processwire.com/modules/markup-rssenhanced/) of this module by Martijn Geerts.


## Page

Page modules are modules that provide additional functionality or assistance to Page objects.


### Path History (PagePathHistory)

This module keeps track of past URLs where pages have lived and automatically redirects (301 permanent) to the new location whenever the past URL is accessed. This is a good module to install if you regularly rename or move pages in your site. It ensures that visitors always get to the right place, even if it was from a previous URL. Note however that this module does not support multi-language URLs.


### Paths (PagePaths)

When installed, this module creates a cache of all page URLs and keeps them in the database. This enables page paths (path and/or url fields) to be partial-match queried from selectors in `$pages->find("url%=foo/bar")` operations, and the like. Without this module installed, you cannot query partial matches from page url or path properties because the information simply doesn't exist in the database. That's because ProcessWire stores a name for each page, along with reference to a parent page, rather than the entire URL. So if you've had a need perform searches on pages from the URL/path, this module is what you want.

The PagePaths module also has potential to improve the performance of ProcessWire's page loading of individual URLs. Without this module installed, ProcessWire determines which page matches a requested URL by joining each segment of the URL with an equivalent SQL join. Installation of this module enables it to bypass those joins. In real-world usage, this probably doesn't make a significant difference, so don't install it just for this reason. But consider this an extra bonus if you installed it for the reasons mentioned in the previous paragraph. Note however that in a multi-language site, this module only maintains paths of the default language. As a result, there may be little reason to install this module in a multi-language site.


## Process

Process modules represent applications in the ProcessWire admin interface. In fact, the entire admin is built around Process modules. For instance, when you are viewing a Page List, that is managed by the ProcessPageList module. Likewise, when you are editing a page, that is managed by the ProcessPageEdit module. All functionality in the admin is handled by individual applications developed as Process modules. Because they are modules (plugins) you can expand the scope of what your admin does, simply by installing Process modules. There are also many 3rd party Process modules available as well. Below are a few that come with ProcessWire but aren't installed by default.


### Comments Manager (ProcessCommentsManager)

This module is highly recommended if you are using ProcessWire's comments field (FieldtypeComments). It provides a separate management interface for comments outside of the page editor. This interface enable you to manage comments for the entire site at once, isolated by approved, pending and spam comments. For instance, if you wanted to see all comments awaiting moderation approval in your site, you would click the "pending" tab, and be able to manage them all as a group.


### Forgot Password (ProcessForgotPassword)

This module enables a "forgot password" function for your admin login form. If you or your users are prone to forgetting their password, this module is exactly what you want. It sends an email, but also tracks the users session to maintain security when resetting their password.

This module is more secure than most reset-password functions we've come across. But the fact remains that password reset functions always invite unwanted attention, so we've left this module uninstalled by default so that only those that need it will install it.


### Languages (ProcessLanguages)

This module is installed by the LanguageSupport module and provide the admin tools for managing languages. When installed, you'll see it at Setup > Languages.


### Language Translator (ProcessLanguageTranslator)

This module is installed by the LanguageSupport module and provide the admin tools for creating and managing [translations of static text](../../docs/multi-language-support/code-i18n.md) in your PHP files. It is also used to create, upload and manage [ProcessWire language packs](http://modules.processwire.com/categories/language-pack/).


### Page Clone (ProcessPageClone)

As you might guess, this module adds a page cloning capability. This is perhaps one of the most common core modules to install, and perhaps we should have it pre-installed in the future. Once installed, you will see a "clone" option in your pages list, after clicking the arrow to reveal extra actions. This module also installs two permissions: *page-clone* and *page-clone-tree*, which you can assign to user roles that you want to have clone capability.


### Sessions (ProcessSessionDB)

This module accompanies the Session Handler Database module and provides an admin tool that enables you to view all active sessions on your site. We recommend installing this module if you are using database-driven sessions. The ability to see these sessions in action is not only fun and interesting, but enables you to get a gauge on site traffic, including that from crawlers and robots.


## Session

Session modules help to manage ProcessWire sessions. By installing a Session Handler module, you can change the way that ProcessWire stores and manages sessions.


### Session Handler Database

This module changes the way that sessions are stored in ProcessWire. By default, sessions are stored on the file system using PHP's default session handler. When this module is installed, it instead puts ProcessWire in control of the session data and stores it in the database. There may be some performance benefits to session storage in the database, though we've not observed much practical difference. Perhaps one of the greatest reasons to install this module is to take advantage of the benefits provided by the ProcessSessionDB module, mentioned above. In some environments, there may also be security benefits to using the database rather than PHP's default file-based sessions.

Note that after installing this module, the session storage will have changed and thus you and any other users will be immediately logged out and begin a new session. Simply log back in again and all will be good in the world.


## System

System modules help with managing, maintaining and updating the core and system behaviors, or modifying the behavior of default system behaviors.


### Notifications (SystemNotifications)

The SystemNotifications module changes and expands the behavior and capabilities of notifications in ProcessWire. This module was envisioned and sponsored by [Avoine](http://www.avoine.fi). Some benefits of using this module include:

- Notifications appear as "ghosts" that fade in and out at the top of the screen, while you can click a "bug" at the top with a number in it to reveal the full notifications. You can open or close the notifications bar with the "bug" whenever you want.
- Notifications may be stored with the user account, which enables persistent notifications (ones that appears until you dismiss them), and means that you can have notifications queued to you even when you aren't logged in.
- You can receive notifications at any time, even while you are in the middle of something else. Notifications are polled and delivered via ajax at set intervals, which makes them independent of the usual notifications you may be used to seeing after submitting a form.
- You will get a notification if you are attempting to edit a page that another user is already editing.
- You can receive instant notifications on system events like user logins and more.
- The appearance and behavior of notifications is configurable in the module settings.

That's just for starters, here's [more details about SystemNotifications](/blog/posts/processwire-2.5.3-master-2.5.4-dev/#whats-new-on-the-dev-branch).

There is also a reason why SystemNotifications isn't installed by default. It uses significantly more resources than normal notifications. Every logged-in account pings the server for new notifications every 5 seconds (or whatever interval you've defined). This also has the behavior of keeping you logged in indefinitely while you've got your PW admin window open (which may be a plus or minus).


## Textformatter

Textformatter modules can be applied to text fields in ProcessWire (and others). They modify the output of fields when the output formatting state of a page is enabled (as it is by default on the front-end of your site). A common example is the need to entity encode text that will be output in HTML markup, which is what the core Entity Encoder Textformatter module does (which is also the most commonly used Textformatter module). There are also numerous 3rd party [Textformatter modules](http://modules.processwire.com/categories/textformatter/) available like [Video Embed](http://modules.processwire.com/modules/textformatter-video-embed/) and [Hanna Code](http://modules.processwire.com/modules/process-hanna-code/).

You can select what Textformatter modules are applied to any given text field by editing the text field (Setup > Fields) and clicking gone the Details tab. From there you are giving a field where you can select what Textformatter modules are applied to the field. You can also control the order in which they are applied, which is important for some combinations of Textformatter modules.


### Markdown/Parsedown Extra (TextformatterMarkdownExtra)

This module enables you to output text formatted with Markdown (or Markdown Extra) formatting to any text field. It can be used as an alternative to the HTML Entity Encoder Textformatter module when used with trusted users.


### Newlines to line breaks (TextformatterNewlineBR)

This module simply converts newlines in a text field to `<br />` tags at output time. It is typically applied after the Entity Encode Textformatter.


### Newlines to unordered list (TextformatterNewlineUL)

This module converts newlines in a text field to a `<ul>` list, where each line represents an `<li>`. Very handy for feature lists and the like, without resorting to a full rich text editor field. It is typically applied after the Entity Encode Textformatter.


### Paragraph stripper (TextformatterPstripper)

This text formatter module is often combined with the Markdown one. It strips the paragraph `<p>` tags added by markdown, enabling you to use markdown within existing block-level or inline HTML elements. For instance, if you were using the Markdown text formatter module on a "title" field, and outputting that title field in an `<h1>` tag, you want the inline markdown like `**bold**` and `*emphasis*` (and more), but you don't want it wrapping your text in a `<p>paragraph</p>` because that would be inappropriate in an `<h1>`. When you set the paragraph stripper text formatter to run after Markdown, it gives you this result (Markdown-to-HTML without surrounding paragraph tag). Consider this Textformatter for any single-line text fields where you may already be formatting with Markdown, Textile or some other lightweight markup language, and make it run as the last Textformatter.


### Smartypants Typographer (TextformatterSmartypants)

This text formatter provides several typographic conversions:

- Straight quotes ( " and ' ) into “curly” quote HTML entities
- Backticks-style quotes (``like this'') into “curly” quote HTML entities
- Dashes (“--” and “---”) into en- and em-dash entities
- Three consecutive dots (“...”) into an ellipsis entity

Source: [SmartyPants at Daring Fireball](https://daringfireball.net/projects/smartypants/). It also supports [these additions](https://michelf.ca/projects/php-smartypants/typographer/) from Michel Fortin.


### Strip Markup Tags (TextformatterStripTags)

This text formatter strips any HTML out of the text at runtime. This is useful for something like a browser title, meta description or other instances where you don't want any HTML in the text. Some users are prone to entering HTML tags like `<b>I want bold</b>`, perhaps due to past experience with other systems, and you don't want them doing that. When using this Textformatter, we recommend applying it before the Entity Encode or Markdown Textformatters.


## Miscellaneous


### Akismet (CommentFilterAkismet)

If you are using ProcessWire's comments module (FieldtypeComments) this module enables you to connect it with the Akismet comment filtering service. This service is highly effective in reducing or eliminating spam from your comments. We use it here on processwire.com too.


### Lazy Cron (LazyCron)

This module provides hooks that are automatically executed at various intervals. It is called "lazy" because it's triggered by a page view, so the interval is guaranteed to be at least the time requested, rather than exactly the time requested. This is fine for most cases, but you can make it not lazy by connecting this to a real CRON job. See the [Lazy Cron documentation](/api/modules/lazy-cron/) for more details.

Install the LazyCron module if you want to make use of its API hooks. Or more likely, install the LazyCron module if you have another module that indicates it requires LazyCron.

That's all for this week! Hope to see you at the [ProcessWire Weekly](http://weekly.pw) this weekend.
