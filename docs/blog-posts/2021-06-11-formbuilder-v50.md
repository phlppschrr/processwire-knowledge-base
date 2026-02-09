# ProcessWire FormBuilder v50 updates

Source: https://processwire.com/blog/posts/formbuilder-v50/

## Sections


## ProcessWire FormBuilder v50 updates

11 June 2021 by Ryan Cramer [ 0 Comments](/blog/posts/formbuilder-v50/#comments)

Today a new version of FormBuilder has been released in the FormBuilder support board (our 50th version) and it has a lot of interesting new features, which we’ll take a closer look at in this post.

While some of those 50 versions have been unreleased development versions, the first version of [FormBuilder](https://processwire.com/store/form-builder/) began almost 10 years ago. It has changed quite a bit over the years, but it remains focused on its original goals of being a simple, flexible and powerful tool for creating forms in ProcessWire, and to save you lots and lots of time.

Unlike previous major versions of FormBuilder, version 50 doesn't necessarily contain any single major “highlight” new feature. Instead, it focuses on lots of small improvements and features that—when combined—make for a rather major new version of FormBuilder. In fact the scope of changes makes it one of the biggest FormBuilder releases, while remaining familiar to existing users and an easy drop-in replacement for previous versions.


### What’s new in FormBuilder v50


### How to use the new Spam Trigger Words filters

FormBuilder v50 has a new spam filtering option that fills a gap that honeypots and reCAPTCHA cannot. Bot spam is relatively easy to catch, so a significant portion of spam that we see these days is coming from actual people being paid to submit it through web forms. But filters designed for bots cannot catch it because there's a real person at the other side that knows how to follow instructions to complete a captcha or turing test. And because they are a real person using a real web browser, honeypots are also of little help.

A common example of this is the [domain termination scam](https://en.wikipedia.org/wiki/Domain_name_scams) which often comes through website contact form submissions. Someone sends a message pretending to be an invoice saying that your domain is expiring and will be terminated if you don't renew it immediately by clicking some link. And then they presumably steal your domain if you proceed (which we definitely don't want our clients to do). Of course we all know this is spam (and a scam), but a lot of people don't. Because it's a real person submitting it, it tends to get through the spam filters that filter out bots, such as honeypots and captchas.

FormBuilder supports spam filters like [Akismet](https://akismet.com/) (and other services) which can be helpful here, but my experience has been that few want to pay a monthly fee to them for this. FormBuilder v50 adds another alternative: support for spam trigger words. This enables you to configure certain words or phrases that flag a form submission as spam. It's very simple to configure, but also quite powerful when you need it to be. You enter one spam matching rule per line, and you can specify just simple words or phrases to match anywhere in any field. But you can also specify ProcessWire selectors to perform different kinds of matches in different fields. My rules for matching the annoying domain termination spammer are as follows:

- `termination of domain`
- `termination of your domain`
- `hostdomains`
- `email%=domainregistrationcorp`

When you enter just a word or phrase on a line, it presumes you are performing a partial match (%=) on any field in the form. Below are how to use more advanced matching rules with ProcessWire selectors:

**Examples:**

If you omit the field name at the beginning, then it implies all fields.

Be sure to test any filters you add by submitting a form that matches your filter(s). While doing this you may want to set your “What should happen when spam is detected” setting to “Tell the user…”, so that it will be simple for you to identify what does (or doesn't) match your filters.


### FormBuilder processor plugin modules

In addition to Inputfield plugin modules, FormBuilder also supports form processor plugins. The first example of this was the [Stripe Processor module](/blog/posts/stripe-payment-processor-form-builder/) released with an earlier version of FormBuilder. More form processor plugins are on the way as well. I wanted to mention that there's a new “Hello World” processor plugin now posted in the FormBuilder board. This is a ready-to-install module that demonstrates a few different capabilities of form processor plugin modules in a very simple way.

The “Hello World” form processor module serves as an excellent starting point for building your own form processor plugin modules, should you want to. The current version of it lets you configure a hello-world message that displays above your form when you check a box on your form's “Actions” tab. It also adds a button on your entries screen, enabling you to apply an action to user-selected form entries.

Of course, the Hello World action doesn't do anything useful, but the point of it is simply to demonstrate how you can work with form processor actions to achieve something useful and specific to your needs.


### Upgrading to FormBuilder v50

*Before upgrading, please note that (as with all new FormBuilder versions) it is released initially as a beta version and will become the next stable version after a week or two. As a result, please test in a non-production environment before migrating to production, or wait a week or so before installing the upgrade. *

This version of FormBuilder is technically smaller than previous versions, as it drops a lot of legacy framework baggage, no longer including Uikit 2, Bootstrap 4, Foundation 6, Legacy or Admin frameworks. It also drops most of the jQuery UI themes as well, which are rarely used, though we've left these jQuery UI themes: delta, start, basic. Some of you may still be using one of the legacy frameworks, or less likely, one of the jQuery UI themes.

**If you are using one of the legacy CSS frameworks**, grab the FormBuilderFrameworks.zip file posted alongside FormBuilder v50 in the FormBuilder downloads thread. It contains all of those legacy frameworks. See the README.md file in the zip for instructions. Basically, you'll take the framework you need and place it in one of the two locations where FormBuilder can find it: /site/modules/FormBuilder/frameworks/ or /site/templates/FormBuilder/frameworks/.

**If you are dependent upon one of the legacy jQuery UI themes**, double check that that's really the case. Chances are it'll only be the case if you are relying upon a specific color theme for the jQuery UI date picker or for AsmSelect. See if substituting the Delta or Basic theme works just as well (you can select it from the Output tab of your form). If you find you still want one of the legacy themes, download a previous version of FormBuilder (like v46) and replace the /themes/ directory in FormBuilder v50 with the one from FormBuilder v46, or prior. Or, if you want it to survive future upgrades then place it in /site/templates/FormBuilder/themes/ instead.

Beyond the considerations of frameworks and themes, there aren't any other changes in FormBuilder v50 that are likely to require your attention for existing forms. However, like any major upgrade, you should test all of your forms to make sure that everything still works as you expect.


### What FormBuilder and Pro modules do for ProcessWire

FormBuilder has been particularly important in the development of ProcessWire itself. Development of FormBuilder started not long after ProcessWire, it was the first Pro module released for ProcessWire, and it has consistently been one of the most popular Pro modules. Pro modules are what funds development of the ProcessWire core and what enables the community to support development the ProcessWire core. For me it means I'm able to put more time towards ProcessWire and less time towards client work. At the same time, the goal with all Pro modules is that they deliver exceptional value to users (well beyond their cost) and save you significant development time, making them a good investment that aims to save you time and money.

While we are still a relatively small project, we are also one of the most stable, active, secure and reliable open source projects in the CMS landscape, and have been for a long time. The Pro module model has been one that's consistently enabled ProcessWire to grow as a sustainable open source project over nearly a decade now, thanks to your support. While it doesn't bring in enough to hire more people, it does help a whole lot because it enables me to dedicate a major portion of my time towards ProcessWire and its development, and less towards developing stuff for other people (client work). I particularly like this because it means I get to spend more time working with all of you, the most talented community of web professionals in the world.

Thank you for reading and for all of your interest and support. Next week we'll be back to the core for ProcessWire 3.0.180. Be sure to catch the latest ProcessWire news, updates and site of the week in [ProcessWire Weekly](https://weekly.pw).
