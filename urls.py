from django.urls import path
from .views import home, questionnaire, submit, bubble_bath_gifts, curling_up_gifts, walk_run_gifts, meditation_gifts, cooking_meals_gifts, exercise_gifts, chocolate_gifts, romantic_movies_gifts, video_games_gifts, cartoons_gifts, riding_bikes_gifts, creating_arts_gifts, pop_music_gifts, rock_music_gifts, hip_hop_music_gifts, jazz_music_gifts, indie_alternative_gifts, aries_gifts, taurus_gifts, gemini_gifts, cancer_gifts,leo_gifts, virgo_gifts, scorpio_gifts, sagittarius_gifts, capricorn_gifts

urlpatterns=[
    path('', home, name='home'),
    path ('questionnaire/', questionnaire, name = 'questionnaire'),
	path ('bubble_bath_gifts/', bubble_bath_gifts, name='bubble_bath_gifts'),
	path ('curling_up_gifts/', curling_up_gifts, name='curling_up_gifts'),
	path ('walk_run_gifts/', walk_run_gifts, name='walk_run_gifts'),
	path ('meditation_gifts/', meditation_gifts, name='meditation_gifts'),
	path ('cooking_meals_gifts/', cooking_meals_gifts, name='cooking_meals_gifts'),
	path ('exercise_gifts/',  exercise_gifts, name = 'exercise_gifts'),
	path ('chocolate_gifts/', chocolate_gifts, name='chocolate_gifts'),
	path ('romantic_movies_gifts/', romantic_movies_gifts, name='romantic_movies_gifts'),
	path ('video_games_gifts/', video_games_gifts, name='video_games_gifts'), 
	path ('cartoons_gifts/', cartoons_gifts, name='cartoons_gifts'),
	path ('riding_bikes_gifts/', riding_bikes_gifts, name='riding_bikes_gifts'),
	path ('creating_arts_gifts/', creating_arts_gifts, name='creating_arts_gifts'),
	path('pop_music_gifts/', pop_music_gifts, name='pop_music_gifts'),
	path ('rock_music_gifts/', rock_music_gifts, name='rock_music_gifts'),
	path ('hip_hop_music_gifts/', hip_hop_music_gifts, name='hip_hop_music_gifts'),
	path ('jazz_music_gifts/', jazz_music_gifts, name='jazz_music_gifts'),
	path ('indie_alternative_gifts/', indie_alternative_gifts, name='indie_alternative_gifts'),
	path ('aries_gifts/', aries_gifts, name='aries_gifts'),
	path('taurus_gifts/', taurus_gifts, name='taurus_gifts'),
	path('gemini_gifts/', gemini_gifts, name='gemini_gifts'),
	path('cancer_gifts/', cancer_gifts, name='cancer_gifts'),
	path('leo_gifts/', leo_gifts, name='leo_gifts'),
	path('virgo_gifts/', virgo_gifts, name='virgo_gifts'),
	path('scorpio_gifts/', scorpio_gifts, name='scorpio_gifts'),
	path('sagittarius_gifts', sagittarius_gifts, name='sagittarius_gifts'),
	path('capricorn_gifts', capricorn_gifts, name='capricorn_gifts'),
    path ('submit/' , submit, name='submit')
	
    
]
