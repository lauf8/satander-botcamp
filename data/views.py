from django.shortcuts import redirect, render
import pandas as pd
from .models import Sport, Athletes, Nacionality

def home(request):
    return render(request, 'home/index.html')

    #return render(request, "viagem/show.html", {"viagem": viagem})

def read_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file, sheet_name='Athletes', header=2 )
            #sheet_name seria a aba do csv, e o header é onde começa os dados do cabeçalho
            df = df.dropna()
            for index,row in df.iterrows(): #for para percorrer as linhas dp excel
                name = row['Name']
                name_checker = Athletes.objects.filter(name=name)
                if name_checker is not None: # verifica se o atleta foi inserido, se foi skipa a linha
                    continue 
                
                #essa verificação não é uma boa pratica pois podem existir atletas
                # com o mesmo nome, para essa verificação ser correta deveria ser um id unico,
                # mas para esse este exeplo de uma um etl, isso serve por hora
                       
                sport = row['Sport']
                nationality = row['Nacionality']
                age = row['Age']
                kg = row['Wt kg']
                ht = row['Ht']
                
                if kg is None or ht is None: # Essa condicional faz com que o valores que forem vazios não vão ser salvos
                    continue
                else:
                    sport_checker = Sport.objects.filter(sport=sport)
                    if sport_checker is None:
                        new_sport = Sport()
                        new_sport.sport = sport
                        new_sport.save()
                        sport_save = new_sport
                        
                        #cria um novo esporte e salva ele
                    else:
                        sport_save = sport_checker
                    
                    nacionality_checker = Nacionality.objects.filter(nationality=nationality)
                    if nacionality_checker is None:
                        new_nacionality = Nacionality()
                        new_nacionality.nacionality = nationality
                        new_nacionality.save()
                        nacionality_save = new_nacionality
                    else:
                        nacionality_save = nacionality_checker
                    
                    athlete_save = Athletes()
                    athlete_save.name = name
                    athlete_save.age = age
                    athlete_save.kg = kg
                    athlete_save.ht = ht
                    athlete_save.sport = sport_save
                    athlete_save.nacionality = nacionality_save
                    athlete_save.save()
                    count = count + 1
                    #contador para retorna quantas linhas foram inseridas
                    
            return redirect('return_excel')        

                    
                    
    return render(request, 'excel/excel.html', context= {'count': 'count'})


def return_excel(request):
    return render(request, 'excel/return.html')

def atlhets_index(request):
    athletes = Athletes.objects.all()
    context = {
        'athletes' : athletes
    }
    return render(request, 'excel/return.html', context)