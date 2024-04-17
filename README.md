# Camera-Calibration

The program analyzes a video in `h264` format where there is a chessboard used for camera calibration. Grabs every set of frames to detect the biggest square grid. Once found it calculates the parameters to fix the camera distortion. 
Once found, these values are tested correcting the image distortion of some video frames. The distortion is fixed by applying 2 types of functions: `cv.undistor` & `cv.remap`

### Algorithm
![Flowchart Camera Calibration Algorithm](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/ac6751cb-89da-4728-b1e5-a32b8b1ffa30)



## Running the Programm
### Steps
1. Download the video from Drive (file too big to upload to github): https://drive.google.com/file/d/1Sa3bPw3b-QNIY8aqQYijV6o-tdyz2u8q/view?usp=sharing
2. Run `video2frames.py` to get the frames as .jpg images (The images are stored in `Frames New` folder)
3. Run `CameraCalibrationFinal.py`


## Results

![Figure_10](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/0083acaf-db63-4eec-a9b8-2718057b87e7)
![Figure_9](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/7f63d45e-3ee9-4fa2-a88a-bb290868f348)
![Figure_8](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/7f04f430-3880-4b47-bebc-a35dcee5e251)
![Figure_7](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/42fa4820-2753-442c-9429-e469a119bf7b)
![Figure_6](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/5d3288c4-9588-4e4b-88a4-2fcd86ecc685)
![Figure_5](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/d60ac2c3-7ed2-4281-a3f3-adc705ce77e8)
![Figure_4](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/5bc7e7fe-7167-4596-abde-ae56448d1f9a)
![Figure_3](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/7cbba9af-5eb8-4319-b331-98e8e5b4c80d)

![Figure_2](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/9d3df4bd-13c3-4905-a882-3852dffa1501)
![Figure_1](https://github.com/AlexysCR/Camera-Calibration/assets/111618122/2e8e12c7-74de-4d66-9977-e0b0a735c97a)



Check the following document to read more about the results: 
[Task 2 Report-Camera Calibration .pdf](https://github.com/AlexysCR/Camera-Calibration/files/15014495/Task.2.Report-Camera.Calibration.pdf)

**NOTE: This project is part of the "Computer Vision" class during my german exchange program.**
