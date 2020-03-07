// read data from a txt file, write into a Eigen::MatrixXs
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
         if (line[k] == ',')
             line[k] =' ';
		std::stringstream ss(line);
		double d;
		while (ss >> d) {
			if (j == col) {
				++i;
				j = 0;
			}
			m(i, j) = d;
			++j;
		}
	}
  Parameter = m;
}