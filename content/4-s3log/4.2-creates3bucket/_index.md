---
title : "Process and View Result"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

### Step 2: Process and View Result

After successfully uploading an image, proceed to process the image and verify the generated video output.

---

#### Instructions:

1. **Check the "EditTextList" Interface:**
   - This screen shows the OCR (text extracted from the uploaded image).
   - It also displays the translated text, typically into Vietnamese or another selected language.

2. **Create Video from Text:**
   - Click the **"Create Video"** button.
   - The system will process the text and generate a video.
   - The output video is saved in the `outputs/` folder inside your S3 bucket.

3. **View the Video:**
   - Open the **"Result"** interface to watch the video generated from the original image.

---



---

{{% notice tip %}}
If the video does not appear in the "Result" screen, check system logs or the processing status. Videos are saved under `S3 > outputs/` when successfully created.
{{% /notice %}}
