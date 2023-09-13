from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request, 'home/index.html')

    #return render(request, "viagem/show.html", {"viagem": viagem})

def read_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file, header=3 )
            df = df.dropna()
            for index,row in df.iterrows():
                periodo = row['Período']    
    return render(request, 'excel/excel.html')