
<p style="font-family: Arial; font-size:2.5em;color:purple; font-style:bold"><a href="https://github.com/pavelsjo/JackInTheBox"><img src="./images/liakad-Jack-in-the-box.png" alt="Buenos Aires Data" width="150px"></a><br>Jack in the Box</p><br>

### Main task:
- The mobile app **Jack in the Box** consists in push five buttons to open the Jack's box, so, based in this non revealed parameters(buttons), the goal is predict if jack or not jump out of box.
  - If `target_churn_indicator` **0** means yes.
  - If `target_churn_indicator` **1** means not.

<p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold"> Data description:</p>

The **box_data.csv**, is a (comma-separated-values) and if the main source of data, and contains the follows attributes:

#### Attributes[13]:
- **user_id:** anonymized id.
- **install_time:** gameplay date.
- **platform:** platform used: Android o iOS.
- **country_region:** player region.
- **city:** player city.
- **gender:** gender player, will be Male or Female.
- **min_age_range:** min age range.
- **max_age_range:** max age range.
- **event_1:** counts of events with button #1.
- **event_2:** counts of events with button #2.
- **event_3:** counts of events with button #3.
- **event_4:** counts of events with button #4.
- **event_5:** counts of events with button #5.
#### Clase[1]:
- **target_churn_indicator:** 
  - If **0** means yes.
  - If **1** means not.