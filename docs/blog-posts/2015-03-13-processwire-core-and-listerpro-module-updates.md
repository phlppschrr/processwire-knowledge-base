# ProcessWire core and ListerPro module updates

Source: https://processwire.com/blog/posts/processwire-core-and-listerpro-module-updates/

## Sections


## ProcessWire core and ListerPro module updates

13 March 2015 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-core-and-listerpro-module-updates/#comments)


### Responsive tables in the admin

When working in the admin, you are likely to work with tables quite a lot. Several core modules (and many 3rd party modules) use tables for output of tabular lists. They are especially prevalent in Process modules. Examples include Lister, Modules (admin), Templates (admin), Fields (admin), Logs, and so on. In fact, *most* Process modules use tables somewhere or another. You’ll also see tables used in some Inputfields, like InputfieldPageTable, among others. All of these modules output tables using another module called MarkupAdminDataTable. Using that module makes it easy to generate and output tables in a consistent manner.

So we've got a lot of tables… The problem is that tables don’t adapt very well to small screens. One of our goals for ProcessWire 2.6 is to have the admin be very mobile friendly (whether using AdminThemeDefault or AdminThemeReno), which you've already seen many updates for in recent weeks. But even now, when you’ve tried to access the ProcessWire admin on a mobile device and come across one of these tables, you might have noticed that it wasn’t very attractive, as it was clearly not fitting the screen (even if the rest of the interface did).

This week we solved that problem by making MarkupAdminDataTable tables responsive and mobile friendly. Now when viewing on a small screen (or making your window small on a large screen), the table columns stack, and each row gets its own header. This makes these tables just as easy to use and interact with as they are on desktop sizes. Hopefully next time you (or your client) have to administer something in ProcessWire from a mobile device, you’ll find the experience every bit as good as you do on the desktop.


### Create databases at install time

We’ve got several pull requests pending, and are planning to increase momentum on integrating some of them over the coming weeks. One that we pulled in this week was [submitted by @plauclair](https://github.com/ryancramerdesign/ProcessWire/pull/950), which suggested making it possible to create databases from the ProcessWire installer.

Previously you had to create the database separately before installing ProcessWire, using a tool like the mysql client, cPanel and/or PhpMyAdmin. In fact, this is the same thing you have to do for the vast majority of CMS installers out there. It makes sense because most of the time [in production hosting environments], the user account doesn’t have permissions to create databases.

But a lot of us are working with ProcessWire in our own development environments quite a lot too. In this environment (and perhaps others) there’s really no need for the extra step of creating the database. ProcessWire is all about saving you time, so I thought this PR that updated the installer to create the database for you was a nice touch (thanks to @plauclair).

It works like this: when you specify the database information, if the database you specify doesn’t already exist, it will attempt to create it for you. Nice and simple. In my case, it’s already saved me time and hassle as I probably install at least one copy of ProcessWire a day.


### New ListerPro version 1.0.2

This week a new update was released for [ListerPro](/talk/store/product/14-listerpro-dev/). This update adds several features that have been requested by users since the initial release. Because the ListerPro version tends to track closely to the Lister version (in the ProcessWirw core) this new version of ListerPro requires the latest version of the ProcessWire dev branch. ListerPro users can download the update now in the ListerPro support board. Here’s a partial summary of what’s been added and updated:

- Add Lister management controls (list, add, clone, delete) to the ListerPro module configuration screen.
- Add new "Advanced" config options for dictating the visibility and behavior of sections: Filters, Columns, Actions.
- Add config option under "Advanced" to make it easier to specify whether field names or labels should be shown for Filters/Columns.
- Add support for responsive Lister table output (per addition in PW core).
- Add support for modal "add new" pages. This simply inherits from your edit page setting for modals.
- Plus numerous bug fixes and other optimizations.


### New magic trick: the disappearing module

There have recently been [reports](https://github.com/ryancramerdesign/ProcessWire/issues/1011) from some users about certain modules in ProcessWire randomly disappearing. In particular, the LanguageTabs and AdminThemeReno modules. But it's actually not a magic trick, it's a mystery. Usually it would be easy to track down and fix something like this, except that I wasn’t able to reproduce the issue despite many attempts. While it wasn't causing anything urgent or fatal, it was clear there was an issue, because the reports were not isolated.

I should know better than to do this, but I ended up spending about 25% of my working hours this week trying to fix an issue I couldn’t reproduce.* The result was that I couldn’t fix it, despite thinking I might have on more than one occasion. Then late last night Antti Peisa emailed me an exported site profile out of the blue ([using the site profile exporter module](https://github.com/ryancramerdesign/ProcessExportProfile/tree/master)), where he was actively seeing the issue. Luckily I was able to reproduce it immediately upon installation this morning, and it took about 5 minutes at that point to fix it (and just one line of code).

Hopefully the issue is now fixed. But I'm mentioning it here because I’d like to make sure that it really is fixed. If you have experienced this magic trick (err… mystery) recently, please upgrade to the latest version of the dev branch, click Modules > Refresh, and let us know if it resolved the issue or if you continue to experience it.

*Helpful tip: don't try to fix something until you can observe and reproduce it. :)


### Now you can temporarily disable (rather than uninstall) autoload modules

*With a few caveats…*

There have been requests recently for the option to disable modules rather than just uninstall them. Why would you want to do that? The answer is that any configuration settings you had applied to the module could remain present, rather than being lost when the module is uninstalled. Likewise, any pages, fields or other assets created by the module could remain in place while the module's behavior would be disabled. This is particularly helpful for module developers or testing things out for sites in development.

It seemed like a good idea. But as I started looking closer, it became clear that there probably wasn’t any need for this capability except for “autoload” modules (meaning, modules that automatically load at boot time). An installed module that isn’t “autoload” generally behaves the same as an uninstalled module, so there’s not really a benefit to disable other module types, that I can think of.

I went ahead and added the ability to disable autoload modules, so you’ll see that in this week’s dev branch. But it turns out to be a little bit of a dangerous feature if the module happens to be collaborating with any others (like LanguageSupport modules as an example). The worst case is that it could break your site to the point where you can’t undo it interactively… modules that always talk to each other don't like it when their friend takes a nap. As a result, I recommend being careful with it and avoid using it on modules that have other modules using it as a dependency. To keep things safe, I went ahead and hid the option behind debug AND advanced mode, so you have to have both of those modes enabled in your /site/config.php before it’ll give you the option. When they are enabled, you’ll see a checkbox on any autoload module edit screen that lets you disable the module.


### What’s coming next

At this point we’ve got a great feature set for ProcessWire 2.6 and need to start focusing on getting 2.6 out as the new master version. As a result, we are already starting to limit new additions to the core while we focus primarily on testing and resolving issue reports, and ensuring everything is as stable and solid as possible. (Though I believe the dev branch is already just as stable as current master, if not more so).

Most core additions for the next couple of weeks are likely to be based on existing pull requests already in the queue. As a result, there may not be as many surprises as there have been the last few months, but there is a lot of good stuff on the way, so stay tuned! We hope to have an official 2.6 version to you in May, or sooner if possible. But of course if you are tracking the dev branch, you'll have a new version of ProcessWire just about every single week.
