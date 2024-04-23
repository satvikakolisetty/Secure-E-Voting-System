# E-Voting System Documentation

## System Architecture
![System Design of a E-Voting System](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/System%20Architecture.jpg)

The proposed e-voting system comprises several components including fingerprint sensors, webcams, Arduino boards, and machine learning algorithms for facial and fingerprint recognition.

## Algorithm for the Proposed Design

1. Keep the voting switch turned on.
2. Record fingerprints and face images using the webcam and fingerprint reader.
3. Verify the entries:
   - If both entries match, proceed to step 7.
   - If only one entry matches, allow the booth manager to determine correctness.
   - If none match, sound an alert and display "Unauthorized to Vote."
4. The booth head enters the private key for further verification.
5. If verification fails, identify the mismatch.
6. Voters press buttons with candidate emblems to cast votes.
7. Save the vote in the database.

## Face Recognition Verification

Facial images are compared with those in the database using CNN architectures like VGG-16, AlexNet, and Random Forest Algorithm. VGG-16 showed superior performance.

## AlexNet Architecture

AlexNet consists of convolutional and fully connected layers. It contains 60 million parameters and 650,000 neurons. Despite its size, it operates quickly on GPUs and achieves high accuracy.

## Random Forest Algorithm

The Random Forest method combines multiple decision trees for classification. More trees in the forest lead to higher prediction accuracy.

## VGG16 Architecture

VGG16 uses convolutional layers with 3x3 filters and max-pooling layers for spatial pooling. It achieves high accuracy in facial recognition.

## Arduino

Arduino boards, such as the ATmega328-based Uno, facilitate interactions with sensors and control of physical objects.

## Fingerprint Reader

Biometric sensors like the R307 Fingerprint Sensor use UART interfaces for communication and comparison of fingerprint data.

![R307 Fingerprint Scanner Registration](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Fingerprint%20Registration.png)

## Fingerprint Verification

Fingerprint sensors, like the R307 module, compare acquired images with saved data. Different methods like optical and capacitive scanning are employed for fingerprint recognition.

![R307 Fingerprint Scanner Verification](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Fingerprint%20Verification.png)

## Power Supply Unit

Adapters convert electronic properties for different devices, ensuring compatibility and functionality.

## Face Recognition Verification Process

The Face images of individual are taken during enrollment time and that will be stored in the database. The database images and the captured image are compared and the result is taken. With the development of deep learning, face recognition technology based on CNN (Convolutional Neural Network) has become the main method adopted in the field of face recognition. This project also made use of CNN architectures such as VGG-16, Alex Net, and the Random Forest Algorithm. VGG-16 is the best facial recognition algorithm among all the algorithms tested.

## Fingerprint Verification Process

Fingerprint sensors are now used extensively in security measures and at every entry point. For identifying purposes, thumbprint applications have existed. Because each person has an unique identifier, this is the most effective way for a machine to authenticate an available person. The finger print picture acquired from the fingerprint module and compared to the fingerprints saved in the database. The database pictures and the acquired image are compared, and the result is recorded. For fingerprint recognition, we combined the R307 fingerprint sensor with the Arduino. In general, fingerprint scanners function by employing optical rays. In addition, it also digitally records a picture of the thumb. Now it watches the fingerprints sequence, translates this to numeric Zero and one, and creates the fingerprint's code. This fingerprint’s code serves as a fingerprint identifying key-pair. If it matches, then the sensor will provide access to the system. Fingerprint enrolment and fingerprint matching are both performed by this thumbprint reader. Each module in this R307 scanner must identify the address. 

## Web Application Developement
Web Technologies (HTML, CSS, JavaScript) has been used for implementing this project We used HTML to show the webpage, CSS to design the webpage, and JavaScript to make the webpage more interactive. Flask is a commonly used software plugin that is a Python library used to construct online Web applications. In this work, we used Flask to construct a web site where users may register for the voting process using face and finger print recognition, cast votes, and view voting results. We have constructed routes: one is an voting page where voters may login to the voting website, and the other is a registration page where voters can register to vote. When we search for the website using the link provided by the flask run command in the command prompt, i.e., http://localhost:5000, we are sent to the login page, followed by http://localhost:5000/admin for registration. MongoDB is a popular NoSQL database that is also an open-source document database. MongoDB is required for the creation and implementation of a highly scalable and performance-oriented database. The database stores information such as the user's login data and voting preferences.

## Voter Registartion Page

![Verification Page](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Voter%20Registartion%20Page.png)

## Voter Login Page

![Login Page](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Login%20Page.png)


## Voting Result Page

![Voting Results Page](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Voting%20Results%20page.png)

## Results and Discussion

The e-voting system employs CNNs for facial recognition and Random Forest for fingerprint verification. VGG-16 achieved the highest accuracy of 98.45%. 

### Comparison of Algorithms

![Comparision of Different ALgorithms](https://github.com/satvikakolisetty/Secure-E-Voting-System/blob/main/Accuracies%20of%20Diff%20Algorithms.jpg)

The graph represents Algorithms used on X-axis and accuracy in percentage on Y-axis. A bar graph is drawn based on the accuracies achieved using different Algorithms. After 20 epochs of testing in various models, we found that training our model using the VGG-16 architecture yielded the best results, with an accuracy of 98.45%. We can save both time and resources by using the notion of transfer learning and the pre-trained weights of the VGG16 architecture. We all know that training a Convolution Neural Network (CNN) from scratch takes a lot of data and also computes power. So, we instead use transfer learning, It will detect faces at different position and takes less processing time AlexNet 94.16%. Works with low power portable device Random forest Algorithm 92% This model can be used to different angles a model trained on similar data is fine-tuned as per our requirement. We have built three models — VGG-16, Alex Net and Random Forest Algorithm trained for face recognition as well as for face classification. We have used the VGG-16 model as it is a smaller model and the prediction in real-time can work on my local system without GPU. This implementation has the entire model in Keras with TensorFlow v1.14 as backend. We planned to build the same in TensorFlow v2.3 and extracted the model weights. These extracted weights were stored in vgg_face_weights.h5 and later loaded on an untrained VGG-16 (in TensorFlow v2.3) network shown in this project. The pre-processing generally depends on the underlying model. So, for training and testing, the input images have to go through the same pre-processing that is defined by the VGG-16 and Alex Net model. The results of the current model are much better than expected, but we could also improve them by manually creating good triplets.To create the model, we used the Convolutional VGG-16 architecture. When compared to alternative architectures, the key benefit of employing this is that it takes less processing resources and is 6 times quicker. Although both Alex Net and VGG16 contain 60M parameters, their accuracies are different. When we built a model utilising the VGG-16 Architecture, we got excellent results.


| Methods Used | Accuracy | Advantages |
|--------------|----------|------------|
| VGG16        | 98.45%   | Detects faces at different positions and has low processing time |
| AlexNet      | 94.16%   | Works with low-power portable devices |
| Random Forest Algorithm | 92% | Effective for recognizing faces at different angles |


The VGG-16 architecture showed the best results, providing a balance between accuracy and processing resources.



