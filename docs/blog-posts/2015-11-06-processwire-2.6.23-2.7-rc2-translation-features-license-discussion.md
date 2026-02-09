# ProcessWire 2.6.23 (2.7 rc2), translation features, license discussion

Source: https://processwire.com/blog/posts/processwire-2.6.23-2.7-rc2-translation-features-license-discussion/

## Sections


## ProcessWire 2.6.23 (2.7 rc2), translation features, license discussion

6 November 2015 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-2.6.23-2.7-rc2-translation-features-license-discussion/#comments)


## ProcessWire 2.6.23 (2.7 rc2)

We'd hoped to get ProcessWire 2.7 released for you this week, but a lot of small details came out of the woodwork. None of them showstoppers by any means, but the more things that can be already accounted for in the first release of 2.7, the better. So I took this week to focus on some of the smaller details that would make PW 2.7 even nicer, and we'll aim to get 2.7 out by this time next week if possible.

Since I knew early on in the week that we weren't going to be pushing 2.7 out this week, we also brought in several pending pull requests. See the dev branch [commit log](https://github.com/ryancramerdesign/ProcessWire/commits/dev) for more details about what's been added and changed.


## Upgrades to language translation tools

One of the [pending](https://github.com/ryancramerdesign/ProcessWire/pull/1404) PRs on GitHub was from @justonestep which suggested some tweaks to the language translation tools. While implementing those changes, I worked on further improvements to the language translation tools. You will see some nice upgrades to those tools in this weeks update.


### Easier-to-use file translation interface

As language translators are aware, there's quite a bit of redundant text in ProcessWire's static file translation tool. It identifies all the translatable phrases in a file, but repeats them twice: once in the label and once in the description. This is because we support the ability for a developer to provide additional notes to a translator. When such notes aren't provided, it simply repeats the translation text in both the label and description. This was done in part to ensure that the translator had a version of the text they could copy/paste from, which is handy when using other tools to help out (like Google translate).

After making some upgrades to our base Inputfield class, we can now just show the translatable text once (while copy/paste friendly), and only show the additional notes when they are provided. This makes the interface a lot cleaner and enables you to see a lot more translation inputs on the screen, with less clutter. This one was suggested via the previously linked PR.


### Ability to hide already translated text

You'll now see a checkbox at the top of the file translation interface that enables you to hide all fields that are already translated. This enables you to focus on just the phrases that still need translation.


### Ability to specify “does not need translation”

There are some phrases that are identical between languages and don't need translation. In order to avoid storing redundant data, ProcessWire doesn't store phrases that are identical to the original.

That's a desirable thing, but with one undesirable side effect: the block would still be considered "untranslated". That's not a problem for users of a language pack, but it is an inconvenience for the person doing translation, as certain translation files would always indicate they still had phrases that needed translation.

Now you can specify an equals sign "=" for the translatable text, and that's your way of telling ProcessWire that the text doesn't need translation (i.e. the translation would be identical to the original). In doing this, translators now have the ability to keep track of things more easily and quickly know when their job is done.


### New lang-edit permission for file translators that aren't superusers

Previously ProcessWire's language management and static file translation tools were only available to superusers. This week we added a new optional permission called `lang-edit` that you can use to give other user roles access to the language management and static file translation tools.

To use it, simply install it from Access > Permissions > Add New > "Install predefined optional permissions". Once installed, a user with this permission (in one of their roles) will have the ability to access Setup > Languages and use the static file translation tools. If you want to limit access to only a certain language (or languages) then add and use the [multi-language page edit permissions](/api/user-access/permissions/#multi-language-page-edit-permissions).


## ProcessWire moving to more open license

Some of you may have noticed the ProcessWire 3.x (devns branch) license is different from that of 2.x. We will likely be applying the same license update to the upcoming 2.7 version (or soon after), so wanted to give you a little more information about that, as well as invite any feedback that you may have.


### Why update the license?

We've noticed that most of the non-legacy CMSs in our segment are using more open licenses than we are, and we've been thinking we should become more open as well. As most of you know, ProcessWire is equal parts framework and CMS. Yet when it comes to licensing, it has a license (GNU v2) that works as a CMS, but not so well as a framework. In fact, ProcessWire is having trouble being taken seriously as a framework due to this license.

Most frameworks (like Laravel) use an MIT license. That license gives the developer (you) control over how you license your own work built within the framework. That is a flexibility we generally assume now via interpretation, but really need to make implicit in our license. This ensures we can be taken seriously not just as a CMS, but as a framework too.


### Perception under GPL

We've [stated specifically](/about/license/3rd-party-files/) in many places and at many times that we support license flexibility for anything in your /site/ directory (like templates, modules, etc.). ProcessWire is a system specifically built to execute those resources. That IS the product, and we do not require or even suggest that assets executed by the system must fall under the same license as the core. Yet those who don't understand what ProcessWire is may assume otherwise, and think that ProcessWire is not as open as it really is. This hurts perception of ProcessWire. We'd really like the language of our license to better match what ProcessWire actually is in specific terms, rather than always having to state how we interpret it.


### ProcessWire is not WordPress

It doesn't help matters that the GNU v2 license is from the BBS era rather than the Internet/CMS era, leaving much open to interpretation. ProcessWire is not WordPress, and we need a more open and modern license to improve not only our perception as a framework, but support growth of our audience.


### Considering the MIT license

We'd hoped to adopt the MIT license, which we see as the most open and flexible license available. It's roughly equivalent to the Apache 2.0 or BSD license to the end user, but incredibly short, easy to read, and with better name recognition. If we were purely a framework, that's what we'd use exclusively. But since we're also a CMS, we have other components in our system (like CKEditor) that aren't MIT, and thus we can't offer the product as a whole under that license. Though many of the core framework files already use an MIT license in ProcessWire 3.0. We intend to continue that on a file-by-file basis where it might be useful to others.


### ProcessWire as a product sits between MIT and GPL

By this I mean our heart is with MIT as a license (or Apache or BSD). But as a combined CMS and framework, our product can't be bundled as an MIT exclusive product since it has components that aren't MIT. (The most important being CKEditor). So after a lot of research, we found a license that sits exactly in the position we occupy, and that's the Mozilla Public License version 2.0 ([MPL 2.0](https://www.mozilla.org/en-US/MPL/)).


### Looking at the MPL 2.0

The MPL 2.0 license was created and is maintained by the [Mozilla Foundation](https://www.mozilla.org/en-US/foundation/) and intended as a hybrid between the BSD (or MIT) and GPL licenses. It is compatible with the GPL license. It is approved as a free software license by the Free Software Foundation, and approved as an open-source software license by the Open-Source Initiative.

It specifically defines the type of linkages that we want to support in order to be taken seriously as a framework. And it fully supports our desire to use more open licenses on a file-by-file basis (specifically, the MIT license for many core framework files).

Version 2.0 of the MPL was published in 2012, so it's actually newer than ProcessWire (which was first released as open source in 2010). Meaning, it's a modern license that adequately accounts for today's context rather than one from a quarter century ago. That means there is little ambiguity or things that are open to interpretation since it was envisioned in the same lifetime of our product. It also helps matters that it originated as a license for a browser (Firefox) and as a CMS/CMF that delivers content to a browser, we are part of that same ecosystem. It's the license I would have chosen had it been there in 2010.

The MPL 2 also contains the wording necessary to guarantee you (site, application and module developers) the ability to choose your own licenses for your own work built in ProcessWire. Granted, that's something we already provide to you (at least for what's in /site/), but the MPL 2.0 allows us to do that without ambiguity or interpretation. If someone doesn't know or understand what ProcessWire is, they will be able to find clarity in the license rather than applying their own interpretation.


### What it means to you

In reality? Nothing. The MPL 2.0 is pretty much identical to how we've been interpreting the GPL, but with the benefit of not having to interpret it. Though the MPL does let you apply that interpretation beyond the template files and modules that we've stated ProcessWire is specifically designed to execute under the current license (if that's of use to anyone, it isn't to me).

In "the developer went crazy" terms, the change protects you against me changing my interpretation of the GPL. Lets say that we decided we were now going to interpret the GPL like the WordPress team does… meaning that everything you (as a web developer) create in or for ProcessWire now has to be GPL as well. That would be bad news for you and your clients. Adopting the MPL 2.0 means that you are protected from such a scenario.


### Other points

When I first updated the PW 3.0 license to be a combination of MIT and MPL 2.0, there was the suggestion that it was motivated by the desire to maintain a separate commercial version of ProcessWire. Sorry to disappoint anyone, but there is no plan for a commercial version of ProcessWire, so that has nothing to do with updating the license. As some of you may know, ProcessWire 1.0 was commercial, and ProcessWire 2.0 was released as open source, and the intention is to go even more open. I developed commercial CMSs for more than a decade and they are a dead end.

There are no commercial interests participating in this. It's just me trying to figure out what's best for ProcessWire, our users and our growth as a purely open source project (CMS & framework), and writing here to try and bring you into it. All feedback is welcome.


### Comparing licenses

One of the tools I found helpful in comparing licenses is the site tldr;legal. Here are links outlining the GPL 2 license, as well as others I've considered:

- [GPL 2](https://tldrlegal.com/license/gnu-general-public-license-v2) (our current)
- [MPL 2](https://tldrlegal.com/license/mozilla-public-license-2.0-(mpl-2))
- [MIT](https://tldrlegal.com/license/mit-license)
- [Apache 2.0](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0))
- [LGPL 2.1](https://tldrlegal.com/license/gnu-lesser-general-public-license-v2.1-(lgpl-2.1))


## Heads-up for those with Microsoft-hosted email

We noticed in the last week or so that all Microsoft domains are refusing email from processwire.com. This includes domains like hotmail.com, outlook.com and others. Since the only email actually being sent from processwire.com comes from the forums, we're guessing that someone flagged forum notification emails as spam, rather than correcting their notification preferences. The result is that the forums can no longer send you any email if you use a Microsoft hosted email address. This includes notifications of replies to your topics, PMs, invoices, etc. Further, if you forget your password, you won't be able to reset it if we can't email you.

For this reason, if you are using any Microsoft hosted domain for your ProcessWire forum account, we recommend that you change your email address in your forum account profile to one that is not hosted by Microsoft. Hopefully they will correct this soon, but it's now been going on for more than a week.

This affects the email sent by IP.Board, but not any email sent from the copies of ProcessWire running at processwire.com. For instance, the ProcessWire Weekly email we distribute from here is sent by ProcessWire using a WireMail module with Mandrill, and we're not having any issues delivering to Microsoft email addresses there. Speaking of [ProcessWire Weekly](http://weekly.pw), be sure to check in there tomorrow for the latest edition!
