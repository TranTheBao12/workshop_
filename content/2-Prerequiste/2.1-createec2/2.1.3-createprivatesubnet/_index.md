---
title : "Add vie.traineddata to tessdata"
date : "2025-05-28"
weight : 3
chapter : false
pre : " <b> 2.1.3 </b> "
---

#### Add `vie.traineddata` to `tessdata` Directory

In this step, we will download and add the Vietnamese language data file `vie.traineddata` into the `tessdata` directory in your project. This is required if you plan to use Tesseract OCR for recognizing Vietnamese text.

---

### 1. Download `vie.traineddata`

Go to the official Tesseract OCR language data GitHub repository:

- [https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata)

Locate the file `vie.traineddata` and click **Download**.

Alternatively, use this direct link to download:  
[Download vie.traineddata](https://github.com/tesseract-ocr/tessdata/raw/main/vie.traineddata)

---

### 2. Create `tessdata` Directory in Your Project

1. In Visual Studio, right-click on the root of your project.
2. Choose **Add → New Folder** and name it `tessdata`.
3. Right-click on `tessdata` → **Add → Existing Item**.
4. Select the downloaded `vie.traineddata` file and click **Add**.

> 📌 Make sure the `Copy to Output Directory` property of `vie.traineddata` is set to **Copy if newer** or **Copy always**.

---

### 3. Verify Directory Structure

Your project directory should now look like:
![AWS Explorer](/images/2.prerequisite/anh5.png)
