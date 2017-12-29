# alexa-googlemaps
**Unofficial Google Maps skill for Alexa**

## SKILL COMMANDS

1. Request travel time to a place: "Alexa, ask Google Maps how long does it take to get to Coventry?"
2. Request travel time from one place to another: "Alexa, ask Google Maps for directions from London to Glasgow"
3. Get current commuting time: "Alexa, ask Google Maps how is my commute?"
4. Get time for commuting home: "Alexa, ask Google Maps how is the traffic home?"

## SETUP INSTRUCTIONS

### Step 1: Get a Google Maps API key

Each Google Maps Web Service request requires an API key or client ID. API keys
are freely available with a Google Account at
https://developers.google.com/console. The type of API key you need is a
**Server key**.

To get an API key:

 1. Visit https://developers.google.com/console and log in with
    a Google Account.
 1. Select one of your existing projects, or create a new project.
 1. Enable the API(s) you want to use. The Python Client for Google Maps Services
    accesses the following APIs:
    * Directions API
    * Distance Matrix API
    * Elevation API
    * Geocoding API
    * Geolocation API
    * Places API
    * Roads API
    * Time Zone API
 1. Create a new **Server key**.

For guided help, follow the instructions for the [Directions API][directions-key].
You only need one API key, but remember to enable all the APIs you need.
For even more information, see the guide to [API keys][apikey].

**Important:** This key should be kept secret.


### Download code from github

1. Click on the green "Clone or download" button just under the yellow bar
2. Click download ZIP
3. Unzip the file (it will be called alexa-googlemaps-master.zip) to a known place on your hard-drive

### AWS Lambda Setup

1. Go to http://aws.amazon.com/. You will need to set-up an AWS account (the basic one will do fine) if you don't have one already. Make sure you use the same Amazon account that your Echo device is registered to. **Note - you will need a credit or debit card to set up an AWS account - there is no way around this. There should be no charges from using this skill in a normal way, though I am not resposible if there are.**
2.  Go to the drop down "Location" menu at the top right and ensure you select "US-East (N. Virginia)" if you are based in the US or "EU (Ireland)" if you are based in the UK or Germany. This is important as only these two regions support Alexa. 
3. Select Lambda from the AWS Services menu at the top left
4. Click on the "Create Function" button.
5. Select "Author From Scratch", and name the Lambda Function :-

    ```
    GoogleMaps
    ```
6. Select the runtime as "Python 2.7".
7. Set the Role as "Create a Custom Role".
8. In the new window that opens, set the IAM Role as "Create a New IAM Role", and set the Role Name as "lambda_basic_execution", then click Allow.
9. Back in the Lambda Management window, click "Create Function".
10. Under "Add Triggers", select "Alexa Skills Kit" (NOTE - if you do not see Alexa Skill Kit as an option then you are in the wrong AWS region). Under "Configure Triggers", click "Add".
11. In the middle of the screen, click on the box that says "GoogleMaps".
12. Under "Function Code", make sure Runtime says "Python 2.7", and Handler says "lambda_function.lambda_handler"
13. Under "Code Entry Type", select "Upload a .ZIP file".
14. Click on the "Upload" button. Go to the folder where you unzipped the files you downloaded from Github, select Alexa-GoogleMaps.zip and click open. Do not upload the alexa-googlemaps-master.zip you downloaded from Github - only the Alexa-GoogleMaps.zip contained within it.
15. Enter the following into the Environment Variables Section (If you are pasting in the API Key then make sure you have no extra spaces):

|Key           | Value|
|--------------| -----|
|API_KEY       |(Put the Google API key in here)|
|COUNTRY       |(Put your country name in here, eg UK, USA)|
|WORK          |(Put your work address in here)|
|HOME          |(Optional, if you cannot set your home address in the Alexa app, put it here)|

16. Click "Save" in the top right. This will upload the Alexa-GoogleMaps.zip file to Lambda. This may take a few minutes depending on your connection speed.
17. Copy the ARN from the top right to be used later in the Alexa Skill Setup (it's the text after ARN - it won't be in bold and will look a bit like this arn:aws:lambda:eu-west-1:XXXXXXX:function:GoogleMaps). Hint - Paste it into notepad or similar.


### Alexa Skill Setup

1. In a new browser tab/window go to the Alexa Console (https://developer.amazon.com/home.html and select Alexa on the top menu)
2. If you have not registered as an Amazon Developer then you will need to do so. Fill in your details and ensure you answer "NO" for "Do you plan to monetize apps by charging for apps or selling in-app items" and "Do you plan to monetize apps by displaying ads from the Amazon Mobile Ad Network or Mobile Associates?"
3. Once you are logged into your account go to to the Alexa tab at the top of the page.
4. Click on the yellow "Get Started" button under Alexa Skills Kit.
5. Click the "Add a New Skill" yellow box towards the top right.
6. You will now be on the "Skill Information" page.
7. Set "Custom Interaction Model" as the Skill type
8. Select the language as English (US), English (UK), German, English (Australia) or English (India), whichever suits you best. - **Note: For German you will need to do some translation below**
9. Set the "Name" to 

    ```
    Google Maps
    ```
    
10. Set the "Invocation Name" to 

    ```
    Google Maps
    ```
11. Set the "Audio Player", "Video App", and "Render Template" settings to "No"
12. Click "Save" and then click "Next".
13. You will now be on the "Invocation Model" page.
14. Copy the text below into the "Intent Schema" box - Ignore the "Built-in intents for playback control box above". If you are in the UK, replace "AMAZON.US_CITY" with "AMAZON.GB_CITY", or use "AMAZON.DE_CITY" for Germany, "AMAZON.AT_CITY" for Austria, or "AMAZON.EUROPE_CITY" for anywhere else in Europe. For Australia or India, use "AMAZON.City". Canadians, or others, replace "AMAZON.US_CITY" with just "CITY", and make sure to follow step 15.

```
{
  "intents": [
    {
      "intent": "AMAZON.CancelIntent"
    },
    {
      "intent": "AMAZON.HelpIntent"
    },
    {
      "intent": "AMAZON.StopIntent"
    },
    {
      "intent": "GetCommuteToWork"
    },
    {
      "intent": "GetCommuteFromWork"
    },
    {
      "slots": [
        {
          "name": "tocity",
          "type": "AMAZON.US_CITY"
        }
      ],
      "intent": "GetDirectionsTo"
    },
    {
      "slots": [
        {
          "name": "fromcity",
          "type": "AMAZON.US_CITY"
        },
        {
          "name": "tocity",
          "type": "AMAZON.US_CITY"
        }
      ],
      "intent": "GetDirectionsFromTo"
    }
  ]
}
```
15. **Canadians Or Others Only** Under "Custom Slot Types", in the "Enter Type" box, type CITY. In the "Enter Values" box, type in the names of as many cities in your country as you can, one on each line. Canadians can paste the contents of CanadianCities.txt, which is in the zip file you downloaded from this github page. Make sure to click "Add" when you have finished.
16. Copy the text below and paste them into the Sample Utterances box. **For German, you need to translate these into German, don't change the first word on each line or the words in curly brackets.**
```
GetCommuteToWork How is my commute
GetCommuteToWork How is my commute to work
GetCommuteToWork How is the traffic to work
GetCommuteToWork How is the drive to work
GetCommuteToWork My travel time to work
GetCommuteFromWork How is my commute home
GetCommuteFromWork How is my commute home from work
GetCommuteFromWork How is the traffic home
GetCommuteFromWork How is the drive home
GetCommuteFromWork My travel time home from work
GetDirectionsTo Get directions to {tocity}
GetDirectionsTo How long does it take to get to {tocity}
GetDirectionsTo How far is {tocity}
GetDirectionsTo How far away is {tocity}
GetDirectionsTo How far to {tocity}
GetDirectionsTo How long to {tocity}
GetDirectionsTo Give me directions to {tocity}
GetDirectionsTo For directions to {tocity}
GetDirectionsFromTo Get directions from {fromcity} to {tocity}
GetDirectionsFromTo How long does it take to get from {fromcity} to {tocity}
GetDirectionsFromTo How far is it from {fromcity} to {tocity}
GetDirectionsFromTo How far from {fromcity} to {tocity}
GetDirectionsFromTo How long from {fromcity} to {tocity}
GetDirectionsFromTo Give me directions from {fromcity} to {tocity}
GetDirectionsFromTo For directions from {fromcity} to {tocity}
```
17. Click "Save" and then "Next".
18. You will now be on the "Configuration" page.
19. Select "AWS Lambda ARN (Amazon Resource Name)" for the skill Endpoint Type.
20. Where it says "Default", paste into the box the ARN you copied earlier from the AWS Lambda setup.
21. Select "No" for "Provide geographical region endpoints?" and also select "No" for Account Linking
22. Under Permissions, tick the Device Address box, and select Full Address.
23. Click "Save" and then "Next".
24. There is no need to go any further through the process i.e. submitting for certification.

### Skill Permissions

You need to give the skill permission to see your home address from the Alexa app.
If you cannot set your address in the Alexa app, for example if you are in a non-supported country,
make sure to set the HOME variable in step 15 of the Lambda setup.

1. Open the Alexa app and go to "Skills".
2. In the top right select "Your Skills".
3. Find the Google Maps skill and select it.
4. Click "Settings", and then "Manage Settings". If you don't see a Settings button, you didn't ask for the Full Address in step 22 above.
5. Turn on "Device Address", and click "Save Settings".


[apikey]: https://developers.google.com/maps/faq#keysystem
[directions-key]: https://developers.google.com/maps/documentation/directions/get-api-key#key

