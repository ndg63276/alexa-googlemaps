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

1. Go to http://aws.amazon.com/. You will need to set-up an AWS account (the basic one will do fine) if you don't have one already. Make sure you use the same Amazon account that your Echo device is registered to. **Note - you will need a credit or debit card to set up an AWS account - there is no way around this. Please see the AWS Charges section above**
2.  Go to the drop down "Location" menu at the top right and ensure you select US-East (N. Virginia) if you are based in the US or EU(Ireland) if you are based in the UK or Germany. This is important as only these two regions support Alexa. 
1. Select Lambda from the AWS Services menu at the top left
2. Click on the "Create a Lambda Function" or "Get Started Now" button.
3. Select "Blank Function" - this will automatically take you to the "Configure triggers" page.
4. Click the dotted box and select "Alexa Skills Kit" (NOTE - if you do not see Alexa Skill Kit as an option then you are in the wrong AWS region).
5. Click Next 
5. Name the Lambda Function :-

    ```
    Google Maps
    ```
    
5. Set the decription as :-

    ```
    Google Maps
    ```
    
    
6. Select the runtime as "Python 2.7".
7. Select Code entry type as "Upload a .ZIP file". 


7. Click on the "Upload" button. Go to the folder where you unzipped the files you downloaded from Github, select Alexa-GoogleMaps.zip and click open. Do not upload the alexa-googlemaps-master.zip you downloaded from Github - only the Alexa-GoogleMaps.zip contained within it.
8. Enter the following into the Environment Variables Section (If you are pasting in the API Key and Token then make sure you have no extra spaces: -

|Key           | Value|
|--------------| -----|
|API_KEY|(Put the Google API key in here)|
|COUNTRY|(Put your country name in here, eg UK, USA)|
|HOME|(Put your home address in here)|
|WORK|(Put your work address in here)|


9. Keep the Handler as "lambda_function.lambda_handler" (this refers to the main python file in the zip).
10. Under Role - select "Create a custom role". This will automatically open a new browser tab or window.
11. Switch to this new tab or window. 
11. Under IAM Role select "Create a new IAM Role"
11. Then press the blue "Allow" box at the bottom right hand corner. The tab/window will automatically close.
11. You should now be back on the Lambda Management page. The Role box will have automatically changed to "Choose an existing role" and Role we just created will be selected under the "Existing role" box.
13. Click on the blue "Next" at the bottom of the page and review the settings then click "Create Function". This will upload the Alexa-GoogleMaps.zip file to Lambda. This may take a few minutes depending on your connection speed.

14. Copy the ARN from the top right to be used later in the Alexa Skill Setup (it's the text after ARN - it won't be in bold and will look a bit like this arn:aws:lambda:eu-west-1:XXXXXXX:function:youtube). Hint - Paste it into notepad or similar.

[apikey]: https://developers.google.com/maps/faq#keysystem
[directions-key]: https://developers.google.com/maps/documentation/directions/get-api-key#key

