// read data from a txt file, write into a Eigen::MatrixXd
	#include <Eigen>
	path_W0 = "/home/letian/MDN/Parameter/weights_h0.txt"
	load_txt(const std::string& path_WG, Eigen::MatrixXd& WG)
	void load_txt(const std::string& path, Eigen::MatrixXd& Parameter)
	{
		ifstream in;
		std::string line;
		int row = Parameter.rows(), col = Parameter.cols();
		Eigen::MatrixXd m(row, col);

		in.open(path.c_str());	
		int i = 0, j = 0;
		while (std::getline(in, line)) {
		for (int k = 0; k < line.size(); k++)// 如果输入中有‘，’，将其换成空格
		{
			if (line[k] == ',')
				line[k] =' ';
		}
			std::stringstream ss(line);
			double d;
			while (ss >> d) 
			{
				if (j == col) 
				{
					++i;
					j = 0;
				}
				m(i, j) = d;
				++j;
			}
		}
		Parameter = m;
	}

	// 1. How does getline() work?
	// 	   Reads the entire line up to '\n' character or the delimiting character specified. 
	// 	   After reading the line, the control goes to the next line in the file.
	//     Also, it returns a boolean value of true if the read operation was successful, else false.

	// 2. How does stringstream() work?
			istringstream istr;
			istr.str("1 56.7");
			//上述两个过程可以简单写成 istringstream istr("1 56.7");
			int a;
			float b;
			istr >> a;
			istr >> b;


ifstream fin;
fin.open(index_number.c_str());
string interact_index;
while (!fin.eof())
{
    getline(fin, interact_index);
);
}
fin.close();