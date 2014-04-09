# Moviecutter
					
### What is it?

Moviecutter is a simple Python script that uses scraper APIs — created using [Kimono](http://kimonolabs.com) and Niels Lemmens's Python implementation of the [Can I Stream It? API](https://github.com/Bulv1ne/CanIStreamIt) — to compile streaming options for every movie which (a) received an 81 or higher on [Metacritic](http://www.metacritic.com/browse/movies/score/metascore/all?sort=desc&page=0) (b) is in the [Rotten Tomatoes Top 100 list](http://www.rottentomatoes.com/top/bestofrt/?category=0) or (c) is in the [Movie Review Query Engine (MRQE) top 100](http://www.mrqe.com/lists/100-best-films/mrqes-100-best-ranked-films). It then outputs a list of all qualifying movies, along with the relevant review aggregator score and streaming availability of each, into a CSV file for easy spreadsheet manipulation.

### Dependencies

Moviecutter requires Niels Lemmens's CanIStreamIt package, which you can install using pip:

> pip install CanIStreamIt

If you do not have pip, [download it](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) and run:

> python get-pip.py

Then run pip to install CanIStreamIt.

### Usage

Once CanIStreamIt is installed, clone or download the Moviecutter project directory. In a terminal window, open the directory. Open the project directory and run moviecutter.py:

> python moviecutter.py

By default, the CSV file will be named "moviecutter.csv" and be placed in the Downloads folder of the user's home directory. Edit the value of the variable "writepath" at the top of the script if you would like it to write elsewhere.

### Licensing

Moviecutter is released under the MIT license. Please see the file called LICENSE for more information.
