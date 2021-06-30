# remote_video_camera-live_streaming-recording-django-opencv-raspberry_pi

Introduction:

This software has been made mainly for running on raspberry pi. The objective is to stream live video (video can be recorded if necessary) from a webcam (connected with a raspberry pi) attached to main door of a house to any device (by entering the IP address of the raspberry pi in the web browser) over a same wifi network using a web browser when someone knocks Records (each time an user uses the software to live stream) can also be maintained by recording the username and the time of login.

Frameworks and Libraries used:
  1. Django
  2. OpenCV
  3. OS 
  4. sys
  
  Database used with django - MySqlite
  
Description of diffrent django apps:

  1. main: This app streams live video, records live video, maintains records (start time of streaming, stores username, 
  video recording on or off, ), lets user to change settings (), lets user to view and update records.
           
  2. user_authentication: This app helps in signing up, logging in and signing out.
  
  Description of different files in the project:
  
      1. capture.py (location: base_dir/camera): Responsible for capturing frames and recording video.
      
      2. views.py (app: main): 
          
          function_1 - video_stream(): It calls gen() function from capture.py file and keeps on returning the frames to 
                                       a html page.
                                       
          function_2 - index(): It returns the a html file named index.html () From inside of the index.html file an html image tag 
                                calls the video_stream() function which returns the images to the html image tag at a rate specified
                                by the user from settings.html file (settings.html file interacts with the settings() function and updates 
                                the settings table in the database).
                                
          function_3 - settings(): It return a html file named settings.html (get request) from where users can customize certain things 
          like fps, path of recording and whether   video has to be recorded while streaming or not.
                                    
          function_4 - settings.save(): It returns a html file names settings_save.html which tells the user that all the settings have
                                         been updated successfully.
                                         
          function_5 - video_record_current(): It edits a file named recording_switch.txt and changes the content to "True-Current" and
                                               and then calls the index() function (redirecting to the index.html file).
                                               
                                               Reason:
                                               
                                               As mentioned above an user can specify (using settings() function) whether video will 
                                               be recorded or not that's why incase recording is switched off and suddenly an user
                                               wants to record the ongoing session (live streaming is going on) then using a button on
                                               index.html page user can start recording that particular session. 
                                               
                                               In this case recording will not be switched on permanently rather that particular session
                                               will be recorded till the time user exits the streaming page (index.html).
                                               
                                               Working:
                                               
                                               When recording is switched off and user clicks on the recording button then this function
                                               (video_record_current()) function is called and in turn it edits a file named                                                                                                    recording_switch.txt and changes the content to "True-Current" and
                                               and then calls the index() function (redirecting to the index.html file).
                                               
                                               Now as mentioned above that a html image tag inside the index.html page calls 
                                               video_stream() function and the video_stream() function in turn interacts with the                                                                                                capture.py in order to stream the video (capture.py file records the video as well
                                               if specifiedspecified by users). Now if the content inside the recording_switch.txt file
                                               is set to "True-Current" the capture.py file gets to know that the session has to be
                                               recorded for this particualr session and it starts recording the video.
                                               
                                               After it starts recording the video it sets the content of recording_switch.txt file
                                               to "False", otherwise it video will get recorded for future sessions as well which is not                                                                                        required.
                                               
        function_6 - logs():  Returns a html file named logs.html (get request) which shows all the records (login time, username of the user who logged in, 
                              recording present or not) and gives the option to watch the recorded video, download the recorded video and to delete the log 
                              including the recorded video if present.
                              
                              This page also has the option the filter logs by date.
                              
       function_7 - delete_log_confirm(): On clicking on the delete button on the log.html page this function is called and user is taken to
                                           delete_log_confirm.html page to verify whether rally wants to delete the particular log or not.
                                           
       function_8 - delete_log(): On clicking yes on delete_log_confirm page this function is called and the log is deleted along with the video.
                                  It first checks whether the recording is present or not using the os module and if present it deletes the log along
                                  with the recording.
                                  
   3. views.py (app: user_authentication): 
          
        function_1 - signup(): This returns (GET request) the signup.html file which contains the form for signing up.
                               On submitting the form it POST requst block is called and new user is created and at last it return the
                               the signup_confirmation.html file which shows that the user has successfully signed up. 
                               
         Django's inbuilt signup feature has been used for signning up
                               
                               
        The built in login and logout feature provided by Django has been used for logging in and logging out.
        
        
        Forms for signup (in signup.html) and login (in login.html) have been created in forms.py file.
                    
                                             
                                              
                                               
                  
                                
  
  
 
 
  
  

