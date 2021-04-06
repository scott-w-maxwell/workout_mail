# Three levels: 1, 2, 3 (Easy Medium Hard)
# Five different workout_types: Legs, Core, Chest, Shoulders, Arms
# A link to a picture demonstrating the workout
# A link to a video demonstrating the workout

class Exercise:
	
	def __init__(self, name, workout_type, reps, sets, video_url):

		
		self.name = name
		self.exercise_type = exercise_type
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

	def __init__(exercises, level):

		# calculate amount of reps and sets
		for exercise in exercieses:
			exercise.reps = exercise.reps * level
			exercise.sets = exercise.sets * level


class Workout_Schedule:
	# TODO - create the properties of the workout_schedule class
	def __init__(days_per_week):
		pass

