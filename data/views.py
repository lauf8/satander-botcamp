from django.shortcuts import redirect, render, get_object_or_404
import pandas as pd
from .models import Sport, Athletes, Nationality

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
                if name_checker is None: # verifica se o atleta foi inserido, se foi skipa a linha
                    continue 
                
                #essa verificação não é uma boa pratica pois podem existir atletas
                # com o mesmo nome, para essa verificação ser correta deveria ser um id unico,
                # mas para esse este exeplo de uma um etl, isso serve por hora
                       
                sport = row['Sport']
                nationality = row['Nationality']
                age = row['Age']
                kg = row['Wt kg']
                ht = row['Ht']
                
                if kg is None or ht is None: # Essa condicional faz com que o valores que forem vazios não vão ser salvos
                    continue
                else:
                    sport_checker = Sport.objects.filter(sport=sport).first()
                    if sport_checker is None:
                        new_sport = Sport()
                        new_sport.sport = sport
                        new_sport.save()
                        sport_save = new_sport
                        
                        #cria um novo esporte e salva ele
                    else:
                        sport_save = sport_checker
                    
                    nationality_checker = Nationality.objects.filter(nationality=nationality).first()
                    if nationality_checker is None:
                        new_nationality = Nationality()
                        new_nationality.nationality = nationality
                        new_nationality.save()
                        nationality_save = new_nationality
                        
                    else:
                        nationality_save = nationality_checker
                    
                    athlete_save = Athletes()
                    athlete_save.name = name
                    athlete_save.age = age
                    athlete_save.kg = kg
                    athlete_save.ht = ht
                    sport = get_object_or_404(Sport, pk = sport_save.pk)
                    nationality = get_object_or_404(Nationality,pk = nationality_save.pk)
                    athlete_save.sport = sport
                    athlete_save.nationality = nationality
                    athlete_save.save()
                    #contador para retorna quantas linhas foram inseridas
                    
           

                    
                    
    return render(request, 'excel/excel.html')


def return_excel(request):
    return render(request, 'excel/return.html')

def athlete_index(request):
    athletes = Athletes.objects.all()
    context = {
        'athletes' : athletes
    }
    return render(request, 'athlete/index.html', context)

def sport_index(request):
    sports = Sport.objects.all()
    context = {
        'sports' : sports
    }
    return render(request, 'sport/index.html', context)

def sport_detail(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    athletes = Athletes.objects.filter(sport=sport).all()
    count_athletes = len(athletes)
    set_nationality = set()
    ages = []
    weigth = []
    for athlete in athletes:
        set_nationality.add(athlete.nationality)
        ages.append(athlete.age)
        weigth.append(athlete.kg)
    
    avg_age = sum(ages)/len(ages)
    avg_weigth = sum(weigth)/len(weigth)
    
    avg_age = round(avg_age, 2)
    avg_weigth = round(avg_weigth,2)
    list_nationality =  list(set_nationality)
    count_nationality = len(list_nationality)
        
    context = {
        
        'count_athletes': count_athletes,
        'avg_age': avg_age,
        'avg_weigth': avg_weigth,
        'count_nationality': count_nationality,
        'sport' : sport,
        'athletes' : athletes,
    }
    
    print(context)
    return render(request, 'sport/detail.html', context)