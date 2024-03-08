import openpyxl

def delete_series_from_excel_file(excel_file, series_name, device_type):
    """
    Deletes the specified series and its associated data from both the database and the Excel file.
    
    Args:
    - excel_file (ExcelFile): The existing ExcelFile object.
    - series_name (str): The name of the series to be deleted.
    - device_type (DeviceType): The device type associated with the series.
    """
    # Load the workbook in write mode
    wb = openpyxl.load_workbook(excel_file.file.path, read_only=False)

    # Access the specific worksheet corresponding to the device type
    sheet = wb[f"{device_type.device.name}-Series"]

    # Iterate through each row in the worksheet
    for idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
        # Check if the row corresponds to the specified device type and series name
        if row and row[0] and row[1] == series_name:
            # Delete the row from the worksheet
            sheet.delete_rows(idx)
            break

    # Save the changes to the Excel file
    wb.save(excel_file.file.path)

