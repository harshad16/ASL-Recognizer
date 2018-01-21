# ASL-Recognize
ASL-Recognizer: It empower the speak disabled people to communicate through sign language with the people who doesnt understand sign language.
The Porject recognises the sign language and outputs it in form text and sound.Such that the person who couldn't understand sign language can communicate with the speak disabled people freely.

Hardware Required:
Leap Motion Sensor
https://www.leapmotion.com/

Software:
AWS Machine Learing API.

1. Constructed 60,000 instance of Leap motion featured data of 11 sign symbol of ASL(America Sign Language) to produce a dataset.
2. Used that dataset to train our AWS ML Model,which uses the multinomial logistic regression to classify the multiclass data.
3. On Running the app.py, real time data(the hand gesture feed) are recognised through the ML Model.
4. Return the Result
