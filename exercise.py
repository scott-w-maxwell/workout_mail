# Three levels: 1, 2, 3 (Easy Medium Hard)
# Five different workout_types: Legs, Core, Chest, Shoulders, Arms
# A link to a picture demonstrating the workout
# A link to a video demonstrating the workout

class Exercise:
	
	def __init__(self, name, workout_type, reps, sets, video_url):

		
		self.name = name
		self.type = workout_type
		self.reps = reps
		self.sets = sets
		self.picture_url = picture_url
		self.video_url = video_url

		#if self.level == 'Easy':
		#if self.level == 'Medium':
		#if self.level == 'Hard':

		return self


# Include
class Routine:

	def __init__(exercise, level):
