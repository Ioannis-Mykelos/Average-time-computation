# Average-time-computation
This is a real world project with a real data set provided.
The tracking framework is event based, so the App sends events the instant they happen: to evaluate the average time spent in a lesson we need to run a calculation. 
Tracking is anonymous by design: the App does not require a login, so we don’t know anything about users. 
We do track a device id, but we know that in a school environment we will likely have multiple users using the same device. We track app launch events, steps in a lesson, pause and resume events and hub connection events. 
We attach a session_id to every event where we define a “session” as the time interval when the App is active (sending events) with pauses not longer than 10 minutes, so if the user is not active on the App for more than 10 minutes, a new session is started.
