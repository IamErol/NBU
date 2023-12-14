import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

from excel.services import validate_excel


def upload_files(request):
    """
    This function is used to upload two Excel files and merge them into one.
    To merge the files, concat function is used.
    :param request:
    :return: downloadable file.
    """
    if request.method == 'POST':
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']
        # Validate if the files are xlsx files.
        if not validate_excel((file1, file2), 'xlsx'):
            return HttpResponse('File is not a xlsx file.')

        try:  # Read the files.
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
        except Exception as e:
            return HttpResponse(e)
        # Merging two files into one using concat function.
        merged_df = pd.concat([df1, df2])
        merged_df = merged_df.dropna(how='all')
        merged_df.to_excel('static/merged_file.xlsx', index=False)
        return render(request, 'success.html', {'filename': 'merged_file.xlsx'})
    return render(request, 'upload.html')
