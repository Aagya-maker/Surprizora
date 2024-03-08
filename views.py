from django.shortcuts import render, redirect
from .forms import QuestionnaireForm

def home(request):
    return render(request, 'home.html')

def bubble_bath_gifts(request):
    return render(request, 'bubble_bath_gifts.html')
def curling_up_gifts(request):
    return render (request, 'curling_up_gifts.html')
def walk_run_gifts(request):
    return render(request, 'walk_run_gifts.html')
def meditation_gifts(request):
    return render(request, 'meditation_gifts.html')
def cooking_meals_gifts(request):
    return render(request,'cooking_meals_gifts.html')
def exercise_gifts(request):
    return render(request, 'exercise_gifts.html')
def chocolate_gifts(request):
    return render(request, 'chocolate_gifts.html')
def romantic_movies_gifts(request):
    return render(request, 'romantic_movies_gifts.html')
def video_games_gifts (request):
    return render(request, 'video_games_gifts.html')
def cartoons_gifts (request):
    return render(request, 'cartoons_gifts.html')
def riding_bikes_gifts(request):
    return render (request, 'riding_bikes_gifts.html')
def creating_arts_gifts (request):
    return render (request, 'creating_arts_gifts.html')
def pop_music_gifts (request):
    return render (request, 'pop_music_gifts.html')
def rock_music_gifts (request):
    return render (request, 'rock_music_gifts.html')
def hip_hop_music_gifts (request):
    return render (request, 'hip_hop_music_gifts.html')
def jazz_music_gifts (request):
    return render (request, 'jazz_music_gifts.html')
def indie_alternative_gifts (request):
    return render (request, 'indie_alternative_gifts.html')
def aries_gifts(request):
    return render(request, 'aries_gifts.html')
def taurus_gifts(request):
    return render(request, 'taurus_gifts.html')
def gemini_gifts(request):
    return render(request, 'gemini_gifts.html')
def cancer_gifts(request):
    return render(request, 'cancer_gifts.html')
def leo_gifts(request):
    return render(request, 'leo_gifts.html')
def virgo_gifts(request):
    return render(request, 'virgo_gifts.html')
def scorpio_gifts(request):
    return render(request, 'scorpio_gifts.html')
def sagittarius_gifts(request):
    return render(request, 'sagittarius_gifts.html'),
def capricorn_gifts(request):
    return render(request, 'capricorn_gifts.html')



def submit (request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            unwind = form.cleaned_data['unwind']
            
            if unwind == 'bubble-bath':
                return redirect('bubble_bath_gifts')
            elif unwind == 'curling-up':
                return redirect('curling_up_gifts')
            elif unwind == 'walk-run':
                return redirect('walk_run_gifts')
            elif unwind == 'meditation':
                return redirect ('meditation_gifts')
            elif unwind == 'cooking-meal':
                return redirect ('cooking_meals_gifts')
            elif unwind == 'exercise':
                return redirect('exercise_gifts')
            
        
            secret_like = form.cleaned_data['secret_like']
            if secret_like == 'chocolate':
                return redirect('chocolate_gifts')
            elif secret_like == 'romantic-movies':
                return redirect('romantic_movies_gifts')
            elif secret_like == 'video-games':
                return redirect('video_games_gifts')
            elif secret_like == 'cartoons':
                return redirect(cartoons_gifts)
            
            childhood_activity = form.cleaned_data['childhood_activity']
            if childhood_activity == 'riding-bikes':
                return redirect ('riding_bikes_gifts')
            elif childhood_activity == 'creating-arts':
                return redirect ('creating_arts_gifts')
            
            genre=form.cleaned_data['genre']
            if genre == 'pop':
                return redirect('pop_music_gifts')
            elif genre == 'rock':
                return redirect('rock_music_gifts')
            elif genre == 'hip-hop':
                return redirect('hip_hop_music_gifts')
            elif genre == 'jazz':
                return redirect('jazz_music_gifts')
            elif genre == 'indie-alternative':
                return redirect ('indie_alternative_gifts')
            
            zodiac=form.cleaned_data['zodiac']
            if zodiac == 'aries':
                return redirect('aries_gifts')
            elif zodiac == 'taurus':
                return redirect('taurus_gifts')
            elif zodiac == 'gemini':
                return redirect('gemini_gifts')
            elif zodiac == 'cancer':
                return redirect('cancer_gifts')
            elif zodiac == 'leo':
                return redirect('leo_gifts')
            elif zodiac == 'virgo':
                return redirect('virgo_gifts')
            elif zodiac == 'scorpio':
                return redirect('scorpio_gifts')
            elif zodiac == 'sagittarius':
                return redirect('sagittarius_gifts')
            elif zodiac == 'capricorn':
                return redirect('capricorn_gifts')
            
            


            
                
            
    return redirect('home')
def questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm (request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            hobby = form.cleaned_data['hobby']
            unwind = form.cleaned_data['unwind']
            secret_like = form.cleaned_data['secret_like']
            childhood_activity = form.cleaned_data ['childhood_activity']
            genre = form.cleaned_data ['genre']
            zodiac = form.cleaned_data ['zodiac']
            food_type = form.cleaned_data['food_type']
            stay_active = form.cleaned_data['stay_active']
            new_skill = form.cleaned_data['new_skill']
            movie_tv_show = form.cleaned_data['movie_tv_show_']
            express_creativity = form.cleaned_data['express_creativity']
            comfort_food = form.cleaned_data['comfort_food']
            board_game = form.cleaned_data['board_game']
            weekend_getaway = form.cleaned_data['weekend_getaway']
            color = form.cleaned_data['color']
            fashion_style = form.cleaned_data['fashion_style']
            accessories = form.cleaned_data['accessories']
            gadgets = form.cleaned_data['gadgets']
            fitness_goals = form.cleaned_data ['fitness_goals']
            scent = form.cleaned_data ['scent']
            home_decor = form.cleaned_data ['home_decor']
            beverage = form.cleaned_data ['beverage']
            profession = form.cleaned_data ['profession']
            sports = form.cleaned_data ['sports']
            pets = form.cleaned_data ['pets']

           



            if hobby == 'reading' :
                return redirect('reading_gifts')
            elif hobby == 'sports' :
                return redirect ('sports_gifts')
            elif hobby == 'music' :
                return redirect ('music_gifts')
            elif hobby == 'art' :
                return redirect ('art_gifts')
            elif hobby == 'others':
                return redirect ('others_gifts')
            
            if unwind == 'bubble-bath': 
                return redirect ('bubble_bath_gifts')  
            elif unwind == 'curling-up' :
                return redirect ('curling_up_gifts')
            elif unwind == 'walk-run' :
                return redirect ('walk_run_gifts')
            elif unwind == 'meditation' :
                return redirect ('meditation_gifts')
            elif unwind == 'cooking-meal' :
                return redirect ('cooking_meals_gifts')
            elif unwind == 'exercise' :
                return redirect ('exercise_gifts')
            
            if secret_like == 'chocolate' :
                 return redirect ('chocolate_gifts')
            elif secret_like == 'romantic-movies':
                return redirect ('romantic_movies_gifts')
            elif secret_like == 'video-games' :
                return redirect ('video_games_gifts')
            elif secret_like == 'cartoons' :
                return redirect ('cartoons_gifts')
            
            if childhood_activity == 'riding-bikes':
                return redirect ('riding_bikes_gifts')
            elif childhood_activity == 'exploring-imaginative-worlds' :
                return redirect ('imaginative_worlds_gifts')
            elif childhood_activity == 'creating-arts' :
                return redirect == ('creating_arts_gifts')
            
            if genre == 'pop' :
                return redirect ('pop_music_gifts')
            elif genre == 'rock' :
                return redirect ('rock_music_gifts')
            elif genre == 'hip-hop' :
                return redirect ('hip_hop_music_gifts')
            elif genre == 'jazz' :
                return redirect ('jazz_music_gifts')
            elif genre == 'indie-alternative' :
                return redirect ('indie_alternative_gifts')
            
            if zodiac == 'aries' :
                return redirect ('aries_gifts')
            elif zodiac == 'taurus' :
                return redirect ('taurus_gifts')
            elif zodiac == 'gemini' :
                return redirect ('gemini_gifts')
            elif zodiac == 'cancer' :
                return redirect ('cancer_gifts')
            elif zodiac == 'leo' :
                return redirect ('leo_gifts')
            elif zodiac == 'virgo' :
                return redirect ('virgo_gifts')
            elif zodiac == 'scorpio' :
                return redirect ('scorpio_gifts')
            elif zodiac == 'sagittarius' :
                return redirect ('sagittarius_gifts')
            elif zodiac == 'capricorn' :
                return redirect ('capricorn_gifts')
            elif zodiac == 'aquarius' :
                return redirect ('aquarius_gifts')
            elif zodiac == 'pisces' :
                return redirect ('pisces_gifts')
            
            if food_type == 'spicy' :
                return redirect ('spicy-food_gifts')
            elif food_type == 'sweet' :
                return redirect ('sweet-food_gifts')
            elif food_type == 'savoury' :
                return redirect ('savoury-food_gifts')
            elif food_type == 'comfort' :
                return redirect ('comfort_food_gifts')
            elif food_type == 'healthy' :
                return redirect ('healthy_food_gifts')
            elif food_type == 'dessert' :
                return redirect ('dessert_gifts')
            
            
            if stay_active == 'running' :
                return redirect ('running_gifts')
            elif stay_active == 'dancing' :
                return redirect ('dancing_gifts')
            elif stay_active == 'weightlifting' :
                return redirect ('weightlifting_gifts')
            elif stay_active == 'swimming' :
                return redirect ('swimming_gifts')
            elif stay_active == 'team-sports' :
                return redirect ('team_sports_gifts')
            
            if new_skill == 'cooking' :
                return redirect ('cooking_gifts')
            elif new_skill == 'painting' :
                return redirect ('painting_gifts') 
            elif new_skill == 'language' :
                return redirect ('language_gifts')
            elif new_skill == 'musical-instrument':
                return redirect == ('musical_instrument_gifts')
            elif new_skill == 'coding' :
                return redirect == ('coding_gifts')
            
            if movie_tv_show == 'action' :
                return redirect == ('action_movie_tv_show_gifts')
            elif movie_tv_show == 'comedy' :
                return redirect == ('comedy_movie_tv_show_gifts')
            elif movie_tv_show == 'drama' :
                return redirect == ('drama_movie_tv_show_gifts')
            elif movie_tv_show == 'sci-fi' :
                return redirect == ('sci_fi_movie_tv_show_gifts')
            elif movie_tv_show == 'documentary':
                return redirect == ('documentary_gifts')
            elif movie_tv_show == 'animated' :
                return redirect == ('animated_movie_tv_show_gifts')
            
            if express_creativity == 'painting' :
                return redirect == ('painting_gifts')
            elif express_creativity == 'writing' :
                return redirect == ('writing_gifts')
            elif express_creativity == 'crafting' :
                return redirect == ('crafting_gifts')
            elif express_creativity == 'musical_instrument' :
                return redirect == ('musical_instrument_gifts')
            elif express_creativity == 'cooking' :
                return redirect == ('cooking_gifts')
            elif express_creativity == 'designing' :
                return redirect == ('designing_gifts')
            
            if comfort_food == 'crusty-bread':
                return redirect == ('crusty_bread_gifts')
            elif comfort_food == 'macaroni' :
                return redirect == ('macaroni_gifts')
            elif comfort_food == 'mashed-potatoes':
                return redirect == ('mashed_potatoes_gifts')
            elif comfort_food == 'ramen' :
                return redirect == ('ramen_gifts')
            elif comfort_food == 'chocolate-chip' :
                return redirect == ('chocolate_gifts') 
            elif comfort_food == 'grilled-cheese-sandwich' :
                return redirect == ('grilled_cheese_sandwich_gifts')
            

            if board_game == 'settles' :
                return redirect == ('settles_gifts')
            elif board_game == 'ticket-to-ride' :
                return redirect == ('ticket_to_ride_gifts')
            elif board_game == 'scrabble' :
                return redirect == ('scrabble_gifts')
            elif board_game == 'codenames' :
                return redirect == ('codenames_gifts')
            elif board_game == 'pandemic' :
                return redirect == ('pandemic_gifts')
            elif board_game == 'chess-or-checkers' :
                return redirect == ('chess_or_checkers_gifts')
            
            if weekend_getaway == 'relaxing-cabin' :
                return redirect == ('relaxing_cabin_gifts')
            elif weekend_getaway == 'exploring-city' :
                return redirect == ('exploring_city_gifts')
            elif weekend_getaway == 'lounging-beach' :
                return redirect == ('lounging_beach_gifts')
            elif weekend_getaway == 'hiking-camping-trip' :
                return redirect == ('hiking_camping_gifts')
            elif weekend_getaway == 'spa-retreat' :
                return redirect == ('spa_retreat_gifts')
            elif weekend_getaway == 'landmarks-musuems' :
                return redirect == ('landmarks_musuems_gifts')
            
            if color == 'red' :
                return redirect == ('red_color_gifts')
            elif color == 'green' :
                return redirect == ('green_color_gifts')
            elif color == 'blue' :
                return redirect == ('blue_color_gifts')
            elif color == 'yellow' :
                return redirect == ('yellow_color_gifts')
            elif color == 'pink' :
                return redirect == ('pink_color_gifts')
            elif color == 'purple':
                return redirect == ('purple_color_gifts')
            elif color == 'orange' :
                return redirect == ('orange_color_gifts')
            
            if fashion_style == 'casual' :
                return redirect == ('casual_wear_gifts')
            elif fashion_style == 'classic' :
                return redirect == ('classic_wear_gifts')
            elif fashion_style == 'bohemian' :
                return redirect == ('bohemian_wear_gifts')
            elif fashion_style == 'trendy':
                return redirect == ('trendy_wear_gifts')
            elif fashion_style == 'sporty' :
                return redirect == ('sport_wear_gifts')
            elif fashion_style == 'elegant' :
                return redirect == ('elegant_wear_gifts')
            elif fashion_style == 'vintage' :
                return redirect == ('vintage_wear_gifts')
            
            if accessories == 'jewelry' :
                return redirect == ('jewelry_gifts')
            elif accessories == 'watches' :
                return redirect == ('watches_gifts')
            elif accessories == 'scarves' :
                return redirect == ('scarves_gifts')
            elif accessories == 'sunglasses' :
                return redirect == ('sunglasses_gifts')
            elif accessories == 'handbags':
                return redirect == ('handbags_gifts')
            elif accessories == 'hats' :
                return redirect == ('hats_gifts')
            elif accessories == 'caps':
                return redirect == ('caps_gifts')
            elif accessories == 'belts':
                return redirect == ('belts_gifts')
            
            if gadgets == 'smartphones' :
                return redirect == ('smartphones_gifts')
            elif gadgets == 'laptops':
                return redirect == ('laptops_gifts')
            elif gadgets == 'smartwatches-fitnesstracker' :
                return redirect == ('smartwatches_fitnesstracker_gifts')
            elif gadgets == 'cameras' :
                return redirect == ('cameras_gifts')
            elif gadgets == 'gaming-consoles':
                return redirect == ('gaming_consoles_gifts')
            elif gadgets == 'audio-devices' :
                return redirect == ('audio_devices_gifts')
            
            if fitness_goals == 'weight-loss':
                return redirect == ('weight_loss_gifts')
            elif fitness_goals == 'muscle-gain' :
                return redirect == ('muscle_gain_gifts')
            elif fitness_goals == 'cardio' :
                return redirect == ('cardio_gifts')
            elif fitness_goals == 'flexibility-yoga' :
                return redirect == ('flexibility_gifts')
            elif fitness_goals == 'sports-performance' :
                return redirect == ('sports_performance_gifts')
            
            if scent == 'floral' :
                return redirect == ('floral_scent_gifts')
            elif scent == 'woody' :
                return redirect == ('woody_scent_gifts')
            elif scent == 'citrus' :
                return redirect == ('citrus_scent_gifts')
            elif scent == 'fresh-aquatic' :
                return redirect == ('fresh_aquatic_scents')
            elif scent == 'spicy' :
                return redirect == ('spicy_scent_gifts')
            elif scent == 'oriental' :
                return redirect == ('oriential_scent_gifts')
            
            if home_decor == 'minimalist' :
                return redirect == ('minimalist_home_decor_gifts')
            elif home_decor == 'vintage-retro':
                return redirect == ('vintage_retro_home_decor_gifts')
            elif home_decor == 'modern-contemporary' :
                return redirect == ('modern_contemporary_home_decor_gifts')
            elif home_decor == 'bohemian' :
                return redirect == ('bohemian_home_decor_gifts')
            elif home_decor == 'scandinavian' :
                return redirect == ('scandinavian_home_decor_gifts')
            elif home_decor == 'industrial':
                return redirect == ('industrial_home_decor_gifts')
            elif home_decor == 'farmhouse':
                return redirect == ('farmhouse_home_decor_gifts')
            
            if beverage == 'coffee' :
                return redirect == ('coffee_gifts')
            elif beverage == 'tea' :
                return redirect == ('tea_gifts')
            elif beverage == 'soft-drinks':
                return redirect == ('soft_drinks_gifts')
            elif beverage == 'juice' :
                return redirect == ('juice_gifts')
            elif beverage == 'beer' :
                return redirect == ('beer_gifts')
            elif beverage == 'wine' :
                return redirect == ('wine_gifts')
            elif beverage == 'cocktails' :
                return redirect == ('cocktails_gifts')
            
            if profession == 'technology-it' :
                return redirect == ('information_technology_gifts')
            elif profession == 'healthcare-medicine':
                return redirect == ('healthcare_medincine_gifts')
            elif profession == 'education' :
                return redirect == ('education_gifts')
            elif profession == 'finance' :
                return redirect == ('finance_gifts')
            elif profession == 'creative' :
                return redirect == ('creative_arts_profession_gifts')
            elif profession == 'business':
                return redirect == ('business_gifts')
            elif profession == 'hospitality':
                return redirect == ('hospitality_gifts')
            
            if sports == 'football' :
                return redirect == ('football_gifts')
            elif sports == 'basketball':
                return redirect == ('basketball_gifts')
            elif sports == 'baseball' :
                return redirect == ('baseball_gifts')
            elif sports == 'tennis' :
                return redirect == ('tennis_gifts')
            elif sports == 'golf':
                return redirect == ('golf_gifts')
            elif sports == 'ping-pong':
                return redirect == ('ping_pong_gifts')
            elif sports == 'rugby':
                return redirect == ('rugby_gifts')
            elif sports == 'hockey':
                return redirect == ('hockey_gifts')
            
            if pets == 'dogs' :
                return redirect == ('dog_gifts')
            elif pets == 'cats' :
                return redirect == ('cat_gifts')
            elif pets == 'birds' :
                return redirect == ('bird_gifts')
            elif pets == 'fish':
                return redirect == ('fish_gifts')
            elif pets == 'reptiles' :
                return redirect == ('reptile_gifts')
            elif pets == 'small-mammals':
                return redirect == ('small_mammals_gifts')
            

            return redirect ('submit')
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire.html', {'form': form})

    
            

            

            
                

            




            
            
        
            
            
                    
                

   
