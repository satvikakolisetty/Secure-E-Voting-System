# E-Voting System Documentation

## System Architecture
![System Design of a E-Voting System](path/to/system_design.png)

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

![Network Diagram of AlexNet](path/to/alexnet_diagram.png)

## Random Forest Algorithm

The Random Forest method combines multiple decision trees for classification. More trees in the forest lead to higher prediction accuracy.

![Flow Chart of Random Forest Algorithm](path/to/random_forest_flowchart.png)

## VGG16 Architecture

VGG16 uses convolutional layers with 3x3 filters and max-pooling layers for spatial pooling. It achieves high accuracy in facial recognition.

![Network Layers of VGG16 Architecture](path/to/vgg16_layers.png)

## Fingerprint Verification

Fingerprint sensors, like the R307 module, compare acquired images with saved data. Different methods like optical and capacitive scanning are employed for fingerprint recognition.

![R307 Fingerprint Sensor](path/to/r307_sensor.png)

## Arduino

Arduino boards, such as the ATmega328-based Uno, facilitate interactions with sensors and control of physical objects.

![ATmega328-based Arduino](path/to/arduino.png)

## Fingerprint Reader

Biometric sensors like the R307 Fingerprint Sensor use UART interfaces for communication and comparison of fingerprint data.

![R307 Fingerprint Scanner Interface](path/to/r307_interface.png)

## Power Supply Unit

Adapters convert electronic properties for different devices, ensuring compatibility and functionality.

![Digital Pins Description](path/to/pinout_diagram.png)

## Results and Discussion

The e-voting system employs CNNs for facial recognition and Random Forest for fingerprint verification. VGG-16 achieved the highest accuracy of 98.45%.

### Comparison of Algorithms

| Methods Used | Accuracy | Advantages |
|--------------|----------|------------|
| VGG16        | 98.45%   | Detects faces at different positions and has low processing time |
| AlexNet      | 94.16%   | Works with low-power portable devices |
| Random Forest Algorithm | 92% | Effective for recognizing faces at different angles |

![Comparison of Algorithms](path/to/algorithms_comparison.png)

The VGG-16 architecture showed the best results, providing a balance between accuracy and processing resources.

For more detailed implementation and code, refer to the GitHub repository's README.

