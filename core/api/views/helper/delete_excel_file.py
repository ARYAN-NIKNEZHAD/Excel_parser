from django.core.files.storage import default_storage

def delete_excel(excel_file):
    """
    Deletes the specified Excel file.

    Args:
        excel_file (ExcelFile): The Excel file object to delete.
    """
    # Get the path to the file
    file_path = excel_file.file.path
    
    # Delete the file from the storage
    default_storage.delete(file_path)
    
    # Delete the ExcelFile object from the database
    excel_file.delete()