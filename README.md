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
2.  Go to the drop down "Location" menu at the top right and ensure you select "US-East (N. Virginia)" if you are based in the US or "EU (Ireland)" if you are based in Europe. This is important as only these two regions support Alexa. 
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

1. In a new browser tab/window go to the Alexa Console (https://developer.amazon.com/home.html and select Alexa, then Alexa Skills Kit on the top menu)
2. If you have not registered as an Amazon Developer then you will need to do so. Fill in your details and ensure you answer "NO" for "Do you plan to monetize apps by charging for apps or selling in-app items" and "Do you plan to monetize apps by displaying ads from the Amazon Mobile Ad Network or Mobile Associates?"
3. Once you are logged into your account go to to Alexa, then Alexa Skills Kit at the top of the page.
4. Click the "Create Skill" clue box towards the top right.
5. You will now be on the "Create a new skill" page. Name your skill Google Maps.
6. Select the language as English (US), English (UK), etc, whichever suits you best.
7. Under "Choose a model to add to your skill", select Custom.
8. Under "Choose a method to host your skill's backend resources", select "Provision Your Own".
9. Click "Create Skill" in the top right.
10. Under "Choose a template", select "Start from scratch", and click "Choose".
11. On the left, find where it says JSON Editor, and click on it.
12. Delete everything in the box that appears, then copy in the contents of InteractionModel.json. Click "Save Model" at the top.
13. Click "Endpoint" on the left.
14. Select "AWS Lambda ARN" for the Service Endpoint Type.
15. Where it says "Default Region", paste into the box the ARN you copied earlier from the AWS Lambda setup. Click "Save Endpoints" at the top.
16. Find and click "Permissions" at the bottom left, turn on Device Address, and select Full Address.
17. Click "Custom" on the left, then "Invocation". Then click "Build Model" at the top. Building takes about a minute.
18. Go to the "Test" tab at the top. Where it says "Test is disabled for this skill", change the dropdown to "Development".
19. There is no need to go any further through the process i.e. submitting for certification.

### Skill Permissions

You need to give the skill permission to see your home address from the Alexa app.
If you cannot set your address in the Alexa app, for example if you are in a non-supported country,
make sure to set the HOME variable in step 15 of the Lambda setup.

1. Open the Alexa app and go to "Skills & Games".
2. In the top right select "Your Skills", then scroll right and click "Dev".
3. Find the Google Maps skill and select it.
4. Click "Settings", and then "Manage Settings". If you don't see a Settings button, you didn't ask for the Full Address in step 16 above.
5. Turn on "Device Address", and click "Save Settings".


[apikey]: https://developers.google.com/maps/faq#keysystem
[directions-key]: https://developers.google.com/maps/documentation/directions/get-api-key#key

