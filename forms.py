from django import forms
class QuestionnaireForm (forms.Form):
	gender = forms.ChoiceField(choices=[
		('male', 'Male'),
		('female', 'Female'),
		('others', 'Others')
		])
	hobby = forms.ChoiceField (choices=[
		('reading', 'Reading'),
		('sports', 'Sports'),
		('music,', 'Music'),
		('art', 'Art'),
		('others', 'Others')
	])
	unwind = forms.ChoiceField (choices=[
		('bubble-bath', 'Bubble-Bath'),
		('curling-up', 'Curling-Up'),
		('walk-run', 'Walk/Run'),
		('meditation', 'Meditation'),
		('cooking-meal', 'Cooking-Meal'),
		('exercise', 'Exercise')
	])

	secret_like = forms.ChoiceField (choices=[
		('chocolate', 'Chocolate'),
		('romantic-movies', 'Romantic-Movies'),
		('video-games', 'Video-Games'),
		('cartoons', 'Cartoons')

	])

	childhood_activity = forms.ChoiceField(choices=[
		('riding-bikes', 'Riding-Bikes'),
		('exploring-imaginative-worlds', 'Exploring-Imaginative-Worlds'),
		('creating-art'), ('Creating-Art')

	])

	genre = forms.ChoiceField(choices=[
		('pop', 'Pop'),
		('rock', 'Rock'),
		('hip-hop', 'Hip-Hop'),
		('jazz', 'Jazz'),
		('indie-alternative', 'Indie/Alternative')
	])

	zodiac = forms.ChoiceField(choices=[
		('aries', 'Aries'),
		('taurus', 'Taurus'),
		('gemini', 'Gemini'),
		('cancer', 'Cancer'),
		('leo', 'Leo'),
		('virgo', 'Virgo'),
		('scorpio', 'Scorpio'),
		('sagittarius', 'Sagittarius'),
		('capricorn', 'Capricorn'),
		('aquarius', 'Aquarius'),
		('pisces', 'Pisces')
	])

	food_type = forms.ChoiceField(choices=[
		('spicy', 'Spicy'),
		('sweet', 'Sweet'),
		('savoury', 'Savoury'),
		('comfort', 'Comfort'),
		('healthy', 'Healthy'),
		('dessert', 'Dessert')

	])

	stay_active = forms.ChoiceField(choices=[
		('running', 'Running'),
		('dancing', 'Dancing'),
		('weightlifting', 'Weightlifting'),
		('yoga', 'Yoga'),
		('swimming', 'Swimming'),
		('team-sports', 'Team-Sports')
	])

	new_skill = forms.ChoiceField(choices=[
		('cooking', 'Cooking'),
		('painting', 'Painting'),
		('language', 'Language-Learning'),
		('musical-instrument', 'Musical-Instrument'),
		('coding', 'Coding/Programming')

	])

	movie_tv_show = forms.ChoiceField(choices=[
		('action', 'Action'),
		('comedy', 'Comedy'),
		('drama', 'Drama'),
		('sci-fi', 'Sci-Fi'),
		('documentary', 'Documentary'),
		('animated', 'Animated')
	])

	express_creativity = forms.ChoiceField(choices=[
		('painting' , 'Painting'),
		('writing', 'Writing'),
		('crafting', 'Crafting'),
		('musical-instrument', 'Musical-Instrument'),
		('cooking', 'Cooking'),
		('designing', 'Designing')
	])

	comfort_food = forms.ChoiceField(choices=[
		('crusty-bread', 'Crusty-Bread'),
		('macaroni', 'Macaroni'),
		('mashed-potatoes', 'Mashed-Potatoes'),
		('chocolate-chip', 'Chocolate-Chip'),
		('grilled-cheese-sandwich', 'Grilled-Cheese-Sandwich')
	])

	board_game = forms.ChoiceField(choices=[
		('settles', 'Settles'),
		('ticket-to-ride', 'Ticket-To-Ride'),
		('scrabble', 'Scrabble'),
		('codenames', 'Codenames'),
		('pandemic', 'Pandemic'),
		('chess-or-checkers', 'Chess-Or-Checkers')
	])

	weekend_getaway = forms.ChoiceField(choices=[
		('relaxing-cabins', 'Relaxing-Cabins'),
		('exploring-city', 'Exploring-City'),
		('lounging-beach', 'Lounging-Beach'),
		('hiking-camping-trip', 'Hiking/Camping'),
		('spa-retreat', 'Spa-Retreat'),
		('landmarks-musuem', 'Landmarks/Musuem')
	])

	color = forms.ChoiceField(choices=[
		('red', 'Red'),
		('blue', 'Blue'),
		('green', 'Green'),
		('yellow', 'Yellow'),
		('pink', 'Pink'),
		('purple', 'Purple'),
		('orange', 'Orange')

	])

	fashion_style = forms.ChoiceField(choices=[
		('casual', 'Casual'),
		('classic', 'Classic'),
		('bohemian', 'Bohemian'),
		('trendy', 'Trendy'),
		('sporty', 'Sporty'),
		('elegant', 'Elegant'),
		('vintage', 'Vintage')
	])

	accessories = forms.ChoiceField(choices=[
		('jewelry', 'Jewelry'),
		('watches', 'Watches'),
		('scarves', 'Scarves'),
		('sunglasses', 'Sunglasses'),
		('handbags' , 'Handbags'),
		('hats', 'Hats'),
		('caps', 'Caps'),
		('belts', 'Belts')
	])

	gadgets = forms.ChoiceField(choices=[
		('smartphones', 'Smartphones'),
		('laptops', 'Laptops'),
		('tablets', 'Tablets'),
		('smartwatches-fitnesstracker', 'Smartwatches-Fitnesstracker'),
		('cameras', 'Cameras'),
		('gaming-consoles', 'Gaming-Consoles'),
		('audio-devices', 'Audio-Devices')
	])

	fitness_goals = forms.ChoiceField(choices=[
		('weight-losss', 'Weight-Loss'),
		('muscle-gain', 'Muscle-Gain'),
		('cardio', 'Cardio'),
		('flexibility-yoga', 'Flexibility-Yoga'),
		('sports-performance', 'Sports-Performance')

	])

	scent = forms.ChoiceField(choices=[
		('floral', 'Floral'),
		('woody', 'Woody'),
		('citrus', 'Citrus'),
		('fresh-aquatic', 'Fresh/Aquatic'),
		('spicy', 'Spicy'),
		('oriental', 'Oriential'),
		('fruity', 'Fruity')

	])

	home_decor = forms.ChoiceField(choices=[
		('minimalist', 'Minimalist'),
		('vintage-retro', 'Vintage/Retro'),
		('modern-contemporary', 'Modern/Contemporary'),
		('bohemian', 'Bohemian'),
		('scandinavian', 'Scandinavian'),
		('industrial', 'Industrial'),
		('farmhouse', 'Farmhouse')
	])

	beverage = forms.ChoiceField(choices=[
		('coffee', 'Coffee'),
		('tea', 'Tea'),
		('soft-drinks', 'Soft-Drinks'),
		('juice', 'Juice'),
		('beer', 'Beer'),
		('wine', 'Wine'),
		('cocktails', 'Cocktails')
	])

	profession = forms.ChoiceField(choices=[
		('technology-it', 'Information Technology'),
		('healthcare-medicine', 'Healthcare-Medicine'),
		('education' , 'Education'),
		('finance', 'Finance'),
		('creative', 'Creative'),
		('business','Business'),
		('hospitality', 'Hospitality')
	])

	sports = forms.ChoiceField(choices=[
		('football', 'Football'),
		('basketball', 'Basketball'),
		('baseball', 'Baseball'),
		('tennis', 'Tennis'),
		('golf', 'Golf'),
		('ping-pong', 'Ping-Pong'),
		('rugby', 'Rugby'),
		('hockey', 'Hockey')
		
	])

	pets = forms.ChoiceField(choices=[
		('dogs', 'Dog(s)'),
		('cats', 'Cat(s)'),
		('birds', 'Bird(s)'),
		('fish', 'Fish'),
		('reptiles', 'Reptiles/Amphibians'),
		('small-mammals','Small-Mammals(Rabbits-Hamsters)'),
		('none', 'None')
   
   
		
   
	])
