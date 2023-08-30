# Biometric Identification
A process for biometric identification using iris and fingerprint features fusion. Features are extracted using Discrete Cosine Transform (DCT) with 8X8, 16X16 and 4X4 block size. The features are stored using [Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).

## Steps
* Read the images of fingerprints from fp folder stored in data folder and stored in list. (we have used list as a data structure for storing data)
* Read the images of iris from iris folder stored in data folder and stored in list
* Call feature extraction method by passing fingerprint and iris list
* It will return the fusion of fp and iris
* Call generate shares method by passing fusion vector
* Return two shares which is stored in shares list
* Take the test images for matching process
* Apply the feature extraction process and get the fusion vector
* Recover the fusion vector by calling recover method and passing two shares
* Mathing using MSE and SD, for this call matching and pass recovered feature vector and test feature vector
* If matched we count the no of matches using MSE and SD
* Calculate the GRR and FRR from count
Same process goesfor 4x4 and 16x16 just call feature extraction 4x4 and feature extraction 16x16 method.
