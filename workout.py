# Three levels: Easy, Medium, Hard
# Five different workout_types: Legs, Core, Chest, Shoulders, Arms
# A link to a picture demonstrating the workout
# A link to a video demonstrating the workout

class Workout:
	
	def __init__(self, name, workout_type, level, picture_url, video_url):

		
		self.name = name
		self.type = workout_type
		self.level = level
		self.picture_url = picture_url
		self.video_url = video_url

		#if self.level == 'Easy':
		#if self.level == 'Medium':
		#if self.level == 'Hard':

		return self