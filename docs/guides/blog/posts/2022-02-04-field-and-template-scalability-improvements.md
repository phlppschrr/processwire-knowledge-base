# Field and template performance/scalability improvements

Source: https://processwire.com/blog/posts/field-and-template-scalability-improvements/

## Sections


## Field and template performance/scalability improvements

4 February 2022 by Ryan Cramer [ 3 Comments](/blog/posts/field-and-template-scalability-improvements/#comments)

This week we have some great performance and scalability improvements in the core that enable lazy-loading of fields, templates and fieldgroups.


### Introduction

The idea and proof of concept for this came from Michael Spooner ([@thetuningspoon](https://github.com/thetuningspoon)). I was so impressed with the performance improvement that I thought it belonged in the core.

Michael had one or more ProcessWire installations that were experiencing some lag due to the quantity of fields and/or templates (in the hundreds). He was getting a boot time upwards of 500ms, which is in the range where you'd feel it, making it feel slow. He experimented with WireCache and memcached for the field/template/fieldgroup data, but found that it didn't help. He narrowed in and identified the bottleneck to be the actual creation of the objects that represent fields, templates and fieldgroups.

The approach he came up with is kind of similar to how ProcessWire loads modules in that it doesn't create the actual Field, Template or Fieldgroup objects until something asks for them. It is a type of lazy load pattern, and it's a great idea in this context because it's rare that an individual request would need all of the templates and fields.

I worked with his ideas and code and adapted and integrated it into the core. I found that there are a few instances where the core loads all the fields and templates. For instance, if you have Repeaters or LanguageSupport installed, both of those iterate all of the fields during boot, which limited the benefits of lazy loading. So those parts were re-coded to be lazy-load friendly. There may still be more to cover, but I think the biggest culprits are taken care of.

What we've ended up with is [quite a large commit](https://github.com/processwire/processwire/commit/a5c70a4e7d14caac7e9e444be85590da8710828e) (16 changed files, 1129 additions) with changes to the lowest level core classes and a few modules, and a great collaborative effort.

You won't notice the lazy loading aspect much until you get a lot of fields or templates. That's because ProcessWire is already quite fast at loading these things, even when it has to load them all. But even if you don't feel the difference, the boot process is still faster, even on small installations. And those little improvements can add up to large improvements when multiplied over hundreds or thousands of requests.


### Large scale performance improvements

To test the difference at scale, I installed a blank copy of ProcessWire and automated the creation of 1000 fields, 1000 templates and 1000 fieldgroups, and randomly assigned fields to the templates/fieldgroups. Using last week's dev branch (prior to this update), below are what times were for a sample page (Admin > Setup page), using my 2017 iMac.

*All times are in seconds representing averages over 3 refreshes on an installation with 1000 fields, templates and fieldgroups.*

**Previous core, before any lazy loading added: **

```
0.7160 all (full execution time)
0.6790 boot
0.6560 boot.load
0.5167 boot.load.fields
0.0537 boot.load.fieldgroups
0.0449 boot.load.templates    
```

As you can see, when there are 1000 fields and templates, the boot time gets heavy and is well over half a second. This leads to full a execution time of over 700ms. Most of that boot time is the loading of fields, which is just about exactly half a second. Following the update, with lazy-loading enabled, here's the same test, on the same page:

**New core with lazy-loading enabled:**

```
0.1078 all (full execution time)
0.0820 boot
0.0598 boot.load
0.0062 boot.load.fields
0.0077 boot.load.fieldgroups
0.0062 boot.load.templates    
```

Wow! As you can see, that's a pretty major difference in performance!

Because a lot of other core updates were made related to this, you don't even need to have lazy loading enabled to see a great performance improvement. Below is what it looks like on the new core updates with lazy loading OFF, set by `$config->useLazyLoading = false;`

**New core with lazy-loading disabled:**

```
0.2547 all (full execution time)
0.1878 boot
0.1654 boot.load
0.0322 boot.load.fields
0.0547 boot.load.fieldgroups
0.0382 boot.load.templates
```

So while it is a lot faster with lazy loading enabled, even with lazy loading off, the core is still much *much* faster at this scale than it was a week ago. That's because the optimizations this week have gone beyond just lazy loading. When you get into something like this, it leads to other ideas of how to improve things, so that's what's been happening.


### Small scale performance improvements

The above examples are with a site having a thousand each of fields, templates and fieldgroups, and I'm guessing not many of us use that many. So you might be wondering what kind of difference you can expect on a smaller site. I tested on a site with 22 fields and 17 templates and found that the difference at this scale is very little, but still measurable. With lazy loading off, last week's core and this week's core with lazy loading OFF have identical load times. And with lazy loading ON, boot.load is 0.0731s or 0.0938s when OFF. Not enough to be felt, but still a small improvement that can add up over hundreds of requests, even at this smaller scale. I'm happy with that because sometimes things that improve performance at large scale add some overhead at small scale, and that doesn't appear to be the case here.


### Full circle

ProcessWire has always been highly scalable with pages, but not so much with fields and templates. What I really like about this update is that it means ProcessWire is now very scalable with fields and templates too. This can be a game changer for some. I still think it's a good idea to avoid using more fields than you need, just as a matter of good housekeeping. But it's also nice to know that you no longer trade quantity for performance when it comes to fields and templates.


### 3.0.194 coming soon

I'm not bumping the core version this week because I think it's best not to upgrade immediately unless you've read this post first. When I bump the version, it triggers the upgrades module, and some people might upgrade without knowing there's some fairly major changes in place that probably shouldn't go into a production site just yet. At one point this week while working on these updates, I managed to wipe out all the repeater fields on one test installation. While that issue was fixed, it was enough to make me want to have a week of help testing before we bump the dev branch version number. Though I think after a week, if no significant issues arise, we'll be on track for a stable upgrade and version bump as we inch closer to our next master release.

Big thanks to Michael Spooner for his work here, which we'll all benefit from! Have a great weekend and visit the [ProcessWire Weekly](https://weekly.pw) for the latest core news and updates.
