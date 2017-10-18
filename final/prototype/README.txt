=> Version 1:

	* Restrictions:
		- Fixed container size
		- Objects with 1 dimension
		- Objects with random size 


	*implementations:
		- first_fit_unordered
			Unordered list of objects;
			Put the object in the first fitable container

		- first_fit_ordered  
			Objects sorted by their sizes: The crescent order
			Put the object in the first fitable container

		- biggest_n_smallest
			Objects sorted by their sizes: The crescent order
			Put the greatest object in container.
			If you can't put more big objects, try to pack the small ones into the same container

=> Version 2:
	
	* Restrictions:
		- Variable container size
		- Objects with 1 dimension
		- Objects with random size 


TODO:
	+ Add 2D objects.
	+ Evaluate the efficiency to different sizes distribution:
		- Linear (crescent, decrescent)
		- Triangular
		- Normal
		