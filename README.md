<!-- Header -->
<h1 align="center">
  <span style="color: #ff5733;">Excel Parser</span>
</h1>

<!-- Description -->
<p align="center">
  <strong>An API for Pars the excel files</strong>
</p>

<details open>
  <summary><strong>Table of Contents</strong></summary>
  <ul>
    <li><a href="#Note">Note</a></li>
    <li><a href="#Prerequisites">Prerequisites</a></li>
    <li><a href="#Overview">Overview</a></li>
    <li><a href="#Author&Maintainer">Author&Maintainer</a></li>
    <li><a href="#license">License</a></li>
  </ul>
</details>
<h2 style="color: #33aaff;">Note</h2>


<p>
  <strong>While working on the task, I encountered various challenges. The provided 'requirements' lacked clarity, and the 'sample' for testing presented several issues. Unfortunately, the instructions regarding the task were not effectively communicated, making it challenging to fully grasp the expectations. Despite these obstacles, I took the initiative to interpret the task requirements based on my understanding and expertise. My goal was to deliver a solution that aligns with the intended objectives, despite the initial lack of clarity in the specifications. I firmly believe that through addressing these challenges and leveraging my skills, I have developed a solution that captures the essence of the task. Should there be any specific details or requirements that I might have overlooked, I am more than willing to make the necessary adjustments. Thank you for your understanding and cooperation.</strong>
</p>

<h2 style="color: #33aaff;">Prerequisites</h2>
<p>
    Before proceeding, please ensure that you have reviewed the following documentation located in the "document" folder:
    <strong>
    - 1.env.md
    - 2.installation.md
    - 3.build.md
    </strong>
</p>
<h2 style="color: #33aaff;">Overview</h2>
<p>This API facilitates users in uploading Excel files, extracting data from them, and storing it in a tree format. Additionally, it offers functionalities to delete series both in the Excel files and the associated database, as well as updating them.</p>
<p>Here's a breakdown of the main features:</p>
<ul>
  <li><strong>Excel File Upload:</strong> Users can upload Excel files containing data.</li>
  <li><strong>Data Extraction:</strong> The API extracts relevant data from the uploaded Excel files.</li>
  <li><strong>Tree Representation:</strong> Extracted data is presented in a tree format for better visualization.</li>
  <li><strong>Series Deletion:</strong> Users can delete series from both the Excel files and the database.</li>
  <li><strong>Series Update:</strong> Functionality is provided to update existing series.</li>
</ul>
<p>This API streamlines the process of handling Excel data, offering comprehensive tools for managing and manipulating data effectively.</p>


## Endpoints

### 1. excel_files

- **Endpoint:** `/files/excel_files/`
- **Method:** 
  - GET
  - POST
- **Permissions:**
  - AllowAny
- **Description:** This endpoint allows users to upload and retrieve Excel files.
- **Request Body:**
  - `file` (file): The Excel file to be uploaded.

#### Response

- **Ok (Status 200 Ok):** 
  - Returns all Excel files with pagination or individual Excel file.

- **Error (Status 400 Bad Request):**
  - DETAIL: if user send POST request
    - If a user sends a POST request with a file larger than 50 megabytes.
    - If a user sends a bad Excel file.
    - If a user sends a file that is not an Excel file.




### 2. Excel Hierarchical data

- **Endpoint:** `files/excel_files/id/hierarchical_data/`
- **Method:** 
  - GET
- **Permissions:**
  - AllowAny
- **Description:** This endpoint retrieves hierarchical data from an individual Excel file.

#### Response


- **Success (Status 200 OK):**
  - Returns all data from the Excel file.
  
- **NotFound (Status 404 NotFound):** 
  - Indicates that the Excel file does not exist.


### 3. Excel Delete Series and Associated Values

- **Endpoint:** `files/excel_files/1/delete-series/`
- **Method:** 
  - POST
- **Permissions:**
  - AllowAny
- **Description:** This endpoint deletes series and associated values from an Excel file.
- **Request Body:**
  - `series_name` (char): The name of the series of a device type.
  - `device_type` (char): The type of device.
  - `device_type_id` (char): The ID of the device type.

#### Response

- **Success (Status 204 No Content):**
  - Indicates that the series and associated data have been deleted.


- **Not Found (Status 404 Not Found):** 
  - Indicates that the series or device type does not exist.

- **Error (Status 400 Bad Request):**
  - If the user sends incomplete or incorrect data.




### 4. Excel Update Series Value

- **Endpoint:** `files/excel_files/id/update-series-value/`
- **Method:** 
  - PUT
- **Permissions:**
  - AllowAny
- **Description:** This endpoint updates series values or adds new values for a series.

- **Request Body:**
  - `status` (string): Can be 'add' or 'change'.
  - `series_name` (char): The name of the series of a device type.
  - `device_type` (char): The type of device.
  - `device_type_id` (char): The ID of the device type.
  - `value` (string): The value to be updated or added.



#### Response

- **Success (Status 200 OK):**
  - Indicates that the series has been updated or the value has been added.

- **Error (Status 400 Bad Request):**
  - DETAIL: if user send POST request
    - If the user sends incomplete or incorrect data.

- **Not Found (Status 404 Not Found):** 
  - Indicates that the series or device type does not exist.


## How to Use

1. Use the `/files/excel_files/` endpoint to upload and retrieve Excel files.
2. Use the `/files/excel_files/id/hierarchical_data/` endpoint to retrieve hierarchical data from an individual Excel file.
3. Use the `/files/excel_files/id/delete-series/` endpoint to delete series and associated values.
4. Use the `/files/excel_files/id/update-series-value/` endpoint to update series values or add new values for a series.

Make sure to handle errors as described in the API documentation.

<h2 style="color: #33aaff;">Author&Maintainer</h2>
<h3 align="center">
    <p>ARYAN NIKNEZHAD</p>
  <img src="https://avatars.githubusercontent.com/u/127540182?s=400&u=550a6cfe2bde09d01b7b47ca140339c3ab38239b&v=4" alt="picture">
</h3>
<!-- License -->
<h2 style="color: #33aaff;">License</h2>
<p>This project is licensed under the 'ARYAN NIKNEZHAD'.</p>