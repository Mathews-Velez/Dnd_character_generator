import setuptools

with open("README.md", 'r') as f:
	long_description = f.read()

setuptools.setup(
	name = "dnd-character-generator",
	version = "1.0.0",
	author = "Mathews Velez",
	author_email = "velezmathew@gmail.com",
	description = "Quickly generate random DND characters",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/mathews-velez/dnd-_character_generator",
	packages = [
		"dnd_character_generator",
		"dnd_character_generator/Background_files",
		"dnd_character_generator/Class_files",
		"dnd_character_generator/Race_files"
	],
	package_dir = {
		"dnd_character_generator": "src",
		"dnd_character_generator/Background_files": "src/Background_files",
		"dnd_character_generator/Class_files": "src/Class_files",
		"dnd_character_generator/Race_files": "src/Race_files"
	},
	classifiers = [
		"License :: OSI Approved :: GNU Affero General Public License v3",
		"Natural Language :: English",
		"Operating System :: Unix",
		"Programming Language :: Python :: 3.8"
	],
	entry_points = {
		"console_scripts": [
			"dcg=dnd_character_generator.__main__:main"
		]
	},
	python_requires = ">=3.7"
)
