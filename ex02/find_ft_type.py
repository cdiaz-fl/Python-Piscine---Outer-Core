def all_thing_is_obj(object: any) -> int:
	if isinstance(object, int):
		print("Type not found")
	else:
		print(f"{object + " is in the kitchen" if isinstance(object, str) else type(object).__name__.title()} : ", end="")
		print(type(object))
	return (42)