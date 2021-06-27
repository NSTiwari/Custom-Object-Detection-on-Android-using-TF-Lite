# Custom-Object-Detection-on-Android-using-TF-Lite
An end-to-end tutorial to train a custom object detection model and deploy it on Android using TensorFlow Lite.


## Steps:

1. Clone the repository on your local machine.
 
2. Sign in to your Google account and upload the `Custom_Object_Detection_using_TF_Lite_Model_Maker.ipynb` notebook on Colab.

3. Run the notebook cells one-by-one by following the instructions.

4. Once the TF Lite model is downloaded, copy the `model.tflite` model file inside `Custom-Object-Detection-on-Android-using-TF-Lite/Android_App/app/src/main/assets` directory.

5. Open the project in Android Studio and let it build itself for some time.

6. Open `MainActivity.kt` file and edit **Line 130** by replacing `<your_model.tflite>` with the name of your actual TF Lite model.

7. Build the project and install it on your phone. Enjoy your own custom-built object detector app.



## Output:

![GitHub Logo](Output.gif)



