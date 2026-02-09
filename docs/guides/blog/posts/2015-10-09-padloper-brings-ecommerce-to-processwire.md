# Padloper brings eCommerce to ProcessWire

Source: https://processwire.com/blog/posts/padloper-brings-ecommerce-to-processwire/

## Sections


## Padloper brings eCommerce to ProcessWire

9 October 2015 by Ryan Cramer [ 3 Comments](/blog/posts/padloper-brings-ecommerce-to-processwire/#comments)

It's Antti here again. Three weeks ago I was talking about [what we have been doing with ProcessWire at Avoine](/blog/posts/introducing-iftrunner-and-the-story-behind-it/). This time Ryan asked me if I would like to write something about my personal project called [Padloper](https://www.padloper.pw) that was [released last Sunday](https://twitter.com/apeisa/status/650746077965123585). You don't have to ask me twice for this kind of opportunity, so here I am again. Don't worry, Ryan is back next week!


## A little bit of History

I have been building websites for almost 20 years now (that is a little bit scary fact...). The year was 1997 and I was 13-years old back then. I used to stay at our school's computer class surfing the internet and reading all about how to build websites. It was just HTML, animated gifs, FONT-tags and Geocities back then! My first websites were all gaming and music related. First I maintained Pelisauna ("Gaming Sauna") with my friend, which was quite a popular freeware gaming site. After that I started Rockmusica (with about 10 of us writing reviews), which was a music zine. This background led me to cofound Levyvirasto ("Record Office") with my two brothers in 2005. Levyvirasto was an eCommerce site, which sold records (both physical and MP3) from Finnish indie labels and bands directly. It was a local clone of [CD Baby](http://www.cdbaby.com/) (which was insanely popular back then). I still remember those fights against osCommerce (our weapon of choice back then) when I tried to bend the "templates" to my will. After that journey I have built more than 10 webshops, using multiple platforms. Every time I have built eCommerce sites, I have ended up in tears. Why are simple modifications to frontend templates made so difficult? I know the eCommerce platforms today are far better and more flexible than what osCommerce was 10 years ago, but I doubt that any of them are more flexible than ProcessWire!

Looking at my background, it is no surprise that when I first found out about ProcessWire, my mind was already thinking about how cool a platform it would be for eCommerce sites. When we started using ProcessWire for our client projects at Avoine, I knew the "*we need a webshop too*" -project would come sooner or later. It did come—with a tight deadline—and I ended up building "Shop for ProcessWire" and released it as open source. The client got a great shop, but the community didn't get a great shopping platform. It was built very quickly for one specific shop and project in mind. It wasn't something that was easy or flexible to extend. You know how projects with tight deadlines go?


## Padloper was Born

In summer 2014 I started to build a new eCommerce platform for ProcessWire. This time I wanted to make it as good as possible, being a platform flexible enough for all kinds of eCommerce projects. I also decided to release it as a commercial module, so I could better justify (for myself and for my family) the endless hours I put into it. I wanted to do it as well as I could (don't you love the excitement and all the possibilities when you are starting new project?). The initial plan was to release it in August 2014. I missed that by just two months... and a year! You know how projects without client pressure and deadlines go?

Because Padloper is a sideproject and I have a full time job and a family, I really made progress only during holidays. So the next active development phase was Christmas 2014. I almost nailed it then! After Christmas I decided to drop some features I had planned and focus on getting it released and getting some real feedback. Finally on February 2015 I started closed beta for my newsletter subscribers. That was a big milestone for me personally and for the project.

The feedback I got from first customers was very encouraging. People actually liked it! I was always worried that my decision to do less (a big decision was dropping the full blown shop profile from the release version) would make it too difficult for others to adapt. But I guess people using ProcessWire do like to build things by themselves. That was also my original vision for Padloper: you can have the greatest product catalog built and released. Then any given day you just install Padloper on top of it. It doesn't care how you build your templates and frontend. All Padloper actually needs is a price field for your product template(s).


## The logic behind Padloper

What makes Padloper unique? Why should you care? To be honest with you - the only thing really special in Padloper is ProcessWire. Well, what difference does ProcessWire make compared to more traditional eCommerce solutions? Total flexibility regarding frontend and product fields. Total flexibility with how the website and webshop work together (they can and should be the same site). Very easy to extend and alter behaviour (hooks). While Padloper works well for traditional webshops too (categories and products in grid), it really shines for more customized webshops, usually heavy on content with lots of crosslinks.

At one point I rewrote big parts of the order management, since initally it used custom database tables to store orders. That again created more flexibility for ProcessWire developers. This made it very easy to create custom sales reports, but also made it very simple to extend the information you ask from customers and storing orders.


## Where is Padloper going?

This [little turtle](https://www.google.fi/search?q=padloper&source=lnms&tbm=isch&sa=X&ved=0CAcQ_AUoAWoVChMIp_7b_vW1yAIVgQ9yCh2ODwu-&biw=1200&bih=855) will definitely go forward. This is just the beginning, but unfortunately I haven't yet figured out how to find more hours. I will focus on feedback I get from the developers. Meaning bug fixes, more documentation, a more streamlined checkout process etc. And I have to say that I have been lucky with my customers. I have got brilliant feedback, ideas, discussions, code snippets and even modules! Huge thanks to everyone who has helped me (you are way too many to start mentioning here without forgetting someone...).

To learn more about Padloper visit the website at [padloper.pw](http://www.padloper.pw) - there is nice release sale going on for a few weeks. Here is also a few screenshots that hopefully can give you sneak peak at what it does.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/downloads.png)[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/shipping.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/edit-order.png)[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/order-search.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/reports.png)[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/view-order.png)

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1119/taxes.png)
