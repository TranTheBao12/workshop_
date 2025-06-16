---
title : "Introduction"
date :  "2025-05-28"
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

### Introduction 

- **Objective**: Introduce the project and AWS services.

- **Content**:

  - **ImageToVideoWeb Project**:  
    - An ASP.NET Core web application that allows uploading images, extracting text (OCR), translating text (Google Translate), generating speech (Google TTS), and creating videos (FFmpeg).  
    - Uses Amazon S3 for file storage and Elastic Beanstalk for deployment.

  - **Amazon S3**:  
    - Stores input images in the `uploads/` folder.  
    - Stores temporary text and audio files in the `temp/` folder.  
    - Stores final output videos in the `outputs/` folder.

  - **Architecture Overview**:  
    - Frontend calls controller → Uploads image to S3 → Local processing (OCR, translation, TTS, video creation) → Saves video to S3 → Displays video from S3.

  