Title: Anatomy of a Facebook Phishing Campaign
Date: 2015-01-30 10:00
Category: Research

An average of 1,200 phishing messages were verified each day on [PhishTank](https://www.phishtank.com/) during the month of January 2015. Most phishing attempts are delivered through email. However, some phishing attacks leverage social networking. This is an analysis of one phishing attack seen on Facebook.

A Facebook user reported seeing the following on their newsfeed:

![1]({static}/images/research/anatomyoffacebookphishing/1_fbook_phishing.png#center)

---

Clicking on this image or the link in the text directs the victim to the domain, *tgd37[.]tk*, where they would have seen the following:

![1]({static}/images/research/anatomyoffacebookphishing/2_fbook_phishing1.png#center)

---

This image was actually hosted within a frame. The frame was grabbing content from *nomiup[.]com/coasterpa*, as shown in the following html code:

![1]({static}/images/research/anatomyoffacebookphishing/3_fbook_phishing.png#center)

---

Visiting nomiup[.]com/coasterpa directly, we saw the image. Looking at the source code, there was an inline frame leading to where the image was hosted, at i[.]imgur[.]com/m8GyCcC.jpg and a link to a third URI: *giftscrd-1[.]com/Loginp*:

![1]({static}/images/research/anatomyoffacebookphishing/4_fbook_phishing.png#center)

---

Clicking on the play button or anywhere on the image loaded the following page from *giftscrd-1[.]com/Loginp*:

![1]({static}/images/research/anatomyoffacebookphishing/5_fbook_phishing1.png#center)

---

Rather than coding the display, the attacker used a background image of the Facebook login screen, which was linked directly from i[.]imgur[.]com/g2fm2mB.png, instead of using the previous iframe redirection techniques. The two text fields meant for the victim’s username and password were haphazardly thrown on top of the image, which would most-likely have gone unnoticed to a victim who managed to get this far in the process.

Clicking the ‘Log In’ button would submit the entered text to *giftscrd-1[.]com/get.php*, as seen in this snippet of html code:

![1]({static}/images/research/anatomyoffacebookphishing/6_fbook_phishing.png#center)

---

Once get.php processed the credential submission, the victim would finally be redirected to a YouTube video located at *www[.]youtube[.]com/watch?v=C7_keOOwqZo*. The video is a compilation of roller coaster accidents:

![1]({static}/images/research/anatomyoffacebookphishing/7_fbook_phishing.png#center)

---

### Investigating the domains

The first domain in the Facebook lure, *tgd37[.]tk*, had been hosted on the IP address *195.20.42[.]203* since January 22, 2015 and has not been seen on any other IP addresses as of this writing.

![1]({static}/images/research/anatomyoffacebookphishing/8_fbook_phishing.png#center)

---

*tgd37[.]tk* had no traffic until January 23, 2015, when a relatively large spike of DNS requests was seen via the OpenDNS infrastructure.

![1]({static}/images/research/anatomyoffacebookphishing/9_fbook_phishing.png#center)

---

On January 23, 2015, the number of requests went to 2 at 4:00 PM, 6 at 6:00 PM, 10 at 7:00 PM and 26 by 9:00 PM. There were no further requests after 11:00 PM.

![1]({static}/images/research/anatomyoffacebookphishing/10_fbook_phishing.png#center)

---

Overall, there weren’t many requests in this phishing campaign, but we can probably assume that the first few requests might have been tests while the majority of them around 9:00 PM were potentially victims falling for the click-bait on their Facebook newsfeed.

At the time of this analysis, the IP address hosting *tgd37[.]tk*, 195.20.42.203 was hosting 113 domains and belonged to *freenom[.]com*, a free hosting provider based in Amsterdam. Historical DNS data shows that this IP address has been used to host a total of 434 domains over its history.

In the html source code of *tgd37[.]tk* was a google analytics account number, UA-23441223-3. Looking into this account, we were able to find other domains it was watching, but were unable to access any analytic information for this domain.

The second domain, called in the iframe at *tgd37[.]tk* was *nomiup[.]com*. DNS lookups of *nomiup[.]com* using the OpenDNS infrastructure looked a little more normal:

![1]({static}/images/research/anatomyoffacebookphishing/11_fbook_phishing.png#center)

---

*nomiup[.]com* has been hosted at *108.175.158[.]12* since September 15, 2014.

![1]({static}/images/research/anatomyoffacebookphishing/12_fbook_phishing.png#center)

---

As of this writing, there were 723 domains hosted on *108.175.158[.]12*. Historical DNS data showed that this IP address had hosted a total of 1,235 domains for its entire history to this point and that it was owned by Arvixe, a hosting provider in Santa Rosa, CA

*nomiup[.]com* had only the following content at its root, which was a little odd considering the amount of DNS requests. It’s possible that *nomiup[.]com* had been used as a landing page for other campaigns, which may describe the traffic.

![1]({static}/images/research/anatomyoffacebookphishing/13_fbook_phishing.png#center)

---

The iframe in the source code of *nomiup[.]com/coasterpa* contained an image link to the fake video image and, if clicked, led the victim to *giftscrd-1[.]com/Loginp*

The root of *giftscrd-1[.]com* didn’t have an index page, so the following directories and server software version were shown:

![1]({static}/images/research/anatomyoffacebookphishing/14_fbook_phishing.png#center)

---

Each directory contained the same html which linked to the fake Facebook login page.

DNS requests for this domain from the end of December, 2014 to late January, 2015 spiked up fairly often, potentially showing the use of *giftscrd-1[.]com* in various phishing campaigns.

![1]({static}/images/research/anatomyoffacebookphishing/15_fbook_phishing.png#center)

---

*giftscrd-1[.]com* was also hosted with Arvixe and historical DNS showed that it had been hosted at the IP address *23.91.126[.]104* since December 12, 2014.

![1]({static}/images/research/anatomyoffacebookphishing/16_fbook_phishing.png#center)

---

*23.91.126[.]104* was providing hosting for *giftscrd-1[.]com* and two other domains that might have been employing legitimate hosting services provided by Arvixe:

![1]({static}/images/research/anatomyoffacebookphishing/17_fbook_phishing.png#center)

---

DNS requests to these other domains did look a little suspicious though:

*ns2[.]giftscrd[.]arvixevps[.]com*:

![1]({static}/images/research/anatomyoffacebookphishing/18_fbook_phishing.png#center)

---

*stats[.]giftscrd[.]arvixevps[.]com*:

![1]({static}/images/research/anatomyoffacebookphishing/19_fbook_phishing.png#center)

---

### What was the attacker attempting to accomplish?

In an attempt to answer this question, I created a Facebook profile and entered the credentials into the form fields. Sometime within about 24 hours, I was alerted to a login from IP address *198.23.103[.]79*

![1]({static}/images/research/anatomyoffacebookphishing/20_fbook_phishing.png#center)

---

This IP address belonged to the VPN provider, Private Internet Access, which demonstrates that the attacker was protecting their actual location:

![1]({static}/images/research/anatomyoffacebookphishing/21_fbook_phishing.png#center)

---

While my decoy Facebook profile was designed to be as realistic as possible, it’s unfortunate that he didn’t have any friend connections. The attacker may have logged in and quickly noticed that there would be no point in taking over the account or doing anything malicious.

### Actions taken

Phishing is an effective way for attackers to exploit individuals in order to deliver malware or acquire user credentials. Finding the source of a phishing attempt, any contextual information and the goal of the attack increases the ability to mitigate it. In the case of this phishing attack, the three domains, *tgd37[.]tk*, *nomiup[.]com* and *giftscrd-1[.]com* would be blocked or watched to determine if anyone might have visited them. Additionally, domains associated with the Google Analytics account might be investigated further and blocked. If someone had visited any of these domains, it would be recommended that they change their Facebook password and update credentials for any accounts sharing the same password as their Facebook account.
