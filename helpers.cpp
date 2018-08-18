/**
	helpers.cpp

	Purpose: helper functions which are useful when
	implementing a 2-dimensional histogram filter.

	This file is incomplete! Your job is to make the
	normalize and blur functions work. Feel free to 
	look at helper.py for working implementations 
	which are written in python.
*/

#include <vector>
#include <iostream>
#include <cmath>
#include <string>
#include <fstream> 
//#include "debugging_helpers.cpp"

using namespace std;

/**
	TODO - implement this function

    Normalizes a grid of numbers. 

    @param grid - a two dimensional grid (vector of vectors of floats)
		   where each entry represents the unnormalized probability 
		   associated with that grid cell.

    @return - a new normalized two dimensional grid where the sum of 
    	   all probabilities is equal to one.
*/
vector< vector<float> > normalize(vector< vector <float> > grid) {
	
	vector< vector<float> > newGrid;

	// todo - your code here

	float sumofpriorbeliefs = 0.0;

	for (int i = 0; i < grid.size(); i++)
	{
		for (int j = 0; j < grid[0].size(); j++)
		{
			sumofpriorbeliefs = sumofpriorbeliefs + grid[i][j];
		}
	}

	vector<float> newGridrow;

	for (int rows = 0; rows < grid.size(); rows++)
	{
		newGridrow.clear();

		for(int colmn = 0; colmn < grid[rows].size(); colmn++)
		{
			newGridrow.push_back(grid[rows][colmn] / sumofpriorbeliefs);
			
		}

		newGrid.push_back(newGridrow);

	}


	return newGrid;
}

/**
	TODO - implement this function.

    Blurs (and normalizes) a grid of probabilities by spreading 
    probability from each cell over a 3x3 "window" of cells. This 
    function assumes a cyclic world where probability "spills 
    over" from the right edge to the left and bottom to top. 

    EXAMPLE - After blurring (with blurring=0.12) a localized 
    distribution like this:

    0.00  0.00  0.00 
    0.00  1.00  0.00
    0.00  0.00  0.00 

    would look like this:
	
	0.01  0.02	0.01
	0.02  0.88	0.02
	0.01  0.02  0.01

    @param grid - a two dimensional grid (vector of vectors of floats)
		   where each entry represents the unnormalized probability 
		   associated with that grid cell.

	@param blurring - a floating point number between 0.0 and 1.0 
		   which represents how much probability from one cell 
		   "spills over" to it's neighbors. If it's 0.0, then no
		   blurring occurs. 

    @return - a new normalized two dimensional grid where probability 
    	   has been blurred.
*/
vector < vector <float> > blur(vector < vector < float> > grid, float blurring) {

	vector < vector <float> > newGrid(grid.size(), vector<float>(grid[0].size(), 0.0));
	
	// your code here

	int height = grid.size();

	int width = grid[0].size();

	float center_prob = 1.0 - blurring;

	float corner_prob = blurring / 12.0;

	float adjacent_prob = blurring / 6.0;

	vector < vector< float > > window;

	vector<float> newrow;

	float val;

	for (int i = 0; i < 3; i++)
	{
		newrow.clear();
		for (int j = 0; j < 3; j++)
		{
			switch (i)
			{
			case 0:
				switch (j)
				{
				case 0: val = corner_prob;
					break;
				case 1: val = adjacent_prob;
					break;
				case 2: val = corner_prob;
					break;
				default:
					break;
				}
				//newrow.push_back(val);
				break;
			case 1:
				switch (j)
				{
				case 0: val = adjacent_prob;
					break;
				case 1: val = center_prob;
					break;
				case 2: val = adjacent_prob;
					break;
				default:
					break;
				}
				//newrow.push_back(val);
				break;
			case 2:
				switch (j)
				{
				case 0: val = corner_prob;
					break;
				case 1: val = adjacent_prob;
					break;
				case 2: val = corner_prob;
					break;
				default:
					break;
				}
				//newrow.push_back(val);
				break;
			default:
				break;
			}

			newrow.push_back(val);
		}

		window.push_back(newrow);
	}

  //  newGrid (height, vector<float>(width,0.0));

	vector<int> DX;

	vector<int> DY;

	DX.push_back(-1);

	DX.push_back(0);

	DX.push_back(1);

	DY.push_back(-1);

	DY.push_back(0);

	DY.push_back(1);

	float grid_val;

	int dy;

	int dx;

	float multiplier;

	int new_l;

	int new_k;

	for (int l = 0; l < height; l++)
	{
		for (int k=0;k < width;k++)
		{
			 grid_val = grid[l][k];

			//for (int dx = -1; dx < 2; dx++)
		     for (int ii = 0; ii < 3; ii++)
			{
				 dy = DY[ii];
				//for (int dy = -1; dy < 2; dy++)
				for (int jj = 0; jj < 3; jj++)
				{
					dx = DX[jj];

				    multiplier = window[ii][jj];

					new_l = (l + dy + height) % height;

				    new_k = (k + dx + width) % width;

					newGrid[new_l][new_k] += multiplier * grid_val;

				}

			}

		}
	}


	return normalize(newGrid);
}

/** -----------------------------------------------
#
#
#	You do not need to modify any code below here.
#
#
# ------------------------------------------------- */


/**
    Determines when two grids of floating point numbers 
    are "close enough" that they should be considered 
    equal. Useful for battling "floating point errors".

    @param g1 - a grid of floats
    
    @param g2 - a grid of floats

    @return - A boolean (True or False) indicating whether
    these grids are (True) or are not (False) equal.
*/
bool close_enough(vector < vector <float> > g1, vector < vector <float> > g2) {
	int i, j;
	float v1, v2;
	if (g1.size() != g2.size()) {
		return false;
	}

	if (g1[0].size() != g2[0].size()) {
		return false;
	}
	for (i=0; i<g1.size(); i++) {
		for (j=0; j<g1[0].size(); j++) {
			v1 = g1[i][j];
			v2 = g2[i][j];
			if (abs(v2-v1) > 0.0001 ) {
				return false;
			}
		}
	}
	return true;
}

bool close_enough(float v1, float v2) { 
	if (abs(v2-v1) > 0.0001 ) {
		return false;
	} 
	return true;
}

/**
    Helper function for reading in map data

    @param s - a string representing one line of map data.

    @return - A row of chars, each of which represents the
    color of a cell in a grid world.
*/
vector <char> read_line(string s) {
	vector <char> row;

	size_t pos = 0;
	string token;
	string delimiter = " ";
	char cell;

	while ((pos = s.find(delimiter)) != std::string::npos) {
		token = s.substr(0, pos);
		s.erase(0, pos + delimiter.length());

		cell = token.at(0);
		row.push_back(cell);
	}

	return row;
}

/**
    Helper function for reading in map data

    @param file_name - The filename where the map is stored.

    @return - A grid of chars representing a map.
*/
vector < vector <char> > read_map(string file_name) {
	ifstream infile(file_name);
	vector < vector <char> > map;
	if (infile.is_open()) {

		char color;
		vector <char> row;
		
		string line;

		while (std::getline(infile, line)) {
			row = read_line(line);
			map.push_back(row);
		}
	}
	return map;
}

/**
    Creates a grid of zeros

    For example:

    zeros(2, 3) would return

    0.0  0.0  0.0
    0.0  0.0  0.0

    @param height - the height of the desired grid

    @param width - the width of the desired grid.

    @return a grid of zeros (floats)
*/
vector < vector <float> > zeros(int height, int width) {
	int i, j;
	vector < vector <float> > newGrid;
	vector <float> newRow;

	for (i=0; i<height; i++) {
		newRow.clear();
		for (j=0; j<width; j++) {
			newRow.push_back(0.0);
		}
		newGrid.push_back(newRow);
	}
	return newGrid;
}

// int main() {
// 	vector < vector < char > > map = read_map("maps/m1.txt");
// 	show_grid(map);
// 	return 0;
// }

