---
title: Card sorting for prioritization
parent: Extras
nav_order: 2
permalink: /extras/card-sorting-for-prioritization/
---

# Card sorting for prioritization

From [Chapter 13, Findability and Navigation]({{ '/chapters/findability-and-navigation/' | relative_url }}).
{: .fs-5 }

Although card sorting is primarily an organization or naming technique, variations of it can also be used for other purposes. UX leader Jesse James Garrett and Mike developed a straightforward technique that combines closed card sorting with a speak-aloud protocol (see [Chapter 8, Usability Testing]({{ '/chapters/usability-testing/' | relative_url }})) to understand how people prioritize features.

As a break in a long one-on-one interview, they asked a group of participants to organize cards with descriptions of current and potential features for presenting current events on websites. Each card had a single sentence that described a way that information could be presented or organized. Jesse and Mike first asked them to place the cards into one of four piles based on the feature's current worth to them, as they used the Web right now. The four piles were labeled "Most Valuable," "Somewhat Valuable," "Least Valuable," and "Not Valuable." As participants placed the cards in these piles, Jesse and Mike asked each one to narrate their thoughts about the topic to understand why they made certain choices and how they thought about the features.

After the participants completed organizing the cards, Mike and Jesse asked them to repeat the exercise, but this time only using the cards that they had put into the "Most Valuable" pile and with a different set of criteria for the placement. The new task was for them to organize the features in terms of how *frequently* they felt they would use each of the features. This was done in order to differentiate between the features that attracted people to a site and those that they felt were the most immediately useful.

To understand where the participants' values lay, each one of the categories was given a numerical rating indicating the strength of preference, from 0 to 5:

| Rating | Meaning |
|---|---|
| 0 | Not valuable |
| 1 | Least valuable |
| 2 | Somewhat valuable |
| 3 | Most valuable, rarely used |
| 4 | Most valuable, sometimes used |
| 5 | Most valuable, used often |

Jesse and Mike then rated participants' choices, and calculated the *median* value of their ratings. Since a number of choices had the same median, it was necessary to further organize the list. Mike and Jesse calculated the *standard deviation* and represented the degree of agreement among all the ratings for a given category, with lower deviations representing greater agreement. (See [Chapter 10, Surveys]({{ '/chapters/surveys/' | relative_url }}) for more on calculating the median and standard deviation.) They then ordered the list first by preference, and then by agreement. This gave the development team a much clearer idea of their customers' values, and in turn helped them prioritize their own development efforts.
