SESSION 11 - Working With Media Files & User ProfileTopicsMEDIA_ROOT and MEDIA_URLUpload profile pictureServing uploaded filesActivitiesProfile edit page (update photo, name, phone)
Pending
Tasks
1.
Set up MEDIA_ROOT and MEDIA_URL in your Django project's settings.py so that uploaded media files are stored in a folder named 'user_uploads' and can be accessed via '/media/'.
2.
Create a Django model called InfluencerProfile with fields: user (OneToOneField), display_name (CharField), bio (TextField), and profile_pic (ImageField). Ensure profile_pic uploads to 'profile_pics/'.
3.
Build a profile edit page where users can update their display name, bio, and upload a new profile picture, similar to editing your Instagram profile.
4.
Display the uploaded profile picture on the user's profile page, falling back to a default image if no picture is uploaded.<br><br><em><strong>Hint:</strong> Use the MEDIA_URL setting and check if profile_pic exists for the user.</em>
5.
Add a phone number field to your InfluencerProfile model, update the edit form to allow changing it, and validate that the phone number is exactly 10 digits.<br><br><em><strong>Constraint:</strong> Show an error message if the phone number is invalid.</em>